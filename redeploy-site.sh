#!/bin/bash

tmux kill-session -t portfolio
cd flask-portfolio
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
clear
tmux new -d -s  portfolio
tmux send -t portfolio "flask run --host=0.0.0.0" ENTER
cd


