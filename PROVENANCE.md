# Data Provenance

## 1) Routes of Administration — EMA SPOR RMS

* **Source**: EMA SPOR RMS Web UI → list: “Routes and Methods of Administration”.
* **Subset**: For the PoC, only 4 rows were manually selected and stored in `data/routes_of_administration.csv`.
* **Fields used**: `identifier`, `term_name`, `source_id`, `status`.
* **Linking**: Each route is modeled with the local IRI `ex:route/{identifier}` and linked to the RMS representation IRI via `skos:exactMatch`.
* **Next (production)**: Replace the manual CSV with the **RMS API/Export** output and record the extraction date and URL.

## 2) Synthetic Domain Data

* **products.csv / substances.csv / organizations.csv** contain synthetic but realistic data (no PHI/PII).
* **Purpose**: To demonstrate mapping and linking between product → route → substance → organization.

## 3) Reproducibility & Change Log

* This PoC is **deterministic**; rerunning it will produce identical outputs.
* When replacing with live sources, record the **extraction date/time** and **endpoint(s)** here:

  * Extraction date: *YYYY-MM-DD*
  * Endpoint(s): *e.g., RMS API …*
