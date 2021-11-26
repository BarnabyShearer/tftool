target "docker-metadata-action" {
  context = "./"
  platforms = [
    "linux/amd64",
    "linux/arm64"
  ]
}

group "default" {
  targets = ["python", "python-slim", "python-alpine", "alpine", "debian"]
}

target "python" {
  inherits = ["docker-metadata-action"]
  dockerfile = "Dockerfile"
}

target "python-slim" {
  inherits = ["docker-metadata-action"]
  dockerfile = "Dockerfile.python-slim"
}

target "python-alpine" {
  inherits = ["docker-metadata-action"]
  dockerfile = "Dockerfile.python-alpine"
}

target "alpine" {
  inherits = ["docker-metadata-action"]
  dockerfile = "Dockerfile.alpine"
}

target "debian" {
  inherits = ["docker-metadata-action"]
  dockerfile = "Dockerfile.debian"
}
