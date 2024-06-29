SQL_CRIAR_TABELA_PORTFOLIO = """
    CREATE TABLE IF NOT EXISTS portfolio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_usuario INTEGER NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES usuario(id)
    )
"""

SQL_INSERIR_PORTFOLIO = """
    INSERT INTO portfolio(nome, id_usuario)
    VALUES (?, ?)
"""

SQL_OBTER_TODOS_PORTFOLIO = """
    SELECT id, nome, id_usuario
    FROM portfolio
    ORDER BY nome
"""

SQL_ALTERAR_PORTFOLIO = """
    UPDATE portfolio
    SET nome=?, id_usuario=?
    WHERE id=?
"""

SQL_EXCLUIR_PORTFOLIO = """
    DELETE FROM portfolio
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, id_usuario
    FROM portfolio
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_PORTFOLIO = """
    SELECT COUNT(*) FROM portfolio
"""

SQL_OBTER_BUSCA_PORTFOLIO = """
    SELECT id, nome, id_usuario
    FROM portfolio
    WHERE nome LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_PORTFOLIO = """
    SELECT COUNT(*) FROM portfolio
    WHERE nome LIKE ?
"""