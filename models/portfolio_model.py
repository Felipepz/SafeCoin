from dataclasses import dataclass
from typing import Optional

@dataclass
class Portfolio:
    id: Optional[int] = None
    nome: Optional[str] = None
    id_usuario: Optional[int] = None