format:
	isort .
	black .

test:
	tox -e py39

test_all:
	tox
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile.alpine
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile.debian
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile.python-alpine
	docker run --rm --interactive --volume "${PWD}"/.hadolint.yaml:/.hadolint.yaml hadolint/hadolint <Dockerfile.python-slim
