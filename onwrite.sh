#! /bin/bash
FILENAME="nchess.py"
function file_change {
    inotifywait -q -e modify $FILENAME
}
function runscript {
    date
    python $FILENAME
}
runscript
while true; do
    file_change
    runscript
done
