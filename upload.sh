#!/usr/bin/sh

rm dist/*
set -e
rm -rf src/cursesplus/__pycache__
mv src/__cptest.py .
python3 -m build
python3 -m twine upload dist/*
mv __cptest.py src