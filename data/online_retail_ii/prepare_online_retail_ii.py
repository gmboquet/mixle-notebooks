"""Prepare compact IBP-friendly artifacts from UCI Online Retail II.

Inputs:
    online_retail_ii.zip

Outputs:
    transactions_top150.csv
    items_top150.csv
    manifest.json

The notebook consumes the CSV/JSON artifacts, not the Excel workbook, so normal
notebook runs do not need openpyxl.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
RAW_ZIP = ROOT / "online_retail_ii.zip"
RAW_XLSX = ROOT / "online_retail_II.xlsx"
TOP_K = 150

SOURCE = {
    "name": "Online Retail II",
    "creator": "Daqing Chen",
    "repository": "UCI Machine Learning Repository",
    "dataset_page": "https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii",
    "download_url": "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip",
    "doi": "10.24432/C5CG6D",
    "license": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
    "citation": "Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D.",
}


SERVICE_CODES = {
    "POST", "D", "M", "DOT", "C2", "BANK CHARGES", "AMAZONFEE", "CRUK",
    "S", "DCGS0003", "DCGS0004", "DCGS0055", "DCGS0057", "DCGS0066P",
}
SERVICE_DESCRIPTION_RE = re.compile(
    r"(?:POSTAGE|MANUAL|DISCOUNT|CARRIAGE|AMAZON|BANK CHARGES|ADJUST|"
    r"BAD DEBT|CRUK|SAMPLE|DAMAGED|FOUND|LOST|CHECK)",
    flags=re.IGNORECASE,
)


def extract_workbook() -> None:
    if RAW_XLSX.exists():
        return
    if not RAW_ZIP.exists():
        raise FileNotFoundError(
            f"Missing {RAW_ZIP}. Download it from {SOURCE['download_url']} first."
        )
    with ZipFile(RAW_ZIP) as zf:
        zf.extract("online_retail_II.xlsx", ROOT)


def read_workbook() -> pd.DataFrame:
    extract_workbook()
    frames = []
    xl = pd.ExcelFile(RAW_XLSX, engine="openpyxl")
    for sheet in xl.sheet_names:
        frame = pd.read_excel(
            RAW_XLSX,
            sheet_name=sheet,
            engine="openpyxl",
            dtype={"Invoice": str, "StockCode": str, "Customer ID": str},
        )
        frame["SourceSheet"] = sheet
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)


def clean_lines(df: pd.DataFrame) -> pd.DataFrame:
    rv = df.rename(columns={
        "Invoice": "invoice_id",
        "StockCode": "stock_code",
        "Description": "description",
        "Quantity": "quantity",
        "InvoiceDate": "invoice_date",
        "Price": "unit_price",
        "Customer ID": "customer_id",
        "Country": "country",
    }).copy()

    rv["invoice_id"] = rv["invoice_id"].astype(str).str.strip()
    rv["stock_code"] = rv["stock_code"].astype(str).str.strip().str.upper()
    rv["description"] = rv["description"].astype(str).str.strip()
    rv["customer_id"] = rv["customer_id"].replace({"nan": ""}).fillna("").astype(str).str.replace(r"\.0$", "", regex=True)
    rv["line_revenue"] = rv["quantity"].astype(float) * rv["unit_price"].astype(float)

    positive_sale = (
        ~rv["invoice_id"].str.startswith("C", na=False)
        & (rv["quantity"] > 0)
        & (rv["unit_price"] > 0)
        & rv["stock_code"].notna()
        & rv["description"].notna()
    )
    product_like = (
        rv["stock_code"].str.contains(r"\d", na=False)
        & ~rv["stock_code"].isin(SERVICE_CODES)
        & ~rv["description"].str.contains(SERVICE_DESCRIPTION_RE, na=False)
    )
    return rv.loc[positive_sale & product_like].copy()


def most_common_description(series: pd.Series) -> str:
    values = series.dropna().astype(str).str.strip()
    if len(values) == 0:
        return ""
    return values.value_counts().index[0]


def build_artifacts(clean: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    item_stats = (
        clean.groupby("stock_code")
        .agg(
            description=("description", most_common_description),
            invoice_count=("invoice_id", "nunique"),
            total_quantity=("quantity", "sum"),
            total_revenue=("line_revenue", "sum"),
        )
        .sort_values(["invoice_count", "total_revenue"], ascending=False)
        .head(TOP_K)
        .reset_index()
    )
    item_stats.insert(0, "item_index", np.arange(len(item_stats)))
    stock_to_idx = dict(zip(item_stats["stock_code"], item_stats["item_index"]))

    invoice_totals = (
        clean.groupby("invoice_id")
        .agg(
            invoice_date=("invoice_date", "min"),
            country=("country", most_common_description),
            customer_id=("customer_id", most_common_description),
            line_count=("stock_code", "size"),
            distinct_products=("stock_code", "nunique"),
            total_quantity=("quantity", "sum"),
            total_revenue=("line_revenue", "sum"),
        )
        .reset_index()
    )

    top_lines = clean.loc[clean["stock_code"].isin(stock_to_idx), ["invoice_id", "stock_code"]].copy()
    top_lines["item_index"] = top_lines["stock_code"].map(stock_to_idx).astype(int)
    top_grouped = (
        top_lines.groupby("invoice_id")["item_index"]
        .apply(lambda s: " ".join(map(str, sorted(set(s)))))
        .reset_index(name="active_indices")
    )

    transactions = invoice_totals.merge(top_grouped, on="invoice_id", how="inner")
    transactions["top_item_count"] = transactions["active_indices"].str.split().map(len)
    transactions = transactions.loc[transactions["top_item_count"] > 0].copy()
    transactions["invoice_date"] = pd.to_datetime(transactions["invoice_date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    transactions = transactions.sort_values("invoice_date").reset_index(drop=True)

    manifest = {
        "source": SOURCE,
        "preparation": {
            "top_k_items": TOP_K,
            "filters": [
                "drop cancellation invoices whose invoice id starts with C",
                "keep positive quantity and positive unit price lines",
                "drop service/adjustment style stock codes and descriptions",
                "represent each invoice by active item indices among the top 150 products by invoice count",
            ],
            "raw_rows": int(len(clean)),
            "transactions_with_top_items": int(len(transactions)),
            "num_items": int(len(item_stats)),
            "date_min": transactions["invoice_date"].min(),
            "date_max": transactions["invoice_date"].max(),
            "countries": int(transactions["country"].nunique()),
            "customers": int(transactions.loc[transactions["customer_id"] != "", "customer_id"].nunique()),
        },
    }
    return transactions, item_stats, manifest


def main() -> None:
    raw = read_workbook()
    clean = clean_lines(raw)
    transactions, items, manifest = build_artifacts(clean)

    transactions.to_csv(ROOT / "transactions_top150.csv", index=False)
    items.to_csv(ROOT / "items_top150.csv", index=False)
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest["preparation"], indent=2))


if __name__ == "__main__":
    main()
