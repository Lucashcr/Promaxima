# Desafio Promaxima

José está precisando monitorar os preços de referência dos medicamentos de sua farmácia e precisa de um sistema onde ele consiga realizar consultas desses preços por descrição. Você foi designado para ajudar José e abaixo estão algumas informações e requisitos para que o sistema funcione como se espera.

## Fonte de dados

- [PMVG](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos) 
- [Arquivo XLS](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos/arquivos/xls_conformidade_gov_20230602_031318591.xls/@@download/file)

## Tecnologias a serem utilizadas:

- Frontend
- Vue ou Nuxt
- Backend
- Django Rest Framework
- Banco de dados
- Postgres

## Requisitos:

1. O sistema deve possuir uma tela de busca que retorna resultados pelo termo digitado podendo filtrar por:

    - PRINCÍPIO ATIVO
    - CNPJ
    - LABORATÓRIO
    - CÓDIGO GGREM
    - REGISTRO EAN
    - PRODUTO
    - APRESENTAÇÃO
    - CLASSE TERAPÊUTICA
    - TIPO DE PRODUTO (STATUS DO PRODUTO)
    - REGIME DE PREÇO
    - RESTRIÇÃO HOSPITALAR
    - CAP
    - CONFAZ 87
    - ICMS 0%
    - LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFIN
    - COMERCIALIZAÇÃO 2022
    - TARJA

2. Os registros encontrados devem ser listados

3. Cada resultado deve possuir um detalhamento com as informações
disponíveis incluindo:

    - PF Sem Impostos
    - PF 0%
    - PF 12%
    - PF 17%
    - PF 17% ALC
    - PF 17,5%
    - PF 17,5% ALC
    - PF 18%
    - PF 18% ALC
    - PF 19%
    - PF 20%
    - PF 21%
    - PF 22%
    - PMVG Sem Impostos
    - PMVG 0%
    - PMVG 12%
    - PMVG 17%
    - PMVG 17% ALC
    - PMVG 17,5%
    - PMVG 17,5% ALC
    - PMVG 18%
    - PMVG 18% ALC
    - PMVG 19%
    - PMVG 20%
    - PMVG 21%
    - PMVG 22%

4. Os resultados exibidos devem possuir um checkbox para serem selecionados e exportados em xls. 

## O que será avaliado?

1. O projeto está de acordo com as especificações?
2. Como está a estrutura do projeto?
3. O projeto está versionado no github/gitlab com todo o código
disponível?
4. O projeto está documentado?
    - Instruções de como executar
    - Links
    - Observações
    - Restrições
5. O projeto está utilizando docker?
6. Como está o design do frontend? 