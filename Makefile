all:
	@echo "Not implemented yet, run with 'test' instead"

pylint:
	pylint --rcfile=.pylintrc rtdc

nosetests:
	nosetests -v --with-coverage --cover-min-percentage=90 \
        --cover-package=rtdc

test: pylint nosetests

clean:
	rm -rf *.pyc __pycache__
