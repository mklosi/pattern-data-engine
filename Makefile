# Define the poetry export and build commands. The .PHONY target ensures
#   that the 'make' tool is not treating the other targets as files.
.PHONY: env_install env_update env_create test

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

test: env_install
	pytest -s tests/
