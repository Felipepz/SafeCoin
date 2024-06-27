from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *


class NovoUsuarioDTO(BaseModel):
    nome: str
    data_nascimento: str
    email: str
    senha: str
    # confirmacao_senha: str

    @field_validator("data_nascimento")
    def validar_data_nascimento(cls, v):
        msg = is_not_empty(v, "Data de Nascimento")
        if not msg:
            msg = is_date_valid(v, "Data de Nascimento")
        if not msg:
            data_minima = date.today() - timedelta(days=125 * 365)
            data_v = datetime.strptime(v, "%Y-%m-%d").date()
            msg = is_date_between(
                data_v, "Data de Nascimento", data_minima, date.today()
            )
        if msg:
            raise ValueError(msg)
        return v


    @field_validator("email")
    def validar_email(cls, v):
        msg = is_email(v, "E-mail")
        if msg:
            raise ValueError(msg)
        return v

    @field_validator("senha")
    def validar_senha(cls, v):
        msg = is_not_empty(v, "Senha")
        if not msg:
            msg = is_password(v, "Senha")
        if msg:
            raise ValueError(msg.strip())
        return v

    # @field_validator("confirmacao_senha")
    # def validar_confirmacao_senha(cls, v, values):
    #     msg = is_not_empty(v, "Confirmação de Senha")
    #     if "senha" in values.data:
    #         msg = is_matching_fields(
    #             v, "Confirmação de Senha", values.data["senha"], "Senha"
    #         )
    #     else:
    #         msg = "Senha não informada."
    #     if msg:
    #         raise ValueError(msg)
    #     return v
