SQL_CRIAR_TABELA_USUARIO = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento DATE NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        token TEXT
    )
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario(nome, data_nascimento, email, senha)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_TODOS_USUARIO = """
    SELECT id, nome, data_nascimento, email
    FROM usuario
    ORDER BY nome
"""

SQL_ALTERAR_USUARIO = """
    UPDATE usuario
    SET nome=?, data_nascimento=?, email=?, senha=?
    WHERE id=?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, data_nascimento, email
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_USUARIO = """
    SELECT COUNT(*) FROM usuario
"""

SQL_OBTER_BUSCA_USUARIO = """
    SELECT id, nome, data_nascimento, email
    FROM usuario
    WHERE nome LIKE ? OR email LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_USUARIO = """
    SELECT COUNT(*) FROM usuario
    WHERE nome LIKE ? OR email LIKE ?
"""