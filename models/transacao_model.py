from dataclasses import dataclass
from typing import Optional

@dataclass
class Transacao:
    id: Optional[int] = None
    id_criptomoeda: Optional[int] = None
    id_acao: Optional[int] = None
    id_usuario: Optional[int] = None
    id_portfolio: Optional[int] = None
    quantidade: Optional[int] = None
    valor_unitario: Optional[float] = None
    valor_total: Optional[float] = None