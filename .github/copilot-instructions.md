# Copilot instructions for this repository

## Project overview

This repository is a small MongoDB learning project built around the PyMongo driver. It is not a packaged application or a framework project. The code is mainly a set of standalone Python scripts that demonstrate how to connect to MongoDB, insert documents, query data, update records, delete records, and inspect databases/collections.

The main pattern is:

- `connect.py` establishes the local MongoDB connection
- `insert.py`, `find.py`, `update.py`, `delete.py`, and `show_db_col.py` are CRUD-focused examples
- `practice_mongoDB/` contains more detailed worked examples and sample collections such as `quiz-verse` and `results`
- Each file is intentionally script-style and runs directly under `__main__` without a package/module entry point

## Build, test, and lint commands

There is no formal build, test, or lint configuration in this repository (no `pyproject.toml`, `requirements.txt`, `pytest.ini`, `Makefile`, or similar setup files were found).

Use the project virtual environment if needed:

```powershell
# Windows
.\venv\Scripts\python.exe .\connect.py
```

Or, if the environment is active:

```powershell
python .\find.py
python .\practice_mongoDB\find_prac.py
```

These scripts expect MongoDB to be running locally on `mongodb://localhost:27017`.

For a single script or example, run that file directly instead of invoking a broader suite. There is no single test runner for the repo; validation is done by executing the relevant Python example against a local MongoDB instance.

## High-level architecture

The repository is organized around direct, script-based examples rather than layered application code.

- Top-level files are independent learning scripts and often call `MongoClient("mongodb://localhost:27017")` immediately in `if __name__ == "__main__":`
- The database and collection names are hard-coded in the examples (for example `tset-database`, `test-collection`, and `quiz-verse` / `results`)
- `practice_mongoDB/` acts as the “hands-on lab” folder: it contains more realistic query examples, filtering, sorting, and projection usage
- The repo is educational and exploratory: it emphasizes understanding PyMongo APIs and CRUD patterns over application structure or reusable service abstractions

In practice, to understand the codebase, read a connection example first, then read the CRUD script that matches the operation you care about. The flow is mostly linear and self-contained within a single file.

## Key conventions

- All examples use the direct `pymongo.MongoClient` pattern and local connection strings.
- Scripts assume a running MongoDB instance on localhost port 27017 and do not include environment-variable-based config.
- Code is intentionally simple and procedural; there are no classes, dependency injection layers, or app factories.
- Database names and collection names are embedded directly in the script, so examples are meant to be run and observed as-is.
- The repo favors short, educational examples over abstraction. If a behavior is being demonstrated, it is usually implemented in one file with a few immediate `print(...)` calls.
- Query examples commonly use field filters and PyMongo operators such as `$gte`, `$gt`, `$lte`, `$in`, `$and`, and sort options such as `ASCENDING` and `DESCENDING`.

## Project-specific notes

- `README.md` is the authoritative overview and describes the learning path for MongoDB + PyMongo.
- If you add or modify examples, keep them runnable as standalone scripts and preserve the local MongoDB assumption unless the repo explicitly documents otherwise.
- When validating changes, prefer running the exact script affected by the change rather than broad repo-wide checks, because there is no established test suite or CI harness here.
