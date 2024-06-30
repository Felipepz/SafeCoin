from dtos.novo_criptomoeda_dto import NovoCriptomoedaDTO
from models.criptomoeda_model import Criptomoeda


class MapperCriptomoeda():

        @classmethod
        def mapear_cadastrar_novo_criptomoeda_dto(cls, dto: NovoCriptomoedaDTO) -> Criptomoeda:
            return Criptomoeda(
                token_criptomoeda=Criptomoeda.token_criptomoeda
            )
        
        # @classmethod
        # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
        #     return Produto(
        #         id_produto= dto.id_produto,
        #         nome=dto.nome,
        #         valor=dto.valor,
        #         data_validade=dto.data_validade
        #     )