#!/bin/sh

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH/Dedicated/"
guix shell -C -N -u user --share=../wine=/home/user/.wine -f ../wine-old.scm xvfb-run coreutils -- ./run.sh
