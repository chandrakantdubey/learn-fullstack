# scikit-learn

**Role:** Primary | **Layer:** AI/ML

## Mental model
scikit-learn is a general-purpose machine-learning toolkit for classical supervised and unsupervised learning. Its value is not a collection of algorithms alone; it provides consistent estimator, preprocessing, evaluation and pipeline abstractions.

```text
data
 -> preprocessing
 -> feature representation
 -> estimator
 -> validation
 -> metrics
 -> persisted model
 -> inference
```

## Core areas
- classification and regression
- clustering
- dimensionality reduction
- preprocessing and feature engineering
- model selection and cross-validation
- metrics
- pipelines and transformers
- model persistence

## Supervised learning
Understand linear/logistic regression, trees, random forests, gradient boosting and nearest-neighbor methods conceptually. Choose based on data shape, interpretability, latency, sample size and measured validation performance.

## Pipelines
Use pipelines to keep preprocessing and model fitting coupled during cross-validation. This prevents leakage where information from validation/test data influences training transformations.

## Evaluation
Separate training, validation and test data. Choose metrics based on business cost: accuracy is often insufficient for imbalanced classification. Understand precision, recall, F1, ROC-AUC, PR-AUC, calibration and regression metrics.

## Feature engineering
Production feature transformations must be deterministic and versioned. Training/serving skew is a common failure mode when feature logic is duplicated.

## Classical ML vs deep learning
Classical ML can outperform deep learning for tabular datasets with limited data and can be cheaper and easier to operate. Deep learning becomes more compelling for unstructured modalities and representation learning.

## Production patterns
- Version datasets, features and model artifacts.
- Persist preprocessing with the model pipeline.
- Validate input distributions.
- Monitor prediction quality when labels become available.
- Track model version and feature schema.
- Reproduce training from pinned dependencies/configuration.

## Security
Treat serialized model artifacts as untrusted supply-chain inputs. Protect training data and avoid leaking sensitive features into logs or telemetry.

## Testing
Unit-test feature transformations, integration-test the complete pipeline and evaluate against frozen datasets. Test edge cases such as missing values, unseen categories and distribution shifts.

## Common mistakes
- data leakage
- evaluating on training data
- using accuracy for imbalanced problems
- preprocessing differently in production
- changing features without versioning
- assuming a more complex model is automatically better

## Interview-level topics
Bias/variance, regularization, cross-validation, leakage, feature pipelines, tree ensembles, classification metrics, calibration and model deployment lifecycle.

## Related
PyTorch, PostgreSQL, Python, Hugging Face Transformers.