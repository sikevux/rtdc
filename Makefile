all:
	@echo "Not implemented yet, run with 'test' instead"

pylint:
	pylint --rcfile=.pylintrc rtdc

nosetests:
	nosetests -v --cover-erase --with-coverage --cover-min-percentage=85 \
		--cover-package=rtdc

test: pylint nosetests

clean:
	rm -rf *.pyc __pycache__
