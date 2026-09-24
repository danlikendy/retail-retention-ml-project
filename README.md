# Who is cooling off

E-commerce book: **1 300** customers, four tables (profile, revenue by period, time on site, 3-month profit). Target is purchase activity: **«Снизилась»** vs **«Прежний уровень»** — **38.3% / 61.7%**. The retain team wants who is slipping **and** still worth a coupon.

Live write-up: **[danlikendy.github.io/retail-retention-ml-project](https://danlikendy.github.io/retail-retention-ml-project/)**

F1 on the decline class is the score I care about. Accuracy on a 62% majority is cheap.

---

## Problem

People who still buy on promo, browse few pages, and sat through last month are the ones who drop. After the join you have one row per id. I cut **risk × profit** at the 70th percentile of each — four buckets. The only bucket you actually call is high risk, high profit.

`GridSearchCV(scoring="f1")` on a **string** target without `pos_label` returns **NaN**. The notebook run that is in git has CV F1 as `nan` for every model, then picks KNN by accident. I do not quote the conclusions cell (LogReg F1 0.845 / AUC 0.906) — that text does not match the printed test cell.

## What I shipped

| Piece | Choice |
|---|---|
| Target | decline = `Снизилась` |
| Prep | `ColumnTransformer`: scale nums, OHE cats |
| Models | kNN, tree, logreg, SVC — GridSearchCV, 5-fold |
| Hold-out (printed) | **F1 0.794**, **ROC-AUC 0.884**, acc 0.846, rec 0.770 |
| Segments | 70th pct risk × 70th pct profit |
| Explain | SHAP on the fitted pipeline |

Pages per visit, category breadth, last-month time on site, promo share, 6-month marketing intensity — that is the SHAP order in the notebook.

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -q
```

Notebook (join → grids → SHAP → buckets): `notebooks/eda_and_training.ipynb`. CSVs sit in the **repo root**. Run the kernel with cwd = root, or the first cell also looks in `/datasets/`.

More: [docs/RUN.md](docs/RUN.md) · [docs/API.md](docs/API.md)

## Layout

```
src/           decline flag, risk×profit segments
tests/
notebooks/     full training path
market_*.csv, money.csv
```

---

Artem Tsygantsov · [tsygantsov.ru](https://tsygantsov.ru) · MIT
