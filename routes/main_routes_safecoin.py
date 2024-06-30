import math
from sqlite3 import DatabaseError
from fastapi import APIRouter, Body, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from dtos.entrar_dto import EntrarDTO
from dtos.novo_administrador_dto import NovoAdministradorDTO
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
    
# EXEMPLO DE ROTA PARA CADASTRAR (ROTA POST)
@router.post("/cadastrar_administrador")
async def post_administrador(administrador: NovoAdministradorDTO):
    print(administrador)
    # FUNCAO EM QUE O MAPPER E O DTO DEVE ESTAR CORRETORA
    administrador_mapeado = MapperAdministrador.mapear_cadastrar_novo_administrador_dto(administrador)
    # INSERE O DTO MAPEADO NO BANCO DE DADOS, VERIFCAR SQL SE NECESSÁRIO
    administrador_inserido = CorretoraRepo.inserir(administrador_mapeado)
    return {"MSG": administrador_inserido.id}
    
@router.get("/cadastro_corretora")
async def get_cadastro_corretora(request: Request):
    return templates.TemplateResponse(
        "cadastro_corretora.html",
        {"request": request},
    )
    
# EXEMPLO DE ROTA PARA CADASTRAR (ROTA POST)
@router.post("/cadastrar_corretora")
async def post_corretora(corretora: NovoCorretoraDTO):
    print(corretora)
    # FUNCAO EM QUE O MAPPER E O DTO DEVE ESTAR CORRETORA
    corretora_mapeado = MapperCorretora.mapear_cadastrar_novo_corretora_dto(corretora)
    # INSERE O DTO MAPEADO NO BANCO DE DADOS, VERIFCAR SQL SE NECESSÁRIO
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