# Define the Python interpreter and Poetry command
PYTHON := poetry run python
POETRY := poetry run
HOOK_TYPE_ARN := arn:aws:cloudformation:ap-southeast-1:706041656585:type/hook/MyCompany-Testing-MyTestHook

# Define directories to be checked/formatted
SRC_DIR := src

# Run Unit tests
test:
	@echo "Running tests..."
	$(POETRY) pytest $(SRC_DIR)

# Run Black formatter
format:
	@echo "Running Black..."
	$(POETRY) black $(SRC_DIR)

# Run Flake8 linter
lint:
	@echo "Running Flake8..."
	$(POETRY) flake8 $(SRC_DIR)

# Run both Black and Flake8
check: format lint

# Clean up unnecessary files
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -exec rm -f {} +

register-dry-run:
	cfn submit --dry-run

register:
	cfn submit --set-default

verify-hooks:
	aws cloudformation list-types

# Help command to list all available commands
help:
	@echo "Available make commands:"
	@echo "  make format   - Run Black to format code"
	@echo "  make lint     - Run Flake8 to lint code"
	@echo "  make check    - Run both Black and Flake8"
	@echo "  make clean    - Clean up __pycache__ and .pyc files"
