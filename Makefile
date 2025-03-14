.PHONY: run-api run-streamlit install activate run-backend format lint lint-format bump-patch bump-minor bump-major

# Automatically set PYTHONPATH to the project root
export PYTHONPATH := $(shell pwd)

# Virtual environment activation
VENV := venv/bin/activate

# Ensure the virtual environment is activated
activate:
	@source $(VENV)

# Install dependencies from requirements.txt
install:
	@source $(VENV) && pip install -r requirements.txt

# Run Streamlit app with PYTHONPATH set automatically
run-streamlit:
	@export PYTHONPATH=$(PYTHONPATH) && source $(VENV) && streamlit run frontend/app.py

# Run FastAPI backend (optional)
run-backend:
	@export PYTHONPATH=$(PYTHONPATH) && source $(VENV) && uvicorn backend.main:app --reload

# Format code using Ruff (similar to Black)
format:
	@source $(VENV) && ruff format .

# Lint code and automatically fix issues
lint:
	@source $(VENV) && ruff check . --fix

# Run both formatting and linting
lint-format: format lint

# Version bumping
bump-patch:
	bumpversion patch

bump-minor:
	bumpversion minor

bump-major:
	bumpversion major