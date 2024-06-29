SQL_CRIAR_TABELA_CORRETORA = """
   CREATE TABLE IF NOT EXISTS corretora(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        pontuacao FLOAT NOT NULL
    ) 
"""

SQL_INSERIR_CORRETORA = """
    INSERT INTO corretora(nome, pontuacao)
    VALUES (?, ?)
"""

SQL_OBTER_TODOS_CORRETORA = """
    SELECT id, nome, pontuacao
    FROM corretora
    ORDER BY nome
"""

SQL_ALTERAR_CORRETORA = """
    UPDATE corretora
    SET nome=?, pontuacao=?
    WHERE id=?
"""

SQL_EXCLUIR_CORRETORA = """
    DELETE FROM corretora
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, pontuacao
    FROM corretora
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_CORRETORA = """
    SELECT COUNT(*) FROM corretora
"""

SQL_OBTER_BUSCA_CORRETORA = """
    SELECT id, nome, pontuacao
    FROM corretora
    WHERE nome LIKE ? OR pontuacao LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_CORRETORA = """
    SELECT COUNT(*) FROM corretora
    WHERE nome LIKE ? OR pontuacao LIKE ?
"""