#!/bin/sh

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH/Source/Sourcecode/mm dev - MS/"
guix time-machine -C '../../../channels.scm' -- shell -C -W --share="$SCRIPT_PATH" -m '../../../manifest.scm' -- ./build_module.sh
