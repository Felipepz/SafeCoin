SQL_CRIAR_TABELA_TRANSACAO = """
    CREATE TABLE IF NOT EXISTS transacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_criptomoeda INTEGER NOT NULL,
        id_acao INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        id_portfolio INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_unitario FLOAT NOT NULL,
        valor_total FLOAT AS (valor_unitario * quantidade),
        FOREIGN KEY (id_criptomoeda) REFERENCES criptomoeda(id),
        FOREIGN KEY (id_acao) REFERENCES acao(id),
        FOREIGN KEY (id_usuario) REFERENCES usuario(id),
        FOREIGN KEY (id_portfolio) REFERENCES portfolio(id),
        # FOREIGN KEY (valor_unitario) REFERENCES criptomoeda(valor)
    )
"""

SQL_INSERIR_TRANSACAO = """
    INSERT INTO transacao(id_criptomoeda, id_acao, id_usuario, id_portfolio, quantidade, valor_unitario)
    VALUES (?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS_TRANSACAO = """
    SELECT id, id_criptomoeda, id_acao, id_usuario, id_portfolio, quantidade, valor_unitario, valor_total
    FROM transacao
    ORDER BY id
"""

SQL_ALTERAR_TRANSACAO = """
    UPDATE transacao
    SET id_criptomoeda=?, id_acao=?, id_usuario=?, id_portfolio=?, quantidade=?, valor_unitario=?
    WHERE id=?
"""

SQL_EXCLUIR_TRANSACAO = """
    DELETE FROM transacao
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, id_criptomoeda, id_acao, id_usuario, id_portfolio, quantidade, valor_unitario, valor_total
    FROM transacao
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_TRANSACAO = """
    SELECT COUNT(*) FROM transacao
"""

SQL_OBTER_BUSCA_TRANSACAO = """
    SELECT id, id_criptomoeda, id_acao, id_usuario, id_portfolio, quantidade, valor_unitario, valor_total
    FROM transacao
    WHERE id_criptomoeda LIKE ? OR id_acao LIKE ?
    ORDER BY id
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA_TRANSACAO = """
    SELECT COUNT(*) FROM transacao
    WHERE id_criptomoeda LIKE ? OR id_acao LIKE ?
"""
