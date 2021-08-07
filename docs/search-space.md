# Search spaces

In the context of AutoML, a search space is an implicitly- or explicitly-defined collection of machine learning pipelines, among which to search for a suitable solution to a given machine learning problem.
The search space in any given AutoML system ultimately defines what is possible at all.
To characterize common search spaces, we'll focus first on the building blocks of any search space: [operators](#operators), [hyperparameters](#hyperparameters), and [pipelines](#pipelines).

## Operators

An operator is any atomic component that performs a given function in a machine learning pipeline: e.g., a tokenization algorithm, a feature selector, or a classification model.
For the purpose of AutoML, operators are often black-box; that is, we don't care about their internal structure, we just care about whether they can fit in any given pipeline.
Operators are thus often characterized by input, output, and a set of [hyperparameters](#hyperparameters).

The input and output define how that operator interacts with other operators in any given pipeline.
This is not as simple as defining an input and output *type*, since often types, at least in their conventional definition in programming languages (i.e., independent types), are insufficient to completely characterize whether an operator can act on a given input.
For example, most algorithms in [`scikit-learn`](https://scikit-learn.org) take matrices as input, but some can only act on *dense* matrices, while others work for both dense and sparse matrices.
Similarly, in NAS, most operators are neural layers, which all receive tensors as inputs.
However, they work on specific tensor *shapes*, and we cannot connect a layer $L_1$ to another layer $L_2$ unless their output and input shapes match, respectively.

Therefore, to completely characterize an operator, an AutoML systems needs and implict or explicit typing system that is able to capture these restrictions.
The more flexible the pipeline representation and the more varied the types of operators involved, the more sophisticated the typing system should be.
In [fixed-size pipelines](#fixed-size-pipelines), for example, it often suffices to consider that every operator in each step has a definite input and output type.
However, [linear](#linear-pipelines) or [graph-based](#graph-based-pipelines) pipelines need explicit or implicit restrictions about which operators can connect to each other.

### Models

One special type of operators are models, which have that have internal parameters which are adjusted from training data.
For example, in a decision tree classifier, the structure of the tree is adjusted such that it maximizes the probability of classifying correctly all the elements in the training set.
The difference between models and the other operators is important because every machine learning pipeline ultimately fits one or more models.
All the remaining operators are there for secundary, even if often crucial, tasks, such as feature preprocessing or dimensionality reduction.

## Hyperparameters

Hyperparameters are the tunable values of any operator that cannot be adjusted from data, but must be decided with a data-independent strategy.

### Continuous and discrete hyperparameters

### Categorical hyperparameters

### Conditional hyperparameters

## Pipelines

According to how flexible these pipelines are, we can identify four basic types:

### Single model pipelines

When a single model is trained end-to-end, which is often an estimator (e.g., a classifier or regressor). An example is training a neural network end-to-end for image classification, or a linear regression model for price estimation on tabular data.

**Examples:** {!docs/single_pipeline_examples.md!}

### Fixed-size pipelines

When a few fixed atomic steps are considered, e.g., data preprocessing, feature selection, dimensionality reduction, and classification. In each step, several different algorithms with they respective hyperparameters can be considered.

**Examples:** {!docs/fixed_pipeline_examples.md!}

### Linear pipelines

**Examples:** {!docs/linear_pipeline_examples.md!}

### Graph-based pipelines

**Examples:** {!docs/graph_pipeline_examples.md!}

## Other features of search spaces

### Hierarchical spaces

### Probabilistic spaces

### Differentiable spaces

### Implicit versus explicit spaces