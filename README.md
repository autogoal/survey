# AutoML Survey

> An (in-progress) AutoML survey focusing on practical systems.

---

This project is a community effort in constructing and maintaining an up-to-date beginner-friendly introduction to AutoML, focusing on practical systems.
AutoML is a big field, and continues to grow daily.
Hence, we cannot hope to provide a comprehensive description of every interesting idea or approach available.
Thus, we decided to focus on practical AutoML systems, and spread outwards from there into the methodologies and theoretical concepts that power these systems.
Our intuition is that, even though there are a lot of interesting ideas still in research stage, the most mature and battle-tested concepts are those that have been succesfully applied to construct practical AutoML systems.

To this end, we are building a database of qualitative criteria for all AutoML systems we've heard of.
We define an AutoML system as a software project that can be used by non-experts in machine learning to build effective ML pipelines on at least some common domains and tasks.
It doesn't matter if its open-source and/or commercial, a library or an application with a GUI, or a cloud service.
What matters is that it is intended to be used in practice, as opposed to, say, a reference implementation of a novel AutoML strategy in a Jupyter Notebook.

## Features of an AutoML system

For each of them we are creating a system card that describes, in our opinion, the most relevant features of the system, both from the scientific and the engineering points of view.
To describe an AutoML system, we use a YAML-based definition.
Most of the features are self-explanatory.

> Check [data/systems/_template.yml](data/systems/_template.yml) for a starting template.

### Basic information

The first set of characteristics describe the system's general information:

```yaml
# Name of the system
name: My AutoML System
# The URL of the main website or documentation
website: https://example.com/...
# Whether the system is open-source
open_source: yes
# List of businesses or academic institutions that directly support the
# development of the system, and/or hold intellectual property over it
institutions:
  - University of Klingon
  - Star Fleet Ltd.
# If it's open-source, link of a public source code repository, otherwise `null`
repository: https://github.com/...
# If it's open-source, a license key, otherwise `null`
license: MIT
```

### References

A list of papers or other citable sources that should be included when referencing the system.

```yaml
# List of links to relevant papers, preferably DOIs or other universal handlers,
# but can also be links to arxiv.org or other repositories
# sorted by most relevant papers, not date
references:
  - https://doi.org/...
  - https://arvix.org/abs/...
```

### Interfaces

How users interact with the system:

```yaml
# Whether the system has a command line interface
cli: yes
# Whether the system has a graphic user interface
gui: no
# Whether the system can used from an HTTP RESTful API
http: no
# Whether the system can be linked as a code library
library: yes
# Programming languages in which the system can be used, i.e.,
# it is either natively coded in that language or there are maintained bindings
# (as opposed to using language X's standard way to call code from language Y)
programming_languages:
  - python
  - r
```

### Domains

Domains describe the types of inputs on which the AutoML system can be deployed.

```yaml
# Domains in which the system can be deployed
domains:
  - images
  - nlp
  - tabular
  - time_series

# Whether the system supports multiple domains for a single workflow, e.g.,
# by allowing multiple inputs of different types simultaneously
multi_domain: yes
```

### Techniques and libraries

A list of high-level models or techniques available, and the underlying ML libraries on which their implementations are based.

```yaml
# List of high-level techniques that are available in the systems, broadly classified
# according to model families
techniques:
  - linear_models
  - trees
  - bayesian
  - kernel_machines
  - graphical_models
  - mlp
  - cnn
  - rnn
  - pretrained
  - ensembles
  - ad_hoc # indicates non-ML algorithms, e.g., tokenizers...

# Whether the system supports model distillation
distillation: yes

# List of ML libraries that support the system, i.e., where the techniques
# are actually implemented, if any
ml_libraries:
  - scikit-learn
  - keras
  - pytorch
  - nltk
  - spacy
  - transformers
```

### Tasks

Actual machine learning tasks that are performed by the system.

```yaml
# List of high-level tasks the system can perform automatically
tasks:
  - classification
  - structured_prediction
  - structured_generation
  - unstructured_generation
  - regression
  - clustering
  - imputation
  - segmentation
  - feature_preprocessing
  - feature_selection
  - data_augmentation
  - dimensionality_reduction
  # domain-agonostic data preprocessing such as normalization and scaling
  - data_preprocessing
  # refers to domain-specific preprocessing, e.g., stemming, as opposed to
  - domain_preprocessing

# Whether the system supports multiple tasks in a single workflow, e.g.,
# by allowing multiple output heads from the same neural network
multi_task: no
```

### Search strategies

Techniques used for the search/optimization process.

```yaml
# List of high-level search strategies that are available in the system
search_strategies:
  - random
  - evolutionary
  - gradient_descent
  - hill_climbing
  - bayesian
  - grid
  - hyperband
  - reinforcement_learning
  - constructive
  - monte_carlo

# If the system includes meta-learning, list of broadly classified techniques used
meta_learning:
  - portfolio
  - warm_start
```

### Search space

Features that describe the search space, the types of parameters that can be optimized, and the types of pipelines that can be represented.

```yaml
# High-level characteristics of the hyperparameter search space
search_space:
  # If there are hyperparameters that only make sense conditioned to others
  hierarchical: yes
  # If the hyperparameter space has an associated probabilistic model
  probabilistic: yes
  # If the hyperameter space can be used for gradient descent
  differentiable: no
  # If the global structure of the hyperparameter space is inferred automatically from,
  # e.g., type annotations or model's documentation, as opposed to explicitely
  # defined by the developers or the user
  automatic_construction: yes

  # Types of hyperparameters that can be optimized
  hyperparameters:
    - continuous
    - discrete
    - categorical
    - conditional

  # Types of pipelines that can be discovered by the AutoML process
  pipelines:
    # A single estimator (or model in general)
    single: yes
    # A fixed pipeline with several, but predefined, steps
    fixed: yes
    # A variable-length pipeline where each step feeds on the immediately previous' output
    linear: yes
    # An arbitrarily graph-shaped pipeline where each step can feed on any of the previous'
    graph: yes

  # Whether the seach space contains potentially invalid pipelines that are only discovered
  # when evaluated, e.g., allowing a dense-only estimator to precede a sparse transformer
  invalid_pipelines: yes
```

### Software architecture

Other relevant software engineering characteristics:

```yaml
# Whether the system is designed to be extensible, in the sense that a user can add
# a single new type of model, or search algorithm, etc., in an easy manner,
# not needing to modify any part of the system
extensible: yes
# Whether the models obtained from the AutoML process can be freely inspected by the user
# up to the level of individual parameters (e.g., neural network weights)
accessible_models: yes
# Whether the models obtained can be exported out of the AutoML system, either on a
# standard format, or, at least, in a format native of the underlying ML library,
# such that they can be deployed on another platform without depending on the AutoML system itself.
portable_models: no

# Computational resources that, if available, can be leveraged by the system
computational_resources:
  gpu: yes
  tpu: no
  cluster: no
```

## How to contribute

If you are an author or a user of any practical AutoML system that roughly fits the previous criteria, we would love to have your contributions.
You can add new systems, add information for existing ones, or fix anything that is incorrect.

To do this, either create a new file or modifying an existing file in [data/systems](data/systems).
Once done, you can run `make check` to ensure that the modifications are valid with respect to the schema defined in [scripts/models.py](scripts/models.py).
If you need to add new fields, or new values to any of the enumerations defined, feel free to modify the corresponding schema as well.
Once validated, you can open a pull request.
