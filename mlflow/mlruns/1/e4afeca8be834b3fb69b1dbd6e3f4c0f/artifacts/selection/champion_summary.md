# Seleção do modelo campeão

## Contexto

Projeto: risco de crédito 
Tarefa: classificação binária 
Target: inadimplente 
Dataset version: synthetic_credit_v1 
Feature set: core_features_v1 

## Modelo selecionado

- Modelo: logistic_regression
- Run name: hibrid_log_comparison_logistic_regression
- Run ID: e4afeca8be834b3fb69b1dbd6e3f4c0f

## Principais métricas

- ROC-AUC teste: 0.9036
- ROC-AUC CV média: 0.9023
- ROC-AUC CV desvio: 0.0011
- Precision inadimplente: 0.3890
- Recall inadimplente: 0.8232
- F1 inadimplente: 0.5284

## Critérios de decisão

A seleção considerou desempenho técnico, estabilidade, interpretabilidade e simplicidade operacional.

Pesos técnicos:
- ROC-AUC teste: 35%
- Recall inadimplente: 25%
- Precision inadimplente: 15%
- F1 inadimplente: 15%
- Estabilidade: 10%

Score final:
- Score técnico: 75%
- Interpretabilidade: 15%
- Simplicidade operacional: 10%

## Justificativa

O modelo selecionado apresentou o melhor equilíbrio entre desempenho e critérios operacionais dentro da política de seleção definida.

## Próximo passo

Preparar este modelo para registro no MLflow Model Registry.
