#!/bin/bash

source venv/bin/activate
python -m unittest discover -v tests
