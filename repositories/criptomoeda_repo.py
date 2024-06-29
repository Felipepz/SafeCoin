import json
import sqlite3
from typing import List, Optional
from models.criptomoeda_model import Criptomoeda
from sql.criptomoeda_sql import *
from util.database import obter_conexao


class CriptomoedaRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_CRIPTOMOEDA)

    @classmethod
    def inserir(cls, criptomoeda: Criptomoeda) -> Optional[Criptomoeda]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_CRIPTOMOEDA,
                    (
                        criptomoeda.nome,
                        criptomoeda.sigla,
                        criptomoeda.valor,
                        criptomoeda.link_api,
                        criptomoeda.id_corretora,
                    )
                )
                if cursor.rowcount > 0:
                    criptomoeda.id = cursor.lastrowid
                    return criptomoeda
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    
    @classmethod
    def obter_quantidade_criptomoeda(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE_CRIPTOMOEDA).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_criptomoeda_json(cls, arquivo_json: str):
        if  CriptomoedaRepo.obter_quantidade_criptomoeda() == 0:
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                criptomoeda = json.load(arquivo)
                for criptomoeda in criptomoeda:
                    CriptomoedaRepo.inserir(Criptomoeda(**criptomoeda ))

    @classmethod
    def obter_todos(cls) -> List[Criptomoeda]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_CRIPTOMOEDA).fetchall()
                criptomoedas = [Criptomoeda(*t) for t in tuplas]
                return criptomoedas
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, criptomoeda: Criptomoeda) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_CRIPTOMOEDA,
                    (
                        criptomoeda.nome,
                        criptomoeda.sigla,
                        criptomoeda.valor,
                        criptomoeda.link_api,
                        criptomoeda.id_corretora,
                        criptomoeda.id,
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
                cursor.execute(SQL_EXCLUIR_CRIPTOMOEDA, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Criptomoeda]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                criptomoeda = Criptomoeda(*tupla)
                return criptomoeda
        except sqlite3.Error as ex:
            print(ex)
            return None