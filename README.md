# fraud-detection-copilot

# Sistema de Detección de Fraude

Sistema simple de detección de fraude usando árboles de decisión y agentes AI con CrewAI.

## Características

- **Modelo**: Árbol de decisión con scikit-learn
- **Agentes AI**: CrewAI para análisis, triage, enriquecimiento, agrupación, playbooks y reportes
- **API**: FastAPI para endpoints REST
- **Análisis**: Jupyter notebooks para exploración de datos

## Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar variable de entorno para OpenAI:
```bash
export OPENAI_API_KEY="tu_api_key_aqui"
```

## Uso

### Entrenar modelo
```bash
python train_model.py
```

### Ejecutar API
```bash
python src/api.py
```

### Análisis en Jupyter
```bash
jupyter notebook notebooks/fraud_analysis.ipynb
```

## Estructura del Proyecto

```
fraud-detection-copilot/
├── src/
│   ├── models.py          # Modelo de árbol de decisión
│   ├── api.py            # API FastAPI
│   ├── config.py         # Configuración
│   ├── utils.py          # Utilidades
│   └── agents/           # Agentes CrewAI
│       ├── auditor.py    # Agente auditor
│       ├── triage.py     # Agente de triage
│       ├── enrichment.py # Agente de enriquecimiento
│       ├── grouping.py   # Agente de agrupación
│       ├── playbook.py   # Agente de playbooks
│       └── writer.py     # Agente escritor
├── notebooks/
│   └── fraud_analysis.ipynb  # Análisis exploratorio
├── data/
│   └── Fraud.csv         # Dataset de fraude
├── models/               # Modelos entrenados
├── train_model.py       # Script de entrenamiento
└── requirements.txt     # Dependencias
```

## Endpoints de la API

- `GET /` - Información de la API
- `POST /predict` - Predecir fraude en una transacción
- `POST /analyze` - Análisis detallado con agente auditor
- `POST /batch-analyze` - Análisis por lotes
- `POST /triage` - Clasificar caso por prioridad
- `POST /enrich` - Enriquecer caso con contexto
- `POST /group` - Agrupar casos por patrones
- `POST /playbook` - Generar playbook de respuesta
- `POST /report` - Generar reporte de fraude
- `GET /health` - Estado del sistema

## Ejemplo de Uso

```python
import requests

# Predecir fraude
transaction = {
    "step": 1,
    "type": "TRANSFER",
    "amount": 1000.0,
    "nameOrig": "C123456789",
    "oldbalanceOrg": 5000.0,
    "newbalanceOrig": 4000.0,
    "nameDest": "C987654321",
    "oldbalanceDest": 0.0,
    "newbalanceDest": 1000.0
}

response = requests.post("http://localhost:8000/predict", json=transaction)
result = response.json()
print(f"Es fraude: {result['is_fraud']}")
print(f"Probabilidad: {result['fraud_probability']:.4f}")
```
