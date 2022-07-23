# FastAPI

[FastApi](https://fastapi.tiangolo.com/) provide a fasted way to deliver a higth quality API, with automated OpenAPI documentation 🥰.

[Pipenv](https://pipenv.pypa.io/en/latest/) allows to manage dependencies and virtualenv of python in a simple way. It allows to differentiate between prod and dev dependencies, to manage a lock file and to have scripts (like npm).

[Alembic](https://pypi.org/project/alembic/) allows for the industrialization of database migration.

See also:
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [pytest](pytest)
- [mypy](http://mypy-lang.org/)

## Getting started

**Requirement**

- [Python == 3.10](https://www.python.org/downloads/)
- [pipenv](https://pypi.org/project/pipenv/)
- Set enviroment variable (for pipenv):
  ```shell
  PIPENV_DONT_LOAD_ENV = 1
  PIPENV_VENV_IN_PROJECT = 1
  ```
- Add local `.env` file
  ```shell
  DEBUG=true

  SQLALCHEMY_DATABASE_URL = "sqlite:///./data.sqlite"
  ```

**Install**

```
pipenv install --dev
```

**Init DB**

```
pipenv run migrate-db-run
```

**Runnning**

```bash
pipenv run start
```

Access to local api <http://localhost:8080/api/>

> You can change the port:
>  ```bash
>  pipenv run -- start --port 8081
>  ```

## Toolings

**Code formating**

```bash
pipenv run format
```

**Code linting**

```bash
pipenv run lint
```

**Testing**

```bash
pipenv run test
```

## Project structure

```
📂fastapi
 ┣ 📂alembic
 ┣ 📂src
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📂dependencies
 ┃ ┃ ┣ endpoints
 ┃ ┃ ┗ 📜route.py
 ┃ ┣ 📂core
 ┃ ┣ 📂enums
 ┃ ┣ 📂models
 ┃ ┣ 📂schemas
 ┃ ┣ 📂services
 ┃ ┗ 📜app.py
 ┣ 📂tests
 ┃ ┣ 📂integration
 ┃ ┣ 📂mocks
 ┃ ┣ 📂utils
 ┃ ┣ 📜.env
 ┃ ┗ 📜conftest.py
 ┣ 📜.env
 ┣ 📜_version.py
 ┣ 📜alembic.ini
 ┣ 📜main.py
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜setup.cfg
 ┗ 📜tasks.py
```

| Folder/File | Descripton |
| ----------- | ---------- |
| 📂alembic | Alembic, DB migration scripts |
||
| 📂src/api/dependencies | [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) to inject in routes |
| 📂src/api/routes | Routes **FastAPI** (only HTTP, no bussiness here) |
| 📜src/api/route.py | Routes register **FastAPI** |
| 📂src/core | Core code, no bussiness here |
| 📂src/enums | String enum compatible for **Pydantic** and **SqlAlchemy** |
| 📂src/models | **SqlAlchemy** models for **DB** |
| 📂src/schemas | Pydantic schemas for **OpenAPI** |
| 📂src/services | Bussiness code |
| 📜src/app.py | **FastAPI** initialisation |
||
| 📂tests/integration | Integration tests |
| 📂tests/mocks | Mocks file for unit and integration tests |
| 📂tests/utils | Test utilities |
| 📜tests/.env | .env specific to the tests |
| 📜tests/conftest.py | Global pytest configuration |
||
| 📜.env | Your local `.env`, must not be committed to `.gitignore`. |
| 📜_version.py | File containing the version, can by bump by standart-version 😉 |
| 📜alembic.ini | **Alembic** config file |
| 📜main.py | Backend entry point |
| 📜Pipfile | **pipenv** dependency file |
| 📜Pipfile.lock | Dependency locks |
| 📜setup.cfg | Tools (**pytest**, **flake8**, **isort**, **mypy**) configurations |
| 📜tasks.py | Task file for chaining `pipenv run` commands (not natively supported 😭) |
