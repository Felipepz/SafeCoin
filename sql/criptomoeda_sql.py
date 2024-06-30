SQL_CRIAR_TABELA_CRIPTOMOEDA = """
    CREATE TABLE IF NOT EXISTS criptomoeda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token_criptomoeda TEXT NOT NULL
    )
"""

SQL_INSERIR_CRIPTOMOEDA = """
    INSERT INTO criptomoeda(token_criptomoeda)
    VALUES (?)
"""

SQL_OBTER_TODOS_CRIPTOMOEDA = """
    SELECT id, token_criptomoeda
    FROM criptomoeda
    ORDER BY token_criptomoeda
"""

SQL_ALTERAR_CRIPTOMOEDA = """
    UPDATE criptomoeda
    SET token_criptomoeda=?
    WHERE id=?
"""

SQL_EXCLUIR_CRIPTOMOEDA = """
    DELETE FROM criptomoeda
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, token_criptomoeda
    FROM criptomoeda
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_CRIPTOMOEDA = """
    SELECT COUNT(*) FROM criptomoeda
"""

SQL_OBTER_BUSCA_CRIPTOMOEDA = """
    SELECT id, token_criptomoeda
    FROM criptomoeda
    WHERE token_criptomoeda LIKE ?
    ORDER BY token_criptomoeda
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_CRIPTOMOEDA = """
    SELECT COUNT(*) FROM criptomoeda
    WHERE token_criptomoeda LIKE ?
"""
