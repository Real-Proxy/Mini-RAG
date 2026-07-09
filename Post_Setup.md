# Post Setup

This project currently requires one small compatibility fix for RAGAS due to an upstream issue.

## Issue

At the time of development, `ragas` (0.4.x) is incompatible with the latest LangChain ecosystem.

Importing RAGAS throws:

```text
ModuleNotFoundError:
No module named 'langchain_community.chat_models.vertexai'
```

This is a known issue:

https://github.com/explodinggradients/ragas/issues/2745

An official fix has already been submitted:

https://github.com/explodinggradients/ragas/pull/2793

---

## Temporary Fix

Install the missing provider package.

```bash
pip install langchain-google-vertexai
```

Open:

```
.venv/Lib/site-packages/ragas/llms/base.py
```

Replace:

```python
from langchain_community.chat_models.vertexai import ChatVertexAI
```

with

```python
from langchain_google_vertexai import ChatVertexAI
```

No other changes are required.

## Note

This is only a temporary workaround until the upstream RAGAS fix is merged and released.

Once the official release includes PR #2793, this manual change can be removed.