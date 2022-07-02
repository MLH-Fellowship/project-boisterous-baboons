#!/bin/bash

source python3-virtualenv/bin/activate
#pip install typing_extensions urllib
python -m unittest discover -v tests
