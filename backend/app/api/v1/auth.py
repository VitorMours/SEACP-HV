from fastapi import APIRouter


router = APIRouter(prefix="auth", tags=["Auth"])

@router.get("/token")
async def get_login_parameters_field():
    return {
        "email":"Credencial de acesso do usuario",
        "password":"Senha do usuario"
    }

@router.post("/token")
async def generate_jwt_token():
    pass


@router.post("/token/verify")
async def verify_jwt_token():
    pass