# fastapi_workshop

[![codecov](https://codecov.io/gh/diogoro/fastapi-workshop/branch/main/graph/badge.svg?token=fastapi-workshop_token_here)](https://codecov.io/gh/diogoro/fastapi-workshop)
[![CI](https://github.com/diogoro/fastapi-workshop/actions/workflows/main.yml/badge.svg)](https://github.com/diogoro/fastapi-workshop/actions/workflows/main.yml)

Awesome fastapi_workshop created by diogoro

## Install


### Running on gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/diogoro/fastapi-workshop)

### from source
```bash
git clone https://github.com/diogoro/fastapi-workshop fastapi_workshop
cd fastapi_workshop
make install
```

## Executing

```bash
$ fastapi_workshop run --port 8080
```

or

```bash
python -m fastapi_workshop run --port 8080
```

or

```bash
$ uvicorn fastapi_workshop:app
```

## CLI

```bash
❯ fastapi_workshop --help
Usage: fastapi_workshop [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  create-user  Create user
  run          Run the API server.
  shell        Opens an interactive shell with objects auto imported
```

### Creating a user

```bash
❯ fastapi_workshop create-user --help
Usage: fastapi_workshop create-user [OPTIONS] USERNAME PASSWORD

  Create user

Arguments:
  USERNAME  [required]
  PASSWORD  [required]

Options:
  --superuser / --no-superuser  [default: no-superuser]
  --help 
```

**IMPORTANT** To create an admin user on the first run:

```bash
fastapi_workshop create-user admin admin --superuser
```

### The Shell

You can enter an interactive shell with all the objects imported.

```bash
❯ fastapi_workshop shell       
Auto imports: ['app', 'settings', 'User', 'engine', 'cli', 'create_user', 'select', 'session', 'Content']

In [1]: session.query(Content).all()
Out[1]: [Content(text='string', title='string', created_time='2021-09-14T19:25:00.050441', user_id=1, slug='string', id=1, published=False, tags='string')]

In [2]: user = session.get(User, 1)

In [3]: user.contents
Out[3]: [Content(text='string', title='string', created_time='2021-09-14T19:25:00.050441', user_id=1, slug='string', id=1, published=False, tags='string')]
```

## API

Run with `fastapi_workshop run` and access http://127.0.0.1:8000/docs

![](https://raw.githubusercontent.com/rochacbruno/fastapi-project-template/master/docs/api.png)


**For some api calls you must authenticate** using the user created with `fastapi_workshop create-user`.

## Testing

``` bash
❯ make test
Black All done! ✨ 🍰 ✨
13 files would be left unchanged.
Isort All done! ✨ 🍰 ✨
6 files would be left unchanged.
Success: no issues found in 13 source files
================================ test session starts ===========================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- 
/fastapi-project-template/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /fastapi-project-template
plugins: cov-2.12.1
collected 10 items                                                                                                                               

tests/test_app.py::test_using_testing_db PASSED                           [ 10%]
tests/test_app.py::test_index PASSED                                      [ 20%]
tests/test_cli.py::test_help PASSED                                       [ 30%]
tests/test_cli.py::test_cmds_help[run-args0---port] PASSED                [ 40%]
tests/test_cli.py::test_cmds_help[create-user-args1-create-user] PASSED   [ 50%]
tests/test_cli.py::test_cmds[create-user-args0-created admin2 user] PASSED[ 60%]
tests/test_content_api.py::test_content_create PASSED                     [ 70%]
tests/test_content_api.py::test_content_list PASSED                       [ 80%]
tests/test_user_api.py::test_user_list PASSED                             [ 90%]
tests/test_user_api.py::test_user_create PASSED                           [100%]

----------- coverage: platform linux, python 3.9.6-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
fastapi_workshop/__init__.py              4      0   100%
fastapi_workshop/app.py                  16      1    94%
fastapi_workshop/cli.py                  21      0   100%
fastapi_workshop/config.py                5      0   100%
fastapi_workshop/db.py                   10      0   100%
fastapi_workshop/models/__init__.py       0      0   100%
fastapi_workshop/models/content.py       47      1    98%
fastapi_workshop/routes/__init__.py      11      0   100%
fastapi_workshop/routes/content.py       52     25    52%
fastapi_workshop/routes/security.py      15      1    93%
fastapi_workshop/routes/user.py          52     26    50%
fastapi_workshop/security.py            103     12    88%
-----------------------------------------------------
TOTAL                               336     66    80%


========================== 10 passed in 2.34s ==================================

```

## Linting and Formatting

```bash
make lint  # checks for linting errors
make fmt   # formats the code
```


## Configuration

This project uses [Dynaconf](https://dynaconf.com) to manage configuration.

```py
from fastapi_workshop.config import settings
```

## Acessing variables

```py
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Defining variables

### On files

settings.toml

```toml
[development]
dynaconf_merge = true

[development.db]
echo = true
```

> `dynaconf_merge` is a boolean that tells if the settings should be merged with the default settings defined in fastapi_workshop/default.toml.

### As environment variables
```bash
export PROJECT_NAME_KEY=value
export PROJECT_NAME_KEY="@int 42"
export PROJECT_NAME_KEY="@jinja {{ this.db.uri }}"
export PROJECT_NAME_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Secrets

There is a file `.secrets.toml` where your sensitive variables are stored,
that file must be ignored by git. (add that to .gitignore)

Or store your secrets in environment variables or a vault service, Dynaconf
can read those variables.

### Switching environments

```bash
PROJECT_NAME_ENV=production fastapi_workshop run
```

Read more on https://dynaconf.com

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
