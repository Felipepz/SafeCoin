from pydantic import BaseModel, field_validator
from datetime import date, datetime, timedelta

# from util.validators import *

class NovoCorretoraDTO(BaseModel):
    nome: str
    pontuacao: float