# Search spaces


## Pipelines

According to how flexible these pipelines are, we can identify four basic types:

- **Single model pipelines**: when a single model is trained end-to-end, which is often an estimator~(classifier or regressor). An example is training a neural network end-to-end for image classification, or a linear regression model for price estimation on tabular data.

- **Fixed pipelines**: when a few fixed atomic steps are considered, e.g., data preprocessing, feature selection, dimensionality reduction, and classification. In each step, several different algorithms with they respective hyperparameters can be considered.

- **Linear pipelines**:

- **Graph-based pipelines**: