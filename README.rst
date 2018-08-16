===============================
Space Weather Service
===============================


Tracking >= 10 MeV levels.

At the command line::

$ pip3 install -r requirements.txt
$ python3 run.py

If tkinter isn't installed for python3::

$ sudo apt-get install python3-tk


Development
-----------


Test and development requirements in requirements/dev.txt
Tests and fixtures in tests/test*.py

To test::

$ pip3 install -r requirements/dev.txt
$ flake8
$ python3 -m pytest -sv


Features
--------


* Parses NOAA GOES electron flux forecast
* Doesn't do anything with it yet! :)
