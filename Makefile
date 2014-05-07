all:
	@echo "Not implemented yet, run with 'test' instead"

pylint:
	pylint --rcfile=.pylintrc rtdc

nosetests:
	nosetests -v --with-coverage --cover-min-percentage=90

test: pylint nosetests

clean:
	rm -f *.pyc
