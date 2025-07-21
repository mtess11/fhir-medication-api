# FHIR Medication API

A Django + GraphQL backend for working with medication data, aligned with [HL7 FHIR](https://hl7.org/fhir/medication.html) standards. This project supports syncing real-world medication data from [OpenFDA](https://open.fda.gov/apis/drug/ndc/), exposing a GraphQL API for querying and managing medications.

---

## 🔧 Tech Stack

- **Python 3.13**
- **Django 4.x**
- **Graphene-Django** (GraphQL API)
- **SQLite** (default dev DB)
- **OpenFDA Drug NDC API** (for medication sync)
- **Pytest** (for testing)

---

## 🚀 Features

- FHIR-aligned `Medication` model (fields: code, status, form, manufacturer, etc.)
- GraphQL and REST APIs for CRUD operations
- Management command to import medication data from OpenFDA
- Test suite for models, sync logic, and API behavior
- Ready to integrate with frontend apps (e.g. Spezi for iOS)

---

## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fhir-medication-api.git
cd fhir-medication-api
```
### 2. Set up virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 3. Run migrations

```bash
python manage.py migrate
```
### 4. Import medication data from OpenFDA

```bash
python manage.py import_fda_data
```

### 5. Run the dev server

```bash
python manage.py runserver
```

### 6. Open GraphQL Playground

Visit: http://localhost:8000/graphql/

```graphql
Try a sample query:

graphql
Copy
Edit
query {
  medications {
    id
    code
    manufacturer
    form
  }
}

```
---

## 🧪 Running Tests

```bash
pytest
```
Make sure the following packages are installed:

```bash
pip install pytest pytest-django
```
---
## Management Commands

`import_fda_data`: Fetches and stores 20 medication records from OpenFDA

```bash
python manage.py import_fda_data
```
---
## Planned Roadmap
- [x] Add GraphQL filtering & pagination
- [ ] Add update/delete mutations
- [ ] Export medication data as full FHIR-compliant JSON
- [ ] Add CI for testing
- [ ] Connect to frontend (e.g. Spezi for iOS)
 
---
MIT License

---
Developed by Mariya Teslya

