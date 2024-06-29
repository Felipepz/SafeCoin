import json
import sqlite3
from typing import List, Optional
from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.database import obter_conexao


class UsuarioRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA_USUARIO)

    @classmethod
    def inserir(cls, usuario: Usuario) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_USUARIO,
                    (
                        usuario.nome,
                        usuario.data_nascimento,
                        usuario.email,
                        usuario.senha
                    )
                )
                if cursor.rowcount > 0:
                    usuario.id = cursor.lastrowid
                    return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_usuario_json(cls, arquivo_json: str):
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
                for usuario in usuarios:
                    UsuarioRepo.inserir(Usuario(**usuario ))
                    
    @classmethod
    def obter_todos(cls) -> List[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS_USUARIO).fetchall()
                usuarios = [Usuario(*t) for t in tuplas]
                return usuarios
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, usuario: Usuario) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_USUARIO,
                    (
                        usuario.nome,
                        usuario.data_nascimento,
                        usuario.email,
                        usuario.senha,
                        usuario.id,
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
                cursor.execute(SQL_EXCLUIR_USUARIO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                usuario = Usuario(*tupla)
                return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None