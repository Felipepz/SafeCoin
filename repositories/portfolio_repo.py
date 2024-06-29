import sqlite3
from typing import List, Optional
from models.portfolio_model import Portfolio
from sql.portfolio_sql import *
from util.database import obter_conexao


class PortfolioRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_PORTFOLIO)

    @classmethod
    def inserir(cls, portfolio: Portfolio) -> Optional[Portfolio]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_PORTFOLIO,
                    (
                        portfolio.nome,
                        portfolio.id_usuario,
                    )
                )
                if cursor.rowcount > 0:
                    portfolio.id = cursor.lastrowid
                    return portfolio
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> List[Portfolio]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_PORTFOLIO).fetchall()
                portfolios = [Portfolio(*t) for t in tuplas]
                return portfolios
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, portfolio: Portfolio) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_PORTFOLIO,
                    (
                        portfolio.nome,
                        portfolio.id_usuario,
                        portfolio.id,
                    )
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR_PORTFOLIO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Portfolio]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                portfolio = Portfolio(*tupla)
                return portfolio
        except sqlite3.Error as ex:
            print(ex)
            return None