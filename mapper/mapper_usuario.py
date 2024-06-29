from dtos.novo_usuario_dto import NovoUsuarioDTO
from models.usuario_model import Usuario


class MapperUsuario():

        @classmethod
        def mapear_cadastrar_novo_usuario_dto(cls, dto: NovoUsuarioDTO) -> Usuario:
            return Usuario(
                nome=dto.nome,
                data_nascimento=dto.data_nascimento,
                email=dto.email,
                senha=dto.senha
                
            )

        # @classmethod
        # def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
        #     return Produto(
        #         id_produto= dto.id_produto,
        #         nome=dto.nome,
        #         valor=dto.valor,
        #         data_validade=dto.data_validade
        #     )