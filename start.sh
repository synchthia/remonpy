#!/usr/bin/env python3

cd "$(dirname $0)"

export REMONPI_VENDOR="mitsubishi"
export REMONPI_MODEL="kgsa3-c"
export TEMPLATE_DIR="$PWD/public"

if [ "$1" = "" ]; then
    python3 $PWD/entrypoint.py
elif [ "$1" = "build" ]; then
    $PWD/dist/entrypoint
fi
