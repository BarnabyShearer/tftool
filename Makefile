format:
	isort .
	black .

test:
	tox -e py39

test_all:
	tox
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile
