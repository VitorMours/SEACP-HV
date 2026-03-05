# Variáveis
VENV = backend/.venv
PYTHON = $(VENV)/Scripts/python   # Windows
# PYTHON = $(VENV)/bin/python     # Linux/Mac
PIP = $(PYTHON) -m pip
APP = app
CELERY_APP = app.workers.celery_app

.PHONY: help install run worker redis test test-cov lint format clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make install     - Cria venv e instala dependências"
	@echo "  make run         - Sobe o servidor FastAPI"
	@echo "  make worker      - Sobe o worker Celery"
	@echo "  make redis       - Sobe o Redis via Docker"
	@echo "  make test        - Roda os testes"
	@echo "  make test-cov    - Testes com cobertura"
	@echo "  make clean       - Remove arquivos temporários"

install:
	cd backend && python -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r backend/requirements.txt

run:
	cd backend && $(PYTHON) -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

worker:
	cd backend && $(PYTHON) -m celery -A $(CELERY_APP) worker --loglevel=info

redis:
	docker run -d -p 6379:6379 --name redis redis:alpine || docker start redis

test:
	cd backend && $(PYTHON) -m pytest tests/ -v

test-cov:
	cd backend && $(PYTHON) -m pytest tests/ -v --cov=$(APP) --cov-report=term-missing

test-fast:
	cd backend && $(PYTHON) -m pytest tests/ -v -x

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -name "*.pyc" -delete