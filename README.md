Test repository for comparing issues with testcontainers and responses version 0.12.0 and 0.12.1

Replace the responses version in the Pipfile and reinstall dependencies using:
```
pipenv --rm
pipenv install
```

Run tests:
```
pipenv run pytest tests/ -s
```