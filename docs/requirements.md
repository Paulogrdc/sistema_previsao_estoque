# Sistema de Previsão de Estoque

## Objetivo
Criar um sistema de previsão de estoque que vai ser capaz de analisar quando o estoque de produtos estiver baixo e enivar um alerta. ele vai Recomendar a quantidade certa de compra e Utilizar o histórico de vendas/movimentações posteriormente para fazer uma previsão de demanda. 

## Usuários

Adiministrador

## Requisitos Funcionais

- RF01 - Cadastrar produtos;
- RF02 - Consultar produtos; 
- RF03 — Registrar entradas de produtos.
- RF04 - Registrar saídas de produtos; 
- RF05 - Consultar o estoque atual dos produtos;
- RF06 - Identificar produtos com estoque baixo;
- RF07 - Fazer um alerta para produtos com estoque baixo;
- RF08 - Calcular uma quantidade recomendada de compra dos produtos;
- RF09 - Registrar o histórico de movimentações;
- RF10 - Armazenar histórico de vendas;
- RF011 - Analisar o comportamento das vendas;
- RF012 - Utilizar o histórico de vendas/movimentações posteriormente para fazer uma previsão de demanda;

## Requisitos Não Funcionais

- RNF01 - O tempo de resposta das consultas tem que ser menor que 3 segundos
- RNF02 - só o administrador pode ver as movimentações
- RNF03 - backup 


## Regras de Negócios

- RN01 - Cada Produto terá o seu estoque minimo
- RN02 - Só recomanda a comprar de novos produtos se o estoque estiver baixo
- RN03 - A saida de produto não tem que ser necessariamnete a venda de um produto
- RN04 - As saidas de Produtos(vendas/develução) tem que ser exportadas em uma planilha. 


## Decisões Técnicas

- Python
- Programação Orientada a Objetos
- PostgreSQL