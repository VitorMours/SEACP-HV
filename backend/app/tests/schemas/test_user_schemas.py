from pydantic import BaseModel 
import pytest
import importlib
import inspect 



class TestUserSchema:
    def test_if_can_import_user_schema_module(self) -> None:
        try:
            from app.schemas import user
            assert user is not None 
            
        except ImportError:
            raise ImportError("Was not possible to import the user schema module")

    def test_if_users_schema_module_have_correct_class(self) -> None:
        try:
            from app.schemas.user import UserCreate, UserUpdate, UserDelete, UserRead
            assert UserCreate is not None 
            assert inspect.isclass(UserCreate)
            assert UserUpdate is not None 
            assert inspect.isclass(UserUpdate)
            assert UserDelete is not None 
            assert inspect.isclass(UserDelete)
            assert UserRead is not None
            assert inspect.isclass(UserRead)
        except ImportError:
            raise ImportError("Was not possible to import one of the user schemas in the file")

    def test_if_user_schema_classes_have_correct_superclass(self) -> None:
        module = importlib.import_module("app.schemas.user")
        read_schema = module.UserRead
        assert issubclass(read_schema, BaseModel)
        create_schema = module.UserCreate 
        assert issubclass(create_schema, BaseModel)

    def test_if_user_read_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user")
        read_schema = module.UserRead 
        assert read_schema.model_fields["id"].annotation is int
        assert read_schema.model_fields["first_name"].annotation is str
        assert read_schema.model_fields["last_name"].annotation is str
        assert read_schema.model_fields["email"].annotation is str 
        
    def test_if_user_create_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user")
        create_schema = module.UserCreate
        assert create_schema.model_fields["first_name"].annotation is str 
        assert create_schema.model_fields["last_name"].annotation is str 
        assert create_schema.model_fields["email"].annotation is str 
        assert create_schema.model_fields["password"].annotation is str 
        
        
        
