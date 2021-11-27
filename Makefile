format:
	isort .
	black .

test:
	tox -e py39
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile

test_all:
	tox
