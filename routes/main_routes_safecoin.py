import math
from sqlite3 import DatabaseError
from fastapi import APIRouter, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from dtos.entrar_dto import EntrarDTO
from util.html import ler_html
from dtos.novo_cliente_dto import NovoClienteDTO
from models.cliente_model import Cliente
from repositories.cliente_repo import ClienteRepo
from repositories.produto_repo import ProdutoRepo
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
    
@router.get("/cadastro_criptomoeda")
async def get_cadastro_criptomoeda(request: Request):
    return templates.TemplateResponse(
        "cadastro_corretora.html",
        {"request": request},
    )
    
@router.get("/cadastro_transacao")
async def get_cadastro_transacao(request: Request):
    return templates.TemplateResponse(
        "cadastro_transacao.html",
        {"request": request},
    )