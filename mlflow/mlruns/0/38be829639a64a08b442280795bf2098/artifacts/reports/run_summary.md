# Resumo da run

## Contexto

Projeto: risco de crédito 
Objetivo da run: baseline com tracking manual enriquecido 
Modelo: Regressão Logística 
Target: inadimplente

## Dados

- Amostras totais: 6000
- Treino: 4500
- Teste: 1500
- Features: 8
- Dataset version: synthetic_credit_v1

## Principais métricas

- ROC-AUC teste: 0.9036
- ROC-AUC CV média: 0.9045
- ROC-AUC CV desvio: 0.0128
- Precision inadimplente: 0.3890
- Recall inadimplente: 0.8232
- F1 inadimplente: 0.5284

## Leitura inicial

O modelo funciona como baseline rastreável. 
A ROC-AUC indica boa capacidade de ordenação dos casos por risco. 
A análise de precision e recall da classe inadimplente deve ser usada para discutir trade-offs de negócio em aulas futuras.