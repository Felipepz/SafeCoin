import sys
# Impedir a criação de arquivos .pyc
sys.dont_write_bytecode = True

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.administrador_repo import AdministradorRepo
from repositories.acao_repo import AcaoRepo
from repositories.corretora_repo import CorretoraRepo
from repositories.criptomoeda_repo import CriptomoedaRepo
from repositories.portfolio_repo import PortfolioRepo
from repositories.transacao_repo import TransacaoRepo
from repositories.usuario_repo import UsuarioRepo

from routes import  main_routes_safecoin

from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

AcaoRepo.criar_tabela()
AcaoRepo.inserir_acoes_json("sql/acoes.json")

AdministradorRepo.criar_tabela()
AdministradorRepo.inserir_administrador_json("sql/administradores.json")

CorretoraRepo.criar_tabela()
CorretoraRepo.inserir_corretora_json("sql/corretoras.json")

CriptomoedaRepo.criar_tabela()
CriptomoedaRepo.inserir_criptomoeda_json("sql/criptomoedas.json")

PortfolioRepo.criar_tabela()
PortfolioRepo.inserir_portfolio_json("sql/portfolios.json")

TransacaoRepo.criar_tabela()
TransacaoRepo.inserir_transacao_json("sql/transacoes.json")

UsuarioRepo.criar_tabela()
UsuarioRepo.inserir_usuario_json("sql/usuarios.json")


app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)

app.include_router(main_routes_safecoin.router)
