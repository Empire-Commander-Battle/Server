#!/bin/sh

set -e

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd "$SCRIPT_PATH"

if [ ! -d run-tmp ]; then
	set -x
	mkdir run-tmp

	ARTIFACT=$(guix time-machine -C 'channels.scm' -- pack -RR -S /bin=bin -m run-manifest.scm)

	tar xf $ARTIFACT -C run-tmp

	set +x
fi

bwrap --clearenv --bind $PWD/run-tmp / --bind $PWD/Dedicated /Dedicated --bind $PWD/wine /wine --dev /dev --proc /proc --tmpfs /tmp --unshare-all --share-net --setenv WINEPREFIX /wine --setenv HOME / --chdir /Dedicated ./run.sh
