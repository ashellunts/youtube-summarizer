export PYTHONDONTWRITEBYTECODE=1
find . -name "*.py" -or -path "*.txt" | entr -c python -m pytest -x -p no:cacheprovider $@ tests
