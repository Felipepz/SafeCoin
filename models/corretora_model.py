from dataclasses import dataclass
from typing import Optional

@dataclass
class Corretora:
    id: Optional[int] = None
    nome: Optional[str] = None
    pontuacao: Optional[float] = None