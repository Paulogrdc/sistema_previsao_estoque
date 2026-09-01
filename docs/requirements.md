# Sistema de Previsão de Estoque

## Objetivo
Criar um sistema de previsão de estoque que vai conter 3 entidades, Produto, Vendas e Estoque. esse sistema precisa ser capaz de analisar quando o estoque de produtos estiver baixo e enivar um alerta. Recomendar a quantidade certa de compra e que seja capaz de Utilizar o histórico de vendas/movimentações posteriormente para fazer uma previsão de demanda. 

## Usuários

Adiministrador

## Requisitos Funcionais

- RF01 - Cadastrar produtos;
- RF02 - Consultar produtos; 
- RF03 - Registrar saídas de produtos; 
- RF04 - Consultar o estoque atual dos produtos;
- RF05 - Identificar produtos com estoque baixo;
- RF08 - Fazer um alerta para produtos com estoque baixo;
- RF09 - Calcular uma quantidade recomendada de compra dos produtos;
- RF10 - Registrar o histórico de movimentações;
- RF11 - Armazenar histórico de vendas;
- RF012 - Analisar o comportamento das vendas;
- RF013 - Utilizar o histórico de vendas/movimentações posteriormente para fazer uma previsão de demanda;

## Requisitos Não Funcionais

- RNF01 - Criar classe Produtos, vendas e Estoque  
- RNF02 - Registrar os Produdos no banco de dados Sql/postergre
- RNF03 - Registrada as movimentações de vendas no banco de dados Sql/postergre
- RNF04 - Registrar o Estoque do Produtos no banco de dados com Sql/postergre 
- RNF05 - Utilizar o numpy para calcular a quantidade de produdos a ser comprado


## Regras de Negócios

- RN01 - Quando for cadastrar um novo produto, só poder cadastrar ele se a quantidade for maior que 20
- RN02 - O tempo de resposta tem ser menor que 3 segundos
- RN03 - Um estoque é cosidarado baixo quando ele for menor ou igual a 30