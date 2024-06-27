from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

from util.validators import *

class NovoPortfolioDTO(BaseModel):
    nome: str
    id_usuario: int