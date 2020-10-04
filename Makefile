PYTHON=python

help:
	@cat Makefile

test-solution:
	$(PYTHON) -m pytest tests/functional/test_run.py -vs

tests:
	$(PYTHON) -m pytest tests/ -vs

plots:
	$(PYTHON) plots.py

format:
	black *.py tests/

.PHONY: help test-solution tests plots format

