## help: Show this help.
.PHONY: help
help: Makefile
	@sed -n 's/^##\s//p' $<

## install: Install non-dev requirements.
.PHONY: install-req
install-req:
	@pip install -U -r requirements.txt

## install: Install dev requirements.
.PHONY: install-dev-req
install-dev-req:
	@pip install -U -r requirements-dev.txt

## install: Install all requirements.
.PHONY: install
install: install-req install-dev-req

## lint: Run linter
.PHONY: lint
lint:
	@flake8
	@isort --check .
	@black --check .

## test: Run tests and prepare coverage
.PHONY: test
test:
	@coverage run --source=src/ --module pytest -v test/

## cov-report: Display coverage report
.PHONY: cov-report
cov-report:
	@coverage report --precision=2 --fail-under=$(coverage_perc) --sort=Cover

## cov-html: Display code coverage in browser
.PHONY: cov-html
cov-html:
	@coverage html --precision=2 --fail-under=$(coverage_perc); x-www-browser htmlcov/index.html

## test-cov-report: Run tests and show code coverage report.
.PHONY: test-cov-report
test-cov-report: test cov-report

## test-cov-html: Run tests and display code coverage in browser.
.PHONY: test-cov-html
test-cov-html: test cov-html

## clean: Delete autogenerated files.
.PHONY: clean
clean:
	@-python3 -Bc "for p in __import__('pathlib').Path('.').rglob('*.py[co]'): p.unlink()"
	@-python3 -Bc "for p in __import__('pathlib').Path('.').rglob('__pycache__'): p.rmdir()"
	@-rm -rf .pytest_cache
	@-rm -rf htmlcov
	@-rm .coverage