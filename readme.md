# Real Time Currency Converter

In this project we are aiming to create currency convert system.
The page we are scraping updating data in every 60 seconds and this is best of both world.

I check it out Turkish Banking websites and they were also doing the same so I decided to x-rates.com

You can read about them more on this [link](https://www.x-rates.com/)

## Prerequisites

1. Python 3.7 or higher
2. Development IDE (VSCode or Pycharm is preferred)
3. Docker Engine (if you prefer to install with Docker)

## Installation without Docker

Open your terminal and write this code
```bash
git clone project_github_link
cd project_folder
```
Create a project environment for the Flask project
```bash
py -3 -m venv .venv
.venv\scripts\activate
```
Install required packages from requirements.txt
```bash
python -m pip install --upgrade pip
pip install requirements.txt
```
Running the application
```bash
python -m flask run
```
Our application will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Installation with Docker

Please open your terminal and write the following commands
```bash
docker build --tag python-docker .
docker run
```
After everything done, application will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)



## Screenshot from our application
![Currency Converter](docs/application_screenshot.PNG)

## Running tests

Please open your terminal and write the following commands
```bash
cd .\\tests\
pytest test_currency_scraper.py
```

## Footnotes

1. Tests are successfully passed on PyCharm but if you work with VSCODE, you need to use os.path instead of what we've already done. Currently VS Code have problem with importing from parent folder.
