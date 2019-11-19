# resourceresidency.com

Resource Residency is an organization connecting a global network of artists to donated resoureces.

-----

## Installation

```shell
# download repo
git clone [this repo] resourceresidency.com

# set up virtual environment
python -m venv resourceresidency.com/

# install dependencies
cd resourceresidency.com
pip install -r requirements.txt
```

## Versions

* Django 2.1.4
* Python 3.6.3

## Usage

```shell
# navigate into the project root
# cd resourceresidency.com

# activate the virtual environment
source ./venv/bin/activate # mac/ linux
source ./venv/Scripts/activate # windows

# migrate the database tables
python manage.py migrate

# build front end application
# from project root
cd app
yarn
yarn run serve

# start the development server
# from project root
python manage.py runserver
```
