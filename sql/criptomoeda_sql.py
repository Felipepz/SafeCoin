SQL_CRIAR_TABELA_CRIPTOMOEDA = """
    CREATE TABLE IF NOT EXISTS criptomoeda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL,
        valor FLOAT NOT NULL,
        link_api TEXT NOT NULL,
        id_corretora INTEGER NOT NULL,
        FOREIGN KEY (id_corretora) REFERENCES corretora(id)
    )
"""

SQL_INSERIR_CRIPTOMOEDA = """
    INSERT INTO criptomoeda(nome, sigla, valor, link_api, id_corretora)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS_CRIPTOMOEDA = """
    SELECT id, nome, sigla, valor, link_api, id_corretora
    FROM criptomoeda
    ORDER BY nome
"""

SQL_ALTERAR_CRIPTOMOEDA = """
    UPDATE criptomoeda
    SET nome=?, sigla=?, valor=?, link_api=?, id_corretora=?
    WHERE id=?
"""

SQL_EXCLUIR_CRIPTOMOEDA = """
    DELETE FROM criptomoeda
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, sigla, valor, link_api, id_corretora
    FROM criptomoeda
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_CRIPTOMOEDA = """
    SELECT COUNT(*) FROM criptomoeda
"""

SQL_OBTER_BUSCA_CRIPTOMOEDA = """
    SELECT id, nome, sigla, valor, link_api, id_corretora
    FROM criptomoeda
    WHERE nome LIKE ? OR sigla LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_CRIPTOMOEDA = """
    SELECT COUNT(*) FROM criptomoeda
    WHERE nome LIKE ? OR sigla LIKE ?
"""