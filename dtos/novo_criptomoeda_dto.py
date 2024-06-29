from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *

class NovoCriptomoedaDTO(BaseModel):
    nome: str
    sigla: str
    valor: float
    link_api: str
    id_corretora: str
