## Testes Automatizados para o Projeto de Teste de Sistema - Especialização de Teste Ágeis

Este repositório contém uma série de testes automatizados desenvolvidos como parte do Projeto da Disciplina de Teste de Sistema para a Especialização de Teste Ágeis da CESAR School. Esses testes visam verificar a funcionalidade do sistema de banco implementado, garantindo que as diversas partes do sistema funcionem conforme o esperado.

## Sobre o Projeto

O projeto de teste de sistema foi desenvolvido como parte da Especialização de Teste Ágeis na CESAR School. O objetivo principal é criar testes automatizados para verificar a funcionalidade do sistema de banco, abrangendo várias funcionalidades, como a adição de clientes, abertura de contas, visualização de transações, depósitos e saques. Os testes são executados usando a biblioteca Selenium em conjunto com o framework de testes PyTest.

## Organização dos Testes

O projeto está organizado em vários arquivos de teste, cada um cobrindo diferentes partes da aplicação. Abaixo está uma visão geral dos arquivos de teste e das funcionalidades que eles abrangem:

- **Test001:** Testa a funcionalidade de adicionar um novo cliente e registrar suas informações.

- **Test002:** Testa a funcionalidade de abrir uma nova conta para um cliente, selecionando moeda e processando a abertura da conta.

- **Test003:** Testa a página de listagem de clientes, realizando uma pesquisa e verificando se os resultados são exibidos corretamente.

- **Test004:** Testa a funcionalidade de visualização de transações para um cliente específico, verificando se a lista de transações é exibida corretamente.

- **Test005:** Testa a funcionalidade de depósito na conta de um cliente, assegurando que os valores de depósito sejam processados corretamente.

- **Test006:** Testa a funcionalidade de saque da conta de um cliente, verificando se a transação de saque é bem-sucedida.

- **Test007:** Testa a funcionalidade de saque da conta de um cliente, garantindo que o saque falhe devido a saldo insuficiente.

## Como Executar os Testes

1. Certifique-se de ter o ambiente Python configurado em sua máquina.

2. Instale as dependências necessárias usando o gerenciador de pacotes pip:
   
   ```
   pip install -r requirements.txt
   ```

3. Execute os testes automatizados usando o PyTest:

   ```
   pytest
   ```

Isso iniciará a execução dos testes automatizados em sequência e fornecerá feedback sobre o status de cada teste.

## Considerações Finais

Esses testes automatizados desempenham um papel crucial na garantia da qualidade do sistema bancário, permitindo uma verificação contínua e eficaz das funcionalidades implementadas. Eles foram criados como parte do Projeto da Disciplina de Teste de Sistema para a Especialização de Teste Ágeis na CESAR School e representam um esforço para aplicar as práticas de teste ágeis aprendidas durante o curso.
