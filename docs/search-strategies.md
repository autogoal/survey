# Search strategies

!!! warning
    *This section is under construction*

A search strategy is an algorithm that finds well-performing pipelines in a given [search space](../search-space).
Most search strategies are applicable to a variety of search spaces, but often require some specific characteristics.
For example, [bayesian optimization](#bayesian-optimization) requires probabilistic spaces, because it uses the probabilistic distribution as the means to explore the space.

The other ingredient of a search strategy, once a search space is defined, is a [performance metric](../performance-estimation) to optimize.
Most search strategies are compatible with multiple metrics, but some have pre-requisites as well.
For example, [gradient descent methods](#gradient-descent) requires the performance metric to be differentiable with respect to the search space.

## Sampling-based methods

### Random search

**Examples:** {!docs/random_strategy_examples.md!}

### Grid search

**Examples:** {!docs/grid_strategy_examples.md!}

### Hill climbing

**Examples:** {!docs/hill_climbing_strategy_examples.md!}

### Gradient descent

**Examples:** {!docs/gradient_descent_strategy_examples.md!}

### Evolutionary search

**Examples:** {!docs/evolutionary_strategy_examples.md!}

### Bayesian optimization

**Examples:** {!docs/bayesian_strategy_examples.md!}

## Constructive methods

### Monte Carlo tree search

**Examples:** {!docs/monte_carlo_strategy_examples.md!}

### Reinforced learning

**Examples:** {!docs/reinforcement_learning_strategy_examples.md!}

## Meta-learning

### Portfolio-based methods

**Examples:** {!docs/portfolio_meta_examples.md!}

### Warm starting

**Examples:** {!docs/warm_start_meta_examples.md!}
