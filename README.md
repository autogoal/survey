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

> 💡 Check [data/systems/_template.yml](data/systems/_template.yml) for a starting template.

### Basic information

Characteristics about the basic information of the system as a software product.

- **`name`** (`str`): Name of the system.
- **`website`** (`str`): The URL of the main website or documentation.
- **`open_source`** (`bool`): Whether the system is open-source.
- **`institutions`** (`list[str]`): List of businesses or academic institutions that directly support the development of the system, and/or hold intellectual property over it.
- **`repository`** (`str`): If it's open-source, link of a public source code repository, otherwise `null`.
- **`license`** (`str`): If it's open-source, a license key, otherwise `null`.
- **`references`** (`list[str]`): List of links to relevant papers, preferably DOIs or other universal handlers, but can also be links to arxiv.org or other repositories sorted by most relevant papers, not date.

### User interfaces

Characteristics describing how the users interact with the system.

- **`cli`** (`bool`): Whether the system has a command line interface
- **`gui`** (`bool`): Whether the system has a graphic user interface
- **`http`** (`bool`): Whether the system can used from an HTTP RESTful API
- **`library`** (`bool`): Whether the system can be linked as a code library
- **`programming_languages`** (`list[str]`): List of programming languages in which the system can be used, i.e., it is either natively coded in that language or there are maintained bindings (as opposed to using language X's standard way to call code from language Y).

### Domains

Characteristics describing the domains in which the system can be applied, which roughly correspond to the types of input data that the system can handle.

- **`domains`** (`list[str]`): Domains in which the system can be deployed. Valid values are:
  - `images`
  - `nlp`
  - `tabular`
  - `time_series`
- **`multi_domain`** (`bool`): Whether the system supports multiple domains for a single workflow, e.g., by allowing multiple inputs of different types simultaneously

### Techniques

Characteristics describing the actual models and techniques used in the system, and the underlying ML libraries where those techniques are implemented.

- **`techniques`** (`list[str]`): List of high-level techniques that are available in the systems, broadly classified according to model families. Valid values are:
  - `linear_models`
  - `trees`
  - `bayesian`
  - `kernel_machines`
  - `graphical_models`
  - `mlp`
  - `cnn`
  - `rnn`
  - `pretrained`
  - `ensembles`
  - `ad_hoc`
    > 📝 indicates non-ML algorithms, e.g., tokenizers...
- **`distillation`** (`bool`): Whether the system supports model distillation
- **`ml_libraries`** (`list[str]`): List of ML libraries that support the system, i.e., where the techniques are actually implemented, if any. Valid values are lists of strings. Some examples are:
  - `scikit-learn`
  - `keras`
  - `pytorch`
  - `nltk`
  - `spacy`
  - `transformers`

### Tasks

Characteristics describing the types of tasks, or problems, in which the system can be applied, which roughly correspond to the types of outputs supported.

- **`tasks`** (`list[str]`): List of high-level tasks the system can perform automatically. Valid values are:
  - `classification`
  - `structured_prediction`
  - `structured_generation`
  - `unstructured_generation`
  - `regression`
  - `clustering`
  - `imputation`
  - `segmentation`
  - `feature_preprocessing`
  - `feature_selection`
  - `data_augmentation`
  - `dimensionality_reduction`
  - `data_preprocessing`
    > 📝 domain-agonostic data preprocessing such as normalization and scaling
  - `domain_preprocessing`
    > 📝 refers to domain-specific preprocessing, e.g., stemming, as opposed to
- **`multi_task`**: Whether the system supports multiple tasks in a single workflow, e.g.,
    by allowing multiple output heads from the same neural network

## Search strategies

Characteristics describing the optimizaction/search strategies used for model search and/or hyperparameter tunning.

- **`search_strategies`** (`list[str]`): List of high-level search strategies that are available in the system. Valid values are:
  - `random`
  - `evolutionary`
  - `gradient_descent`
  - `hill_climbing`
  - `bayesian`
  - `grid`
  - `hyperband`
  - `reinforcement_learning`
  - `constructive`
  - `monte_carlo`
- **`meta_learning`** (`list[str]`): If the system includes meta-learning, list of broadly classified techniques used. Valid values are:
  - `portfolio`
  - `warm_start`

### Search space

Characteristics describing the search space, the types of hyperparameters that can be optimized, and the types of ML pipelines that can be represented in this space.

- **`search_space`**: High-level characteristics of the hyperparameter search space.
  - **`hierarchical`** (`bool`): If there are hyperparameters that only make sense conditioned to others.
  - **`probabilistic`** (`bool`): If the hyperparameter space has an associated probabilistic model.
  - **`differentiable`** (`bool`): If the hyperameter space can be used for gradient descent.
  - **`automatic_construction`** (`bool`): If the global structure of the hyperparameter space is inferred automatically from, e.g., type annotations or model's documentation, as opposed to explicitely defined by the developers or the user.
  - **`hyperparameters`** (`list[str]`): Types of hyperparameters that can be optimized. Valid values are:
    - `continuous`
    - `discrete`
    - `categorical`
    - `conditional`
  - **`pipelines`**: Types of pipelines that can be discovered by the AutoML process. Each of the following keys is boolean.
    - **`single`** (`bool`): A single estimator (or model in general)
    - **`fixed`** (`bool`): A fixed pipeline with several, but predefined, steps
    - **`linear`** (`bool`): A variable-length pipeline where each step feeds on the immediately previous output
    - **`graph`** (`bool`): An arbitrarily graph-shaped pipeline where each step can feed on any of the previous outputs
  - **`invalid_pipelines`** (`bool`): Whether the seach space contains potentially invalid pipelines that are only discovered when evaluated, e.g., allowing a dense-only estimator to precede a sparse transformer.

### Software architecture

Other characteristics describing general features of the system as a software product.

- **`extensible`** (`bool`): Whether the system is designed to be extensible, in the sense that a user can add a single new type of model, or search algorithm, etc., in an easy manner, not needing to modify any part of the system/
- **`accessible_models`** (`bool`): Whether the models obtained from the AutoML process can be freely inspected by the user up to the level of individual parameters (e.g., neural network weights).
- **`portable_models`** (`bool`): Whether the models obtained can be exported out of the AutoML system, either on a standard format, or, at least, in a format native of the underlying ML library,such that they can be deployed on another platform without depending on the AutoML system itself.
- **`computational_resources`**: Computational resources that, if available, can be leveraged by the system.
  - **`gpu`** (`bool`): Whether the system supports GPUs.
  - **`tpu`** (`bool`): Whether the system supports TPUs.
  - **`cluster`** (`bool`): Whether the system supports cluster-based parallelism.

## How to contribute

If you are an author or a user of any practical AutoML system that roughly fits the previous criteria, we would love to have your contributions.
You can add new systems, add information for existing ones, or fix anything that is incorrect.

To do this, either create a new or modify an existing file in [data/systems](data/systems).
Once done, you can run `make check` to ensure that the modifications are valid with respect to the schema defined in [scripts/models.py](scripts/models.py).
If you need to add new fields, or new values to any of the enumerations defined, feel free to modify the corresponding schema as well (and modify both [data/systems/_template.yml](data/systems/_template.yml) and this README).

Once validated, you can open a pull request.
