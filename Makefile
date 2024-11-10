# &&& all of this needs revamp.
# Define the Docker image name and version tag
BASE_NAME=wmt-martin-klosi-file-metadata
IMAGE_NAME=$(BASE_NAME)
IMAGE_TAG=0.0.1
FULL_IMAGE_NAME=$(IMAGE_NAME):$(IMAGE_TAG)
CONTAINER_NAME=$(BASE_NAME)-container

# Define the poetry export and build commands. The .PHONY target ensures
#   that the 'make' tool is not treating the other targets as files.
.PHONY: env_install env_update env_create docker_reqs docker_build docker_run test

# Install python dependencies from an already generated lock file.
env_install:
	poetry install --sync

# Generate a new lock file (resolve dependencies) and install them.
env_update:
	poetry lock
	$(MAKE) env_install

# Create a new poetry env.
env_create:
	poetry env use python3
	$(MAKE) env_update

# Export requirements.txt for the server docker image using poetry.
docker_reqs:
	poetry install --sync
	poetry export --without-hashes --format=requirements.txt > server/requirements.txt

# Build the Docker image
docker_build: docker_reqs
	docker build -t $(FULL_IMAGE_NAME) .

# Run a Docker container
docker_run:
	@docker stop $(CONTAINER_NAME) > /dev/null || true
	@docker rm $(CONTAINER_NAME) > /dev/null || true
	docker run --name $(CONTAINER_NAME) -p 4000:4000 $(FULL_IMAGE_NAME)

test: env_install
	pytest -s tests/

client_run:
	python client/client.py
