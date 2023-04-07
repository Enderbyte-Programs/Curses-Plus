del /S /Q dist\*
py -m build
py -m twine upload dist/*