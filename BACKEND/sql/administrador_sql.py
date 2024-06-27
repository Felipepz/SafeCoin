SQL_CRIAR_TABELA_ADMINISTRADOR = """
    CREATE TABLE IF NOT EXISTS administrador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento DATE NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        token TEXT
    )
"""

SQL_INSERIR_ADMINISTRADOR = """
    INSERT INTO administrador(nome, cpf, data_nascimento, email, senha)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS_ADMINISTRADOR = """
    SELECT id, nome, cpf, data_nascimento, email
    FROM administrador
    ORDER BY nome
"""

SQL_ALTERAR_ADMINISTRADOR = """
    UPDATE administrador
    SET nome=?, cpf=?, data_nascimento=?, email=?, senha=?
    WHERE id=?
"""

SQL_EXCLUIR_ADMINISTRADOR = """
    DELETE FROM administrador
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, cpf, data_nascimento, email
    FROM administrador
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_ADMINISTRADOR = """
    SELECT COUNT(*) FROM administrador
"""

SQL_OBTER_BUSCA_ADMINISTRADOR = """
    SELECT id, nome, cpf, data_nascimento, email
    FROM administrador
    WHERE nome LIKE ? OR email LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_ADMINISTRADOR = """
    SELECT COUNT(*) FROM administrador
    WHERE nome LIKE ? OR email LIKE ?
"""
