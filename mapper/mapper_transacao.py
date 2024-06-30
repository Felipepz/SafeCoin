from dtos.novo_transacao_dto import NovoTransacaoDTO
from models.transacao_model import Transacao


class MapperTransacao():

        @classmethod
        def mapear_cadastrar_novo_transacao_dto(cls, dto: NovoTransacaoDTO) -> Transacao:
            return Transacao(
                id_criptomoeda=dto.id_criptomoeda,
                id_acao=dto.id_acao,
                id_usuario=dto.id_usuario,
                id_portfolio=dto.id_portfolio,
                quantidade=dto.quantidade,
                valor_unitario=dto.valor_unitario,
                valor_total=dto.valor_total

            )
        
        # @classmethod
        # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
        #     return Produto(
        #         id_produto= dto.id_produto,
        #         nome=dto.nome,
        #         valor=dto.valor,
        #         data_validade=dto.data_validade
        #     )