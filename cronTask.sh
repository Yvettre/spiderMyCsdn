#!/bin/bash
# usage: ./cronTask.sh
# change 'ding_yanfang@outlook.com' to any email adress

python main.py
cat result/output.csv | mail -s 'Today your Csdn Blog gift' ding_yanfang@outlook.com
