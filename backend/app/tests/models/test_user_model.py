import importlib
import inspect
import pytest
from sqlmodel import SQLModel

class TestUserModel:
    def test_if_can_import_user_model_module(self) -> None:
        try:
            from app.models import user
            assert user is not None

        except ImportError:
            raise ImportError("Was not possible to import the user model")

    def test_if_can_import_the_user_data_from_the_module(self) -> None:
        try:
            from app.models.user import User
            assert User is not None
            assert inspect.isclass(User)
        except ImportError:
            raise ImportError("Was not possible to import the user model in the file")

    def test_if_user_model_have_correct_superclass(self) -> None:
        module = importlib.import_module("app.models.user")
        class_ = module.User
        assert issubclass(class_, SQLModel)

    def test_if_user_model_have_correct_fields(self) -> None:
        fields_list = ("id","first_name","last_name","email","password")
        module = importlib.import_module("app.models.user")
        class_ = module.User
        assert inspect.isclass(class_)
        field_names = [name for name, _ in inspect.getmembers(class_)]
        for field in fields_list:
            assert field in field_names

    def test_if_user_model_fields_have_correct_datatype(self) -> None:
        module = importlib.import_module("app.models.user")


