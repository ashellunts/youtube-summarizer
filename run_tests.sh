find . -name "*.py" -or -path "*.txt" | entr -c python -m pytest -x $@
