#!/bin/bash

source python3-virtualenv/bin/activate
python -m unittest discover -v tests
