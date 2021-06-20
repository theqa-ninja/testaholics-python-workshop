# Summary
This is an automation tutorial in the python language & using a framework built upon selenium that is called Pylenium (https://elsnoman.gitbook.io/pylenium/)

## Requirements
Python 3.7 or later

A python editor like [Visual Studio Code](https://
code.visualstudio.com/Download)

[Pylenium](https://docs.pylenium.io/getting-started/setup-pytest) installed

## Automation sections
1. Sign into a website
1. Check your user profile that you’re signed in as
1. Locate a specific event on the calendar
1. Write a comment on the calendar
1. Screenshot stuff
1. Make sure you get a pass/fail result



## Setup steps for Mac

### Initial setup
Inside the Mac terminal do these steps
1. check your python version to make sure it's 3.7+<br>
    `python --version`
1. install a python virtual environment
1. create your virtual environment
1. activate your virtual environment
```
pip install virtualenv
virtualenv (##place a directory path here##)
python3 -m venv (##place a directory path here##)
```
If this has been activated fine, you should see a (venv) at the front of your terminal line.<br>
If you need to get out of the virtual mode, just run

### Setting up Pyleniumio on the Mac

1. install pyleniumio
1. create a new pyleniumio folder
1. install pytest so you can run the tests afterwards!

```
pip install pyleniumio
pip install pytest
mkdir python-workshop
cd python-workshop
pylenium init
```

## Windows Setup

### Initial setup
Inside the Windows command prompt, run these steps
1. check your python version to make sure it's 3.7+<br>
    `python3 --version`
1. install a python virtual environment
1. create your virtual environment
1. activate your virtual environment
```
pip install virtualenv
python3 -m venv (##place the directory path here##)
cd (##place the directory path here##)
.\Scripts\activate
```
If this has been activated fine, you should see a (venv) at the front of your terminal line.<br>
If you need to get out of the virtual mode, just run

### Setting up Pyleniumio on Windows

1. install pyleniumio
1. create a new pyleniumio folder
1. install pytest so you can run the tests afterwards!

```
pip install pyleniumio
pip install pytest
mkdir python-workshop
cd python-workshop
pylenium init
```