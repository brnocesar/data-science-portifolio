import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

RANDOM_STATE = 42
NUM_COLS     = ["idade", "renda_mensal", "tempo_emprego_anos", "score_interno", "valor_solicitado", "num_parcelas"]
CAT_COLS     = ["tipo_renda", "possui_restricao"]


def generate_credit_risk_base(n_amostras: int = 5000, random_state: int = RANDOM_STATE) -> pd.DataFrame:
    
    rng                = np.random.default_rng(random_state)
    n                  = n_amostras
    idade              = rng.integers(22, 66, size=n)
    renda_mensal       = rng.lognormal(mean=np.log(3500), sigma=0.45, size=n).round(2)
    tempo_emprego_anos = rng.exponential(scale=4, size=n).clip(0, 35).round(1)
    score_interno      = rng.normal(650, 90, size=n).clip(300, 900).astype(int)
    valor_solicitado   = rng.lognormal(mean=np.log(8000), sigma=0.6, size=n).round(2)
    num_parcelas       = rng.choice([6, 12, 18, 24, 36, 48], size=n, p=[0.1, 0.25, 0.2, 0.2, 0.15, 0.1])
    tipo_renda         = rng.choice(["CLT", "autonomo", "aposentado"], size=n, p=[0.65, 0.22, 0.13])
    possui_restricao   = rng.choice(["sim", "nao"], size=n, p=[0.12, 0.88])

    # probabilidade base de default (logit simplificado)
    z            = (-3.2 
                    - 0.025   * (score_interno - 650)
                    - 0.00008 * renda_mensal
                    + 0.00002 * valor_solicitado
                    + 0.015   * (num_parcelas / 12)
                    - 0.04    * tempo_emprego_anos)
    z            = np.asarray(z, dtype=float)
    z           += np.where(possui_restricao == "sim", 0.85, 0)
    z           += np.where(tipo_renda == "autonomo", 0.35, 0)
    z           += rng.normal(0, 0.35, size=n)
    p_default    = 1 / (1 + np.exp(-z))
    inadimplente = rng.binomial(1, p_default)

    return pd.DataFrame(
        {
            "idade":              idade,
            "renda_mensal":       renda_mensal,
            "tempo_emprego_anos": tempo_emprego_anos,
            "score_interno":      score_interno,
            "valor_solicitado":   valor_solicitado,
            "num_parcelas":       num_parcelas,
            "tipo_renda":         tipo_renda,
            "possui_restricao":   possui_restricao,
            "inadimplente":       inadimplente,
        }
    )


def data_preprocess(num_cols:list[str]=NUM_COLS, cat_cols:list[str]=CAT_COLS) -> ColumnTransformer:
    numeric_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")), # imputa valores faltantes com a mediana
            ("scaler", StandardScaler()),                  # reescala variaveis: padroniza as colunas para terem media 0 e desvio padrao 1
        ]
    )

    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")), # imputa valores faltantes com a moda
            ("onehot", OneHotEncoder(handle_unknown="ignore")),   # converte variaveis categoricas em variaveis dummy (0 ou 1), criando uma coluna para cada categoria
        ]
    )

    # combina os pipelines de variaveis numericas e categoricas em um unico pipeline
    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, num_cols),
            ("cat", categorical_pipe, cat_cols),
        ]
    )


def profile_for_test_prediction() -> pd.DataFrame:
    return pd.DataFrame([
        {
            "idade":              34,
            "renda_mensal":       4200.0,
            "tempo_emprego_anos": 5.0,
            "score_interno":      620,
            "valor_solicitado":   12000.0,
            "num_parcelas":       24,
            "tipo_renda":         "CLT",
            "possui_restricao":   "nao",
        }
    ])
