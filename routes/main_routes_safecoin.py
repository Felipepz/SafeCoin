import math
from sqlite3 import DatabaseError
from fastapi import APIRouter, Body, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from dtos.entrar_dto import EntrarDTO
from dtos.novo_corretora_dto import NovoCorretoraDTO
from mapper.mapper_corretora import MapperCorretora
from repositories.corretora_repo import CorretoraRepo
from util.html import ler_html

from util.auth import (
    conferir_senha,
    gerar_token,
    obter_hash_senha,
)

from util.cookies import adicionar_cookie_auth, adicionar_mensagem_sucesso
from util.pydantic import create_validation_errors
from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("html_safecoin")


@router.get("/")
async def get_dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request},
    )

@router.get("/transacoes")
async def get_transacoes(request: Request):
    return templates.TemplateResponse(
        "transacoes.html",
        {"request": request},
    )

@router.get("/portfolio")
async def get_portfolio(request: Request):
    return templates.TemplateResponse(
        "portfolio.html",
        {"request": request},
    )
    
@router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request},
    )
    
@router.get("/dashboard")
async def get_dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request},
    )
    
@router.get("/cadastro_usuario")
async def get_cadastro_usuario(request: Request):
    return templates.TemplateResponse(
        "cadastro_usuario.html",
        {"request": request},
    )

@router.get("/cadastro_administrador")
async def get_cadastro_administrador(request: Request):
    return templates.TemplateResponse(
        "cadastro_administrador.html",
        {"request": request},
    )
    
@router.get("/cadastro_corretora")
async def get_cadastro_corretora(request: Request):
    return templates.TemplateResponse(
        "cadastro_corretora.html",
        {"request": request},
    )
    
@router.post("/cadastrar_corretora")
async def post_corretora(corretora: NovoCorretoraDTO):
    print(corretora)
    corretora_mapeado = MapperCorretora.mapear_cadastrar_novo_corretora_dto(corretora)
    corretora_inserido = CorretoraRepo.inserir(corretora_mapeado)
    return {"MSG": corretora_inserido.id}


@router.get("/cadastro_criptomoeda")
async def get_cadastro_criptomoeda(request: Request):
    return templates.TemplateResponse(
        "cadastro_criptomoeda.html",
        {"request": request},
    )
    
@router.get("/cadastro_transacao")
async def get_cadastro_transacao(request: Request):
    return templates.TemplateResponse(
        "cadastro_transacao.html",
        {"request": request},
    )