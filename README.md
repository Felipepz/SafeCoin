# ⚡ SafeCoin.
SafeCoin é um portfólio onde os usuários podem registrar transações de compra e venda de ativos digitais. Ele serve como uma ferramenta eficaz para monitorar a oscilação dos preços, proporcionando um acompanhamento  e armazenamento seguro do histórico de investimentos.

**Objetivo:** Monitoramento de ativos digitais.

#### Personagens

- **Admin:** Responsável por cadastrar criptomoedas.
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

#### Pendências do 1° Ciclo

1. **Preparar os Ambientes:** Configurar o ambiente de desenvolvimento.
2. **Criar as Branches:** Estabelecer branches no controle de versão.
3. **Criar as Tabelas:** Definir e criar as tabelas no banco de dados.
4. **Dividir o Trabalho:** Distribuir tarefas entre os membros da equipe.

#### Pendências do 2° Ciclo

1. **Criar Inserts:** Desenvolver scripts de inserção de dados.
2. **Entrega da Tela HTML Base:** Finalizar e entregar a estrutura básica da tela HTML.
3. **Definir o Padrão para o HTML:** Estabelecer normas e padrões para o desenvolvimento HTML.
4. **Iniciar o Backend:** Começar o desenvolvimento da lógica de backend.
5. **Iniciar as Telas HTML:** Começar a criação das telas HTML.