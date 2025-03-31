#!/bin/sh

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH"

if [ ! -f INIT.txt ]; then
	make
fi

xvfb-run wine mb_warband_wse2_dedicated.exe --config-path server_config.ini -r INIT.txt --module Napoleonic Wars
