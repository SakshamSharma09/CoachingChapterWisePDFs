#!/bin/bash
export PYTHONPATH="C:\Users\Saksham\AppData\Local\Temp\claude\C--Users-Saksham--claude-spares-spare-MGgmm5\d8405be3-342e-4ac3-9ee2-45b3cefd8089\scratchpad\libs"
cd "/d/Coaching Chapterwise PDFs/src/graded"
python run_graded.py $1 $2 Social_Science 2>&1 | grep -v "2 pages" | tail -15
