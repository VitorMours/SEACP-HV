import pytest
import importlib 
import inspect 
from fastapi import APIRouter 


class TestImageV1Router:
    def test_if_can_import_the_module(self) -> None:
        try:
            from app.api.v1 import image 
            assert  image is not None
        except ImportError:
            raise ImportError("Was not possible to find the image router module")

    def test_if_can_import_the_router_from_the_module(self) -> None:
        try:
            from app.api.v1.image import router 

            assert router is not None 
            assert isinstance(router, APIRouter)
            assert router.prefix == "/images"

        except ImportError:
            raise ImportError("Was not possible to find the image router module")

    def test_if_can_see_the_routes_in_the_router(self) -> None:
        module = importlib.import_module("app.api.v1.image")
        router = module.router 
        paths = set([route.path for route in router.routes])

        assert "/images/" in paths
        assert "/images/{image_id}" in paths
        assert "/images/process/{image_id}" in paths
        assert "/images/process/{image_id}/grayscale" in paths

    def test_if_prefix_base_path_have_correct_methods(self) -> None:
        pass
