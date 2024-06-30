from dtos.novo_portfolio_dto import NovoPortfolioDTO
from models.portfolio_model import Portfolio


class MapperPortfolio():

        @classmethod
        def mapear_cadastrar_novo_portfolio_dto(cls, dto: NovoPortfolioDTO) -> Portfolio:
            return Portfolio(
                nome=dto.nome,
                id_usuario=dto.id_usuario
            )
        
        # @classmethod
        # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
        #     return Produto(
        #         id_produto= dto.id_produto,
        #         nome=dto.nome,
        #         valor=dto.valor,
        #         data_validade=dto.data_validade
        #     )