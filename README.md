# Egypts tech scene salaries
Egypt's tech market is a bit vague. You can't access information regarding salaries, popular technologies, and companies' environment without finding yourself having to get in contact with employees working inside the company.

## Table of Content
- [Egypts tech scene salaries](#egypts-tech-scene-salaries)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [URL](#URL)
  * [Author](#author)

## Tools
1. Python
2. Streamlit
3. Pandas
4. Google Sheets
5. Google Forms


## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/egypts-tech-scene-salaries egypts-tech-scene-salaries
```

* Install Python 3.8 venv, pip and compiler
```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd egypts-tech-scene-salaries
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.


* Finally run The Software
```sh
(venv)$ python -m streamlit run main.py
```
## URL
* You can also navigate to the main website without needing to install python, you can navigate it from [here](https://share.streamlit.io/sherif-abdallah/egypt-high-schools-statistics/main/main.py)

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
