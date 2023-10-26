#!/usr/bin/sh

rm dist/*
set -e
mv src/__cptest.py .
rm -rf src/cursesplus/__pycache__
python3 -m build
python3 -m twine upload dist/*
mv __cptest.py src