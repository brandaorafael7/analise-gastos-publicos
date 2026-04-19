# Análise de Despesas e Viagens Governamentais (2023 - 2026)

Este repositório contém uma análise técnica sobre os gastos públicos da administração federal brasileira, com foco em passagens aéreas e diárias de servidores. O projeto processa dados de transações para identificar padrões de consumo, destinos frequentes e médias salariais por categoria funcional.

## 📌 Sobre o Projeto
O objetivo principal é transformar dados brutos de pagamentos governamentais em insights compreensíveis, permitindo visualizar como o orçamento de viagens é distribuído entre diferentes órgãos e cargos.

## 📊 Estrutura dos Dados
O projeto utiliza três bases de dados principais localizadas na raiz do repositório:
- **`2026_Pagamento.csv`**: Detalhamento individualizado de processos de pagamento, incluindo Unidades Gestoras (UG) e tipos de despesa (Diárias, Passagens, Restituições).
- **`tabela_2023.xlsx`**: Dados consolidados referentes ao ano de 2023 para análise histórica.
- **`tabela_2026.xlsx`**: Dados projetados ou processados para o ano de 2026.

## 🔍 Insights Extraídos
A análise exploratória permitiu identificar:
* **Concentração de Destinos:** Brasília/DF como o principal polo de destino das viagens a serviço.
* **Custo por Cargo:** Identificação da despesa média para cargos como "Professor do Magistério" (aprox. R$ 2.031,22 por viagem) e "Auditor-Fiscal".
* **Fluxo de Pagamentos:** Diferenciação entre despesas urgentes e planejadas através dos códigos de processo.

## 🛠️ Tecnologias e Ferramentas
* **Data Cleaning:** Manipulação de arquivos CSV e XLSX para tratamento de valores nulos e padronização de categorias.
* **Análise de Dados:** Organização de tabelas dinâmicas e cálculos de média/soma por órgão superior.
* **Documentação:** Markdown para apresentação do projeto.

## 🚀 Como Executar
1. Instale as dependências: `pip install pandas openpyxl`
2. Execute o script de análise: `python analise_gastos.py`

---
Este projeto faz parte do meu portfólio de **Desenvolvimento de Software e Análise de Dados**, demonstrando competências em tratamento de dados governamentais e organização de informações estruturadas.
