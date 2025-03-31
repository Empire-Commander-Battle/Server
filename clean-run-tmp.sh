#!/bin/sh

set -xe

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH"

if [ -d run-tmp ]; then
	chown -R $USER:$USER run-tmp/
	chmod -R u+rwx run-tmp/
	rm -rf run-tmp/
fi
