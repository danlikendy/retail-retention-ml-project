# Run

Python 3.10+. From the **repo root** (CSV paths are relative to cwd):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -q
jupyter notebook notebooks/eda_and_training.ipynb
```

`money.csv` is `;` + comma decimals. The other three are ordinary commas.

To score F1 on this target in new code, pass `pos_label="Снизилась"` (or map to 0/1 via `src.labels.decline_flag` first). Bare `scoring="f1"` on strings is NaN.

Classes: [API.md](API.md).
