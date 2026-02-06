# Issue: Possible improvements to the project (ML/DS)

**Title:** Possible improvements to the project (ML/DS)

**Body (copy into GitHub Issues):**

---

## Possible improvements (ML/DS)

Proposals for improving the retail retention classification pipeline from an ML/DS perspective:

### 1. Models
- **Add ensemble models:** e.g. `RandomForestClassifier`, `GradientBoostingClassifier` or `XGBoost`/`LightGBM` to the comparison; they often give better F1/ROC-AUC on tabular data and can be explained via SHAP (TreeExplainer).
- **Try calibration:** add `CalibratedClassifierCV` for the best model to improve reliability of predicted probabilities (e.g. for segment thresholds and business decisions).

### 2. Hyperparameters and tuning
- **Extend GridSearchCV:** add `class_weight='balanced'` (or grid over class weights) for LogisticRegression/SVC to better handle class imbalance; tune `n_neighbors` for KNN (e.g. 5–25) and add `metric` (e.g. `minkowski`, `manhattan`).
- **Cross-validation:** consider stratified K-fold with more folds (e.g. 7–10) or repeated CV to get more stable estimates of F1 and ROC-AUC.

### 3. Metrics and evaluation
- **Additional metrics:** report precision-recall curve and AUC-PR (especially useful for imbalanced target); add macro/weighted F1 if multi-class is introduced later.
- **Threshold tuning:** optimize decision threshold for the chosen metric (e.g. F1) instead of using 0.5, and document the chosen threshold for segmentation.

### 4. Features and preprocessing
- **Feature engineering:** add aggregates from `market_money` and `market_time` (e.g. trend, variance, recency) as explicit features; consider binning or polynomial features for key numerical variables if EDA suggests non-linearity.
- **Feature selection:** run recursive feature elimination (RFE) or L1-based selection after preprocessing to reduce overfitting and simplify the model; re-evaluate SHAP on the reduced set.

### 5. Data and validation
- **Stratification and splits:** ensure stratification by target (and optionally by segment) in train/val/test; consider time-based split if “период” has a time component to avoid leakage.
- **Resampling:** experiment with SMOTE or undersampling on the training set only, then re-tune and compare F1/ROC-AUC with the current pipeline.

These changes would strengthen the modeling process and make the project easier to extend and maintain.
