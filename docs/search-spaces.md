# Search spaces

!!! warning
    *This section is under construction*

In the context of AutoML, a search space is an implicitly- or explicitly-defined collection of machine learning pipelines, among which to search for a suitable solution to a given machine learning problem.
The search space in any given AutoML system ultimately defines which solutions are possible at all.
To characterize common search spaces, we'll focus first on the building blocks of any search space: [operators](#operators), [hyperparameters](#hyperparameters), and [pipelines](#pipelines).
Then we'll look at [common characteristics](#other-features-of-search-spaces) that can help us analize and compare the search spaces in current AutoML systems.

## Operators

An operator is any atomic component that performs a given function in a machine learning pipeline: e.g., a tokenization algorithm, a feature selector, or a classification model.
For the purpose of AutoML, operators are often black-box; that is, we don't care about their internal structure, we just care about whether they can fit in any given pipeline.
Operators are thus often characterized by input, output, and a set of [hyperparameters](#hyperparameters).

The input and output define how that operator interacts with other operators in any given pipeline.
This is not as simple as defining an input and output *type*, since often types, at least in their conventional definition in programming languages (i.e., independent types), are insufficient to completely characterize whether an operator can act on a given input.
For example, most algorithms in [`scikit-learn`](https://scikit-learn.org) take matrices as input, but some can only act on *dense* matrices, while others work for both dense and sparse matrices.
Similarly, in NAS, most operators are neural layers, which all receive tensors as inputs.
However, they work on specific tensor *shapes*, and we cannot connect a layer $l_1$ to another layer $l_2$ unless their output and input shapes match, respectively.

Therefore, to completely characterize an operator, an AutoML systems needs and implict or explicit typing system that is able to capture these restrictions.
The more flexible the pipeline representation and the more varied the types of operators involved, the more sophisticated the typing system should be.
In [fixed-size pipelines](#fixed-size-pipelines), for example, it often suffices to consider that every operator in each step has a definite input and output type.
However, [linear](#linear-pipelines) or [graph-based](#graph-based-pipelines) pipelines need explicit or implicit restrictions about which operators can connect to each other.

### Models

One special type of operators are models, which have that have internal parameters which are adjusted from training data.
For example, in a decision tree classifier, the structure of the tree is adjusted such that it maximizes the probability of classifying correctly all the elements in the training set.
The difference between models and the other operators is important because every machine learning pipeline ultimately fits one or more models.
All the remaining operators are there for secundary, even if often crucial, tasks, such as feature preprocessing or dimensionality reduction.

Models break the *operator as a black-box illusion* in one important sense: they have two modes of operation that must be dealt with explicitely in the AutoML engine: training and prediction.
Contrary to the other, model-free operators, models must be run once on training data to adjust their parameters, and only then can they be actually used on new data.
Thus, all AutoML systems must somehow deal with this two-mode operation issue.
The most common strategy is to consider *all* operators to work in these two modes, with model-free operators just ignoring whatever mode they're in.

## Hyperparameters

Hyperparameters are the tunable values of any operator that are not adjusted from data, but must be decided with a data-independent strategy.
Examples include the number of layers or the activation functions in a neural network, the regularization strength in a linear classifier, or the maximum depth in a tree-based model.

In a sense, the whole purpose of AutoML can be defined as finding the optimal configuration for all the hyperparameters involved in a set of selected operators.
In fact, some AutoML paradigms are built entirely on top of the hyperparameter optimzation conceptualization.
Paradigms like [CASH](../#combined-algorithm-selection-and-hyperparameter-optimization) consider the selection of operators as [categorical hyperparameters](#categorical-hyperparameters), defining an implicit [two-level hierarchical space](#hierarchical-spaces).

### Continuous and discrete hyperparameters

The simplest types of hyperparameters are numerical values, either continuous or discrete.
Examples include the regularization strength in logistic regression, or the maximum depth in a decision tree.
In the simplest case, a numerical hyperparameter has a defined range of valid values for the optimizer can choose from.
From a probabilistic point of view, this represents an implicit uniform distribution on the hyperparameter domain.

However, in some cases it makes more sense to explore the domain a specific hyperparameter with a different distribution.
As an example, take the regularization strength $R$ of a simple logistic regression model.
The sensible values for $R$ may lie anywhere between $10^{-6}$ to $1$.
Asuming a uniform distribution in this case means that values between $0.1$ and $1$ will have roughly 90% of the attention of the optimizer, and values between $10^{-6}$ and $10^{-5}$ will be selected one in a million times.
That's probably not what we want, but, on the contrary, we expect values between, say $10^{-3}$ and $10^{-2}$ to be as likely as those between $10{^-2}$ and $10^{-1}$.
In this case, we can define a logarithmic distribution instead of a uniform distribution, effectively stretching out the smallest scales of the hyperparameter range.

### Categorical hyperparameters

Categorical hyperparameters are used to model qualitatively different choices, such as the kernel function in a support vector machine, the activation function in a neural network's layer, or the regularization penalty function in a logistic regression.
Since categorical values have no inherent order, they *should not* be treated as discrete values.
The most common strategy is to define a categorical distribution, which assigns a probability $p_i$ to every value $h_i$ of a given hyperparameter $h$, such that $\sum  p_i = 1$.

### Conditional hyperparameters

Conditional hyperparameters appear when one or more hyperparameters only make sense sometimes, that is, *conditioned* to some other.
The simplest case is in a [two-level hierarchical space](#hierarchical-spaces), where the first level defines the type of model, and the second level defines the hyperparameters of each model.
For example, suppose we have three different operators to choose from: SVM, logistic regression, and decision trees, each with their own hyperparameters.
Lets assume the selection of which operator to use is indicated by a categorical hyperparameter called `model`.
The value of the hyperparameter `kernel_function` is only relevant when `model=svm`.
The hyperparameter `kernel_function` is thus said to be conditioned to the value of the hyperparameter `model`.

Conditional hyperparameters can also appear in non-hierarchical spaces.
For example, suppose we have again an SVM operator with different kernel functions available: `linear`, `rbf` and `poly`.
When `kernel_function=poly`, a new hyperparameter `degree` becomes relevant, which is not used in the other kernel functions.

As long as dependencies among hyperparameters are acyclical, we can transform the search space into a hierarchical one, such that conditional hyperparameters are selected in a level below the hyperparameters they depend on.
In some cases we have constraints that restrict two hyperparameters from simultaneously taking some pairs of values.
These cases cannot be easily transformed into hierarchical spaces without introducing an arbitrary order between the hyperparameters.
The most flexible AutoML systems have mostly conditioned hyperparameters, which in turn result in highly hierarchical search spaces.

## Pipelines

According to how flexible these pipelines are, we can identify four basic types:

### Single model pipelines

When a single model is trained end-to-end, which is often an estimator (e.g., a classifier or regressor).
An example is training a linear regression model for price estimation on tabular data, or fine-tunning a concrete neural network architecture end-to-end for image classification.

**Examples:** {!docs/single_pipeline_examples.md!}

### Fixed-size pipelines

When a few fixed atomic steps are considered, e.g., data preprocessing, feature selection, dimensionality reduction, and classification.
In each step, several different algorithms with they respective hyperparameters can be considered.

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