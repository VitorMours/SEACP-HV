from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.testclient import TestClient
import importlib

import inspect


class TestAuthRouter:
    def __init__(self, app: FastAPI) -> None:
        self.app = app
        self.client = TestClient(app)

    def test_if_can_import_auth_route_module(self) -> None:
        try:
            from app.api.v1 import auth
            assert auth is not None
        except ImportError:
            raise ImportError("Was not possible ot import the auth route module")

    def test_if_can_import_auth_router_from_module(self) -> None:
        try:
            from app.api.v1.auth import router
            assert router is not None
            assert isinstance(router, APIRouter)

        except ImportError:
            raise ImportError("Was not possible to import the auth router")

    def test_if_auth_router_have_token_generator_route(self) -> None:
        response = self.client.get("/token")
        assert response.status_code == 200
        assert response.json()["email"] == "Credencial de acesso do usuario"
        assert response.json()["password"] == "Senha do usuario"

    def test_if_auth_router_post_token_router_verify_token(self) -> None:
        pass
