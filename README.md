# Summary
This is an automation tutorial in the python language & using a framework built upon selenium that is called Pylenium (https://elsnoman.gitbook.io/pylenium/)

## Requirements
Python 3.7 or later

A python editor like [Visual Studio Code](https://code.visualstudio.com/Download)

[Pylenium](https://docs.pylenium.io/getting-started/setup-pytest) installed

## Automation steps
1. go to the best search engine
1. search for `wikipedia`
1. go to the wikipedia result
1. click on the search bar
1. begin typing `quality as`
1. let auto-complete run and select the first result (`software assurance`)
1. on the page, locate a hyperlink to `software testing`
1. verify the URL you are on



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
source (##place a directory path here##)/bin/activate
```
If this has been activated fine, you should see a (##directory_name##) at the front of your terminal line.<br>
If you need to get out of the virtual mode, just run `deactivate`

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
    if it's not, please grab it from [Python](https://www.python.org/downloads/) or via the [Windows Store](https://www.microsoft.com/store/productId/9NJ46SX7X90P)
1. make sure pip is installed
    `pip --version`
    if it's not, pelase install [pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)
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
