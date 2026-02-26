import pytest 
import importlib 
import inspect 
from fastapi import APIRouter



class TestUserV1Route:
    def test_if_can_import_the_users_route_modules(self) -> None:
        try:
            from api.v1 import user
            assert user is not None 
            
        except ImportError:
            raise ImportError("Was not possible to import the user route module")

    def test_if_user_routesmodule_have_router(self) -> None:
        try:
            from api.v1.user import router
            assert router is not None 
            
        except ImportError:
            raise ImportError("Was not possible to import the router object from the user route module")

    def test_if_user_route_module_router_its_the_correct_object(self) -> None:
        module = importlib.import_module("api.v1.user")
        router_ = module.router 
        assert type(router_) == APIRouter


