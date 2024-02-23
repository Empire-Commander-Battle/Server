#!/bin/sh

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH/Dedicated/"
guix time-machine -C '../channels.scm' -- shell -C -N -u user --share=../wine=/home/user/.wine -f ../wine-old.scm xvfb-run coreutils -- ./run.sh
