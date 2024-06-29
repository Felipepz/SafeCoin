from dataclasses import dataclass
from typing import Optional

@dataclass
class Criptomoeda:
    id: Optional[int] = None
    nome: Optional[str] = None
    sigla: Optional[str] = None
    valor: Optional[float] = None
    link_api: Optional[str] = None
    id_corretora: Optional[int] = None