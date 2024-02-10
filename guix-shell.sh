#!/bin/sh
guix shell -N -C -W -E XDG_RUNTIME_DIR -E PS1 -E SSH_AUTH_SOCK -E DISPLAY --share=/tmp/.X11-unix --expose=$HOME/.Xauthority --share=$HOME/.gnupg --share=$XDG_RUNTIME_DIR/gnupg --share=$SSH_AUTH_SOCK --expose=$HOME/.ssh/config --expose=$HOME/.ssh/known_hosts --expose=$HOME/.ssh/keys/ --expose=$HOME/.bashrc --expose=$HOME/.gitconfig --expose=/etc/bashrc -m manifest.scm -- bash
