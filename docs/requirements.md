# Sistema de Previsão de Estoque

## Objetivo
Criar um sistema de previsão de estoque que vai ser capaz de analisar quando o estoque de produtos estiver baixo e enivar um alerta. ele vai Recomendar a quantidade certa de compra e Utilizar o histórico de vendas/movimentações posteriormente para fazer uma previsão de demanda. 

## Usuários

Adiministrador

## Requisitos Funcionais

- RF01 - Cadastrar produtos;
- RF02 - Consultar produtos; 
- RF03 — Registrar entradas de produtos;
- RF04 - Registrar saídas de produtos; 
- RF05 - Identificar produtos com estoque baixo;
- RF06 - Fazer um alerta para produtos com estoque baixo;
- RF07 - Registrar o histórico de movimentações;
- RF08 - Armazenar histórico de vendas;
- RF9 - Calcular a quantidade de produtos a ser comprada com base no comportamento de vendas.
- RF10 - Implementar previsão de demanda a partir do histórico de vendas/movimentações, para uso futuro no cálculo de reposição (RF09).

## Requisitos Não Funcionais

- RNF01 - O tempo de resposta das consultas tem que ser menor que 3 segundos
- RNF02 - só o administrador pode ver as movimentações
- RNF03 - backup 


## Regras de Negócios

- RN01 - Cada Produto terá o seu estoque minimo com base em analise de vendas
- RN02 - Só recomanda a comprar de um produto com base na previsão de estoque do mês seguinte
- RN03 - A saida de produto não tem que ser necessariamnete a venda de um produto
- RN04 - O sistema não deve permitir que o estoque fique negativo.

## Decisões Técnicas

- Python
- Programação Orientada a Objetos
- PostgreSQL