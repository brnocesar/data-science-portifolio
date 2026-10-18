# MLFlow — Risco de Crédito

Este projeto demonstra o uso do **MLflow na construção e gestão de um pipeline de machine learning**, cobrindo o rastreamento de experimentos, a comparação e seleção de modelos, o registro e versionamento, o acompanhamento de artefatos e a execução reproduzível de etapas de avaliação e inferência. A classificação de risco de crédito serve como cenário para ilustrar esse fluxo de ponta a ponta e os recursos do MLflow ao longo do ciclo de vida do modelo.

## Estrutura do repositório

```text
mlflow_risk_credit/
├── mlartifacts/
├── notebooks/
│   ├── 1_pipeline_risco_credito_mlflow.ipynb
│   ├── 2_run_manual_log_tags_artifacts.ipynb
│   ├── 3_auto_log_models_comparison.ipynb
│   ├── 4_champion_model.ipynb
│   └── 5_mlflow_model.ipynb
├── src/
│   └── support_module.py
├── .gitignore
├── mlflow_registry.db
├── README.md
└── requirements.txt
```

## Classificação de Risco de Crédito

O objetivo é prever se um cliente será **inadimplente** (`inadimplente = 1`) ou **adimplente** (`inadimplente = 0`) com base em variáveis financeiras e cadastrais.

### Dataset

O dataset é **sintético**, gerado por regras de negócio simuladas em `generate_credit_risk_base()`.

| Variável | Tipo | Descrição |
| :-: | :-: | :- |
| `idade` | numérica | Idade do solicitante |
| `renda_mensal` | numérica | Renda mensal em reais |
| `tempo_emprego_anos` | numérica | Tempo de emprego |
| `score_interno` | numérica | Score de crédito interno (300–900) |
| `valor_solicitado` | numérica | Valor do empréstimo solicitado |
| `num_parcelas` | numérica | Número de parcelas |
| `tipo_renda` | categórica | CLT, autônomo, servidor público, aposentado |
| `possui_restricao` | categórica | sim / não |
| **`inadimplente`** | **target** | 0 = adimplente, 1 = inadimplente |

### Modelos avaliados

Todos os modelos usam um pipeline scikit-learn com pré-processamento compartilhado:

- **Numéricas:** imputação pela mediana + `StandardScaler`
- **Categóricas:** imputação pela moda + `OneHotEncoder`

| Algoritmo | Identificador |
|---|---|
| Regressão Logística | `logistic_regression` |
| Árvore de Decisão | `decision_tree` |
| Random Forest | `random_forest` |

**Métricas de negócio priorizadas:** ROC-AUC, _recall_ e _precision_ da classe inadimplente, com trade-off explícito entre capturar inadimplentes (_recall_) e evitar falsos positivos (_precision_).
