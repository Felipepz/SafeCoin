from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *

class NovoTransacaoDTO(BaseModel):
    id_criptomoeda: int
    id_acao: int
    id_usuario: int
    id_portfolio: int
    quantidade: int
    valor_unitario: float
    valor_total: float