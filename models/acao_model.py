from dataclasses import dataclass
from typing import Optional

@dataclass
class Acao:
    id: Optional[int] = None
    nome: Optional[str] = None