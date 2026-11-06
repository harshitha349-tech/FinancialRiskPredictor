# CreditLens Architecture

```text
React + Vite UI
      |
      v
FastAPI REST API
      |
      +--> Assessment service --> preprocessing/model --> prediction
      |                              |
      |                              +--> SHAP explanation
      |                              +--> risk engine
      |                              +--> recommendation
      |
      +--> simulation service --> same prediction pipeline
      |
      +--> monitoring service --> SQLite risk history
      |
      +--> model metrics --> stored evaluation results
```

The backend is intentionally a single application. The project does not require external databases, message brokers, containers, or cloud services.
