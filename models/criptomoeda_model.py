from dataclasses import dataclass
from typing import Optional

@dataclass
class Criptomoeda:
    id: Optional[int] = None
    token_criptomoeda: Optional[str] = None