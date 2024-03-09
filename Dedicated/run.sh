#!/bin/sh

if [ ! -f INIT.txt ]; then
	make
fi

wine mb_warband_wse2_dedicated.exe --config-path server_config.ini -r INIT.txt --module Napoleonic Wars
