.PHONY: test integration-tests scale-tests

ifndef TRAVIS_BRANCH
$(error Please set environment variable TRAVIS_BRANCH before running make commands)
endif

test: integration-tests

integration-tests:
	PYTHONWARNINGS=ignore:ResourceWarning python -m unittest \
		discover --start-directory tests/integration --top-level-directory . --verbose

scale-tests:
	PYTHONWARNINGS=ignore:ResourceWarning python -m unittest \
		discover --start-directory tests/scale --top-level-directory . --verbose
