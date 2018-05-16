.PHONY: test integration-tests

test: integration-tests

integration-tests:
	PYTHONWARNINGS=ignore:ResourceWarning python -m unittest \
		discover --start-directory tests/integration --top-level-directory . --verbose
