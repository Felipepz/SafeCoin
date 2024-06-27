import sqlite3
from typing import List, Optional
from models.transacao_model import Transacao
from sql.transacao_sql import *
from util.database import obter_conexao


class TransacaoRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_TRANSACAO)

    @classmethod
    def inserir(cls, transacao: Transacao) -> Optional[Transacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_TRANSACAO,
                    (
                        transacao.id_criptomoeda,
                        transacao.id_acao,
                        transacao.id_usuario,
                        transacao.id_portfolio,
                        transacao.quantidade,
                        transacao.valor_unitario,
                        transacao.valor_total
                    )
                )
                if cursor.rowcount > 0:
                    transacao.id = cursor.lastrowid
                    return transacao
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> List[Transacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_TRANSACAO).fetchall()
                transacoes = [Transacao(*t) for t in tuplas]
                return transacoes
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, transacao: Transacao) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_TRANSACAO,
                    (
                        transacao.id_criptomoeda,
                        transacao.id_acao,
                        transacao.id_usuario,
                        transacao.id_portfolio,
                        transacao.quantidade,
                        transacao.valor_unitario,
                        transacao.valor_total,
                        transacao.id,
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
                cursor.execute(SQL_EXCLUIR_TRANSACAO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Transacao]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                transacao = Transacao(*tupla)
                return transacao
        except sqlite3.Error as ex:
            print(ex)
            return None