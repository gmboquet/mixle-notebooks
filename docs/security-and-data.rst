Security and Data Handling
==========================

Notebooks often expose more data than library tests: rendered tables, plots,
host paths, environment output, and intermediate artifacts. Public release
notebooks need explicit hygiene.

Inputs
------

Notebook inputs should be synthetic, public, or clearly documented. Do not
commit private datasets to make an example run. If a notebook needs private
data, mark it blocked for public release validation.

When public data has licensing or attribution requirements, record them next to
the notebook or dataset-preparation script. A notebook that runs locally is not
automatically cleared for public release.

Credentials
-----------

Do not store API keys, tokens, private endpoints, cloud credentials, or local
database passwords in notebooks. Use environment-variable names and
document required services.

Execution Reports
-----------------

Bitrot reports should capture status, timeout, worker count, and the first
meaningful failure. They should not paste long private logs or raw payloads.

Output Review
-------------

Treat notebook output as publication material — it can carry secrets or data
previews just as easily as a shell log can. Before committing a rerun,
inspect rendered tables, plots, tracebacks, shell output, file paths,
package versions, environment variables, and widget state. If an output cell
is necessary for the reader, keep it small and source-backed; if it's only a
transient execution artifact, clear it and rely on the execution manifest
for evidence instead.

Path Hygiene
------------

Notebook output should not reveal developer-local absolute paths, machine
names, account identifiers, or private service URLs. If a traceback includes
those values, clear the output and preserve a redacted failure summary in the
execution manifest instead.
