import json
import sqlite3
from typing import List, Optional
from models.administrador_model import Administrador
from sql.administrador_sql import *
from util.database import obter_conexao


class AdministradorRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_ADMINISTRADOR)

    @classmethod
    def inserir(cls, administrador: Administrador) -> Optional[Administrador]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_ADMINISTRADOR,
                    (
                        administrador.nome,
                        administrador.cpf,
                        administrador.data_nascimento,
                        administrador.email,
                        administrador.senha
                    )
                )
                if cursor.rowcount > 0:
                    administrador.id = cursor.lastrowid
                    return administrador
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def inserir_administrador_json(cls, arquivo_json: str):
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                administradores = json.load(arquivo)
                for administrador in administradores:
                    AdministradorRepo.inserir(Administrador(**administrador ))

    @classmethod
    def obter_todos(cls) -> List[Administrador]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_ADMINISTRADOR).fetchall()
                administradores = [Administrador(*t) for t in tuplas]
                return administradores
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, administrador: Administrador) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_ADMINISTRADOR,
                    (
                        administrador.nome,
                        administrador.cpf,
                        administrador.data_nascimento,
                        administrador.email,
                        administrador.senha,
                        administrador.id
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
                cursor.execute(SQL_EXCLUIR_ADMINISTRADOR, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Administrador]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                administrador = Administrador(*tupla)
                return administrador
        except sqlite3.Error as ex:
            print(ex)
            return None