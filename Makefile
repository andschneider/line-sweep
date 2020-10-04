PYTHON=python

help:
	@cat Makefile

test-solution:
	$(PYTHON) -m pytest tests/functional/test_run.py -vs

tests:
	$(PYTHON) -m pytest tests/ -vs

.PHONY: help test-solution tests
