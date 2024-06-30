from dtos.novo_administrador_dto import NovoAdministradorDTO
from models.administrador_model import Administrador


class MapperAdministrador():

    @classmethod
    def mapear_cadastrar_novo_administrador_dto(cls, dto: NovoAdministradorDTO) -> Administrador:
        return Administrador(
            nome=dto.nome,
            cpf=dto.cpf,
            data_nascimento=dto.data_nascimento,
            email=dto.email,
            senha= dto.senha
        )
    
    # @classmethod
    # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
    #     return Produto(
    #         id_produto= dto.id_produto,
    #         nome=dto.nome,
    #         valor=dto.valor,
    #         data_validade=dto.data_validade
    #     )