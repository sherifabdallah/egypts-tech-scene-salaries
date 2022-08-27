# Egypts tech scene salaries
Egypt's tech market is a bit vague. You can't access information regarding salaries, popular technologies, and companies' environment without finding yourself having to get in contact with employees working inside the company. Famous reviews websites like Glassdoor aren't much of a help since most employees don't disclose their salaries even anonymously and only angry employees decide to write reviews on Glassdoor.
This unintelligibility makes anyone who wants to value themselves in the market fail to do so. A lot of people often ask me: Which technologies should we learn to increase our chances in the market? Or how much should I ask for? And so on. While it's true that some companies are technology agnostic when it comes to hiring where they test you in your Problem Solving and Design skills, most companies, in Egypt, favour hiring someone who is already comfortable with their tech stack.


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


* Finally run The App:
```sh
(venv)$ python -m streamlit run main.py
```
* And navigate to `http://127.0.0.1:8501`.


## URL
* You can also navigate to the main website without needing to install python, you can navigate it from [here](https://share.streamlit.io/sherif-abdallah/egypt-high-schools-statistics/main/main.py)

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
