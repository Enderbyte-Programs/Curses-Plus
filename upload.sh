#!/usr/bin/sh

rm dist/*
set -e
python3 -m build
python3 -m twine upload dist/*
