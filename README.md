# ⚡ SafeCoin.
SafeCoin é um portfólio onde os usuários podem registrar transações de compra e venda de ativos digitais. Ele serve como uma ferramenta eficaz para monitorar a oscilação dos preços, proporcionando um acompanhamento  e armazenamento seguro do histórico de investimentos.

**Objetivo:** Monitoramento de ativos digitais.

#### Personagens

- **Admin:** Responsável por cadastrar criptomoedas e administradores.
- **User:** Responsável por cadastrar carteiras e seu proprio perfil.

#### Tabelas

- **Corretoras:** Informações sobre as corretoras. / ID, Nome, Pontuação/ 
- **Criptomoedas:** Detalhes das criptomoedas./ ID, Nome, Sigla, Valor API, Corretora FK, Link API/ 
- **Moeda bancárias ou investimentos como bolsa de valores:** Dados de moedas tradicionais e investimentos. / ID, Nome, Sigla, Valor API, Corretora FK, Link API/ 
- **Administradores:** Dados dos administradores do sistema./ ID, Nome, Data Nascimento, CPF / 
- **Usuários:** Informações dos usuários. / ID, Nome, Data Nascimento/ 
- **Transações:** Transações./ ID, Ação, CriptoMoeda, Quantidade, Valor Atual, Data Ação/ 
- **Carteiras:** Detalhes das carteiras de criptomoedas./ ID, Nome, Transações FK, Usuario FK/  

#### Desafio

- **Cotação:** Obter a cotação das moedas por meio de uma API.

#### Referência

- [CoinMarketCap Portfolio Tracker](https://coinmarketcap.com/pt-br/portfolio-tracker/)

#### Dica para Instalar os Pacotes

- Execute o comando: `pip install -r requirements.txt`

#### API utilizada
- https://docs.coingecko.com/reference/introduction

#### Tecnologias Utilizadas

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Banco de Dados**: [SQLite](https://www.sqlite.org/index.html)
- **Frontend**: [Jinja](https://jinja.palletsprojects.com/), [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- **Controle de Versão e Hospedagem do Código**: [Git](https://git-scm.com/) e [GitHub](https://github.com/)
