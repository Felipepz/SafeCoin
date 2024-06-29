SQL_CRIAR_TABELA_ACAO = """
    CREATE TABLE IF NOT EXISTS acao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
"""

SQL_INSERIR_ACAO = """
    INSERT INTO acao(nome)
    VALUES (?)
"""

SQL_OBTER_TODOS_ACAO = """
    SELECT id, nome
    FROM acao
    ORDER BY nome
"""

SQL_ALTERAR_ACAO = """
    UPDATE acao
    SET nome=?
    WHERE id=?
"""

SQL_EXCLUIR_ACAO = """
    DELETE FROM acao
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome
    FROM acao
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_ACAO = """
    SELECT COUNT(*) FROM acao
"""

SQL_OBTER_BUSCA_ACAO = """
    SELECT id, nome
    FROM acao
    WHERE nome LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_ACAO = """
    SELECT COUNT(*) FROM acao
    WHERE nome LIKE ?
"""