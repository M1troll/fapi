### Simple FastApi application

### Prepare python env using pyenv-virtualenv

1. Create separate python virtual environment:

```bash
pyenv virtualenv-delete --force fapi
pyenv install 3.11 --skip-existing
pyenv virtualenv `pyenv latest 3.11` fapi
pyenv local fapi
pyenv shell fapi
```

2. Install requirements:

```bash
pip install -r requirements/develop.in
```