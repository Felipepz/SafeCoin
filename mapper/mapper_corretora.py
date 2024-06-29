from dtos.novo_corretora_dto import NovoCorretoraDTO
from models.corretora_model import Corretora


class MapperCorretora():

        @classmethod
        def mapear_cadastrar_novo_corretora_dto(cls, dto: NovoCorretoraDTO) -> Corretora:
            return Corretora(
                nome=dto.nome,
                pontuacao=dto.pontuacao
            )
        
        # @classmethod
        # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
        #     return Produto(
        #         id_produto= dto.id_produto,
        #         nome=dto.nome,
        #         valor=dto.valor,
        #         data_validade=dto.data_validade
        #     )