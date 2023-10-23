
# README.md

## Overview

This script is designed to gather property value request data from OpenDataSoft and format it for use in the `data.gouv.fr` platform. The data is sourced from the [BuildingRef France Demandes de Valeurs Foncières Géolocalisées Millesime dataset](https://public.opendatasoft.com/explore/dataset/buildingref-france-demande-de-valeurs-foncieres-geolocalisee-millesime/information/?disjunctive.date_mutation&disjunctive.nature_mutation&disjunctive.dep_code&disjunctive.type_local&disjunctive.code_nature_culture&disjunctive.nature_culture&disjunctive.code_nature_culture_speciale&disjunctive.nature_culture_speciale&disjunctive.dep_name&disjunctive.reg_code&disjunctive.reg_name&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImJ1aWxkaW5ncmVmLWZyYW5jZS1kZW1hbmRlLWRlLXZhbGV1cnMtZm9uY2llcmVzLWdlb2xvY2FsaXNlZS1taWxsZXNpbWUiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmRhdGVfbXV0YXRpb24iOnRydWUsImRpc2p1bmN0aXZlLm5hdHVyZV9tdXRhdGlvbiI6dHJ1ZSwiZGlzanVuY3RpdmUuZGVwX2NvZGUiOnRydWUsImRpc2p1bmN0aXZlLnR5cGVfbG9jYWwiOnRydWUsImRpc2p1bmN0aXZlLmNvZGVfbmF0dXJlX2N1bHR1cmUiOnRydWUsImRpc2p1bmN0aXZlLm5hdHVyZV9jdWx0dXJlIjp0cnVlLCJkaXNqdW5jdGl2ZS5jb2RlX25hdHVyZV9jdWx0dXJlX3NwZWNpYWxlIjp0cnVlLCJkaXNqdW5jdGl2ZS5uYXR1cmVfY3VsdHVyZV9zcGVjaWFsZSI6dHJ1ZSwiZGlzanVuY3RpdmUuZGVwX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLnJlZ19jb2RlIjp0cnVlLCJkaXNqdW5jdGl2ZS5yZWdfbmFtZSI6dHJ1ZSwicmVmaW5lLmRhdGVfbXV0YXRpb24iOiIyMDE5In19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoidmFsZXVyX2ZvbmNpZXJlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJkYXRlX211dGF0aW9uIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIifV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,0,0&basemap=jawg.light).

The output is formatted to be compatible with the [Demandes de Valeurs Foncières Géolocalisées dataset on data.gouv.fr](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/).

## How it works

1. **Data Retrieval**: The script fetches the required property data from OpenDataSoft using its API.
2. **Data Transformation**: The raw data is then processed and transformed into the desired format.
3. **Output**: The transformed data is saved to a file, ready to be uploaded to `data.gouv.fr`.

## Usage

To use the script:

1. Ensure you have the necessary Python libraries installed.
2. Run the script:

```bash
python opendatasoft_to_dvg_geo.py
```

3. The output will be saved to a specified file (refer to the script for exact file name and path).

## Dependencies

- Python 3.x
- pandas
