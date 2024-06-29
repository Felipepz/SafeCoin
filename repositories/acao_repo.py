import sqlite3
from typing import List, Optional
from models.acao_model import Acao
from sql.acao_sql import *
from util.database import obter_conexao


class AcaoRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_ACAO)

    @classmethod
    def inserir(cls, acao: Acao) -> Optional[Acao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_ACAO,
                    (
                        acao.nome,
                    )
                )
                if cursor.rowcount > 0:
                    acao.id = cursor.lastrowid
                    return acao
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> List[Acao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_ACAO).fetchall()
                acoes = [Acao(*t) for t in tuplas]
                return acoes
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, acao: Acao) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_ACAO,
                    (
                        acao.nome,
                        acao.id,
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
                cursor.execute(SQL_EXCLUIR_ACAO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Acao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                acao = Acao(*tupla)
                return acao
        except sqlite3.Error as ex:
            print(ex)
            return None