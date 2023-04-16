find . -name "*.py" -or -name "*.html" | entr -c ./run_tests.sh $@
