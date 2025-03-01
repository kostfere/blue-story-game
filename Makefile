.PHONY: run-api run-streamlit

run-api:
	@echo "Starting FastAPI backend..."
	uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

run-streamlit:
	@echo "Starting Streamlit app..."
	streamlit run frontend/app.py

bump-patch:
	bumpversion patch

bump-minor:
	bumpversion minor

bump-major:
	bumpversion major