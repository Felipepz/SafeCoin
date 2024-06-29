import json
import sqlite3
from typing import List, Optional
from models.corretora_model import Corretora
from sql.corretora_sql import *
from util.database import obter_conexao


class CorretoraRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_CORRETORA)

    @classmethod
    def inserir(cls, corretora: Corretora) -> Optional[Corretora]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_CORRETORA,
                    (
                        corretora.nome,
                        corretora.pontuacao,
                    )
                )
                if cursor.rowcount > 0:
                    corretora.id = cursor.lastrowid
                    return corretora
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    
    
    @classmethod
    def obter_quantidade_corretora(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE_CORRETORA).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_corretora_json(cls, arquivo_json: str):
        if  CorretoraRepo.obter_quantidade_corretora() == 0:
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                corretora = json.load(arquivo)
                for corretora in corretora:
                    CorretoraRepo.inserir(Corretora(**corretora ))
                    
    @classmethod
    def obter_todos(cls) -> List[Corretora]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_CORRETORA).fetchall()
                corretoras = [Corretora(*t) for t in tuplas]
                return corretoras
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, corretora: Corretora) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_CORRETORA,
                    (
                        corretora.nome,
                        corretora.pontuacao,
                        corretora.id,
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
                cursor.execute(SQL_EXCLUIR_CORRETORA, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Corretora]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                corretora = Corretora(*tupla)
                return corretora
        except sqlite3.Error as ex:
            print(ex)
            return None