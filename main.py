import sys
import os
import shutil

# Impedir a criação de arquivos .pyc
sys.dont_write_bytecode = True

# Função para excluir todos os diretórios __pycache__
def remove_pycache_dirs(path="."):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
                print(f"Removed {os.path.join(root, dir)}")

# Chamar a função para remover os diretórios __pycache__ no início do script
remove_pycache_dirs()

from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.cliente_repo import ClienteRepo
from repositories.item_pedido_repo import ItemPedidoRepo
from repositories.pedido_repo import PedidoRepo
from repositories.produto_repo import ProdutoRepo
from routes import main_routes, cliente_routes, main_routes_safecoin
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

ProdutoRepo.criar_tabela()
ProdutoRepo.inserir_produtos_json("sql/produtos.json")
ClienteRepo.criar_tabela()
ClienteRepo.inserir_clientes_json("sql/clientes.json")
PedidoRepo.criar_tabela()
ItemPedidoRepo.criar_tabela()

app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(cliente_routes.router)
app.include_router(main_routes_safecoin.router)
