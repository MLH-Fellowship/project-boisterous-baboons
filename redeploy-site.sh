#!/bin/bash


git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
clear
systemctl restart myportfolio



