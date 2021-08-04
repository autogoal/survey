from typing import List, Optional
import pydantic
import enum


class Domain(enum.StrEnum):
    images = enum.auto()
    nlp = enum.auto()
    tabular = enum.auto()
    time_series = enum.auto()


class Technique(enum.StrEnum):
    linear_models = enum.auto()
    trees = enum.auto()
    bayesian = enum.auto()
    kernel_machines = enum.auto()
    graphical_models = enum.auto()
    mlp = enum.auto()
    cnn = enum.auto()
    rnn = enum.auto()
    pretrained = enum.auto()
    ensembles = enum.auto()
    ad_hoc = enum.auto() # indicates non-ML algorithms, e.g., tokenizers...


class MetaLearning(enum.StrEnum):
    portfolio = enum.auto()
    warm_start = enum.auto()


class Task(enum.StrEnum):
    classification = enum.auto()
    structured_prediction = enum.auto()
    structured_generation = enum.auto()
    unstructured_generation = enum.auto()
    regression = enum.auto()
    clustering = enum.auto()
    imputation = enum.auto()
    segmentation = enum.auto()
    feature_preprocessing = enum.auto()
    feature_selection = enum.auto()
    data_augmentation = enum.auto()
    dimensionality_reduction = enum.auto()
    # domain-agonostic data preprocessing such as normalization and scaling
    data_preprocessing = enum.auto()
    # refers to domain-specific preprocessing, e.g., stemming, as opposed to
    domain_preprocessing = enum.auto()


class SearchStrategy(enum.StrEnum):
    random = enum.auto()
    evolutionary = enum.auto()
    gradient_descent = enum.auto()
    hill_climbing = enum.auto()
    bayesian = enum.auto()
    grid = enum.auto()
    hyperband = enum.auto()
    reinforcement_learning = enum.auto()
    constructive = enum.auto()
    monte_carlo = enum.auto()


class Hyperparameters(enum.StrEnum):
    continuous = enum.auto()
    discrete = enum.auto()
    categorical = enum.auto()
    conditional = enum.auto()


class Pipeline(pydantic.BaseModel):
    # A single estimator (or model in general)
    single: bool
    # A fixed pipeline with several, but predefined, steps
    fixed: bool
    # A variable-length pipeline where each step feeds on the immediately previous' output
    linear: bool
    # An arbitrarily graph-shaped pipeline where each step can feed on any of the previous'
    graph: bool


class SearchSpace(pydantic.BaseModel):
    # If there are hyperparameters that only make sense conditioned to others
    hierarchical: bool
    # If the hyperparameter space has an associated probabilistic model
    probabilistic: bool
    # If the hyperameter space can be used for gradient descent
    differentiable: bool
    # If the global structure of the hyperparameter space is inferred automatically from,
    # e.g., type annotations or model's documentation, as opposed to explicitely
    # defined by the developers or the user
    automatic_construction: bool

    # Types of hyperparameters that can be optimized
    hyperparameters: List[Hyperparameters]

    # Types of pipelines that can be discovered by the AutoML process
    pipelines: Pipeline

    # Whether the seach space contains potentially invalid pipelines that are only discovered
    # when evaluated, e.g., allowing a dense-only estimator to precede a sparse transformer
    invalid_pipelines: bool


class ComputationalResources(pydantic.BaseModel):
    gpu: bool
    tpu: bool
    cluster: bool


class AutoMLSystem(pydantic.BaseModel):
    # Name of the system
    name: str
    # The URL of the main website or documentation
    website: Optional[pydantic.HttpUrl]
    # Whether the system is open-source
    open_source: bool
    # List of businesses or academic institutions that directly support the
    # development of the system, and/or hold intellectual property over it
    institutions: List[str]
    # If it's open-source, link of a public source code repository, otherwise `null`
    repository: Optional[pydantic.HttpUrl]
    # If it's open-source, a license key, otherwise `null`
    license: Optional[str]

    # List of links to relevant papers, preferably DOIs or other universal handlers,
    # but can also be links to arxiv.org or other repositories
    # sorted by most relevant papers, not date
    references: List[pydantic.HttpUrl]

    # Whether the system has a command line interface
    cli: bool
    # Whether the system has a graphic user interface
    gui: bool
    # Whether the system can used from an HTTP RESTful API
    http: bool
    # Whether the system can be linked as a code library
    library: bool
    # Programming languages in which the system can be used, i.e.,
    # it is either natively coded in that language or there are maintained bindings
    # (as opposed to using language X's standard way to call code from language Y)
    programming_languages: List[str]

    # Domains in which the system can be deployed
    domains: List[Domain]

    # Whether the system supports multiple domains for a single workflow, e.g.,
    # by allowing multiple inputs of different types simultaneously
    multi_domain: bool

    # Whether the system supports multiple tasks in a single workflow, e.g.,
    # by allowing multiple output heads from the same neural network
    multi_task: bool

    # List of high-level techniques that are available in the systems, broadly classified
    # according to model families
    techniques: List[Technique]

    # List of ML libraries that support the system, i.e., where the techniques
    # are actually implemented.
    ml_libraries: List[str]

    # List of high-level tasks the system can perform automatically
    tasks: List[Task]

    # Whether the system supports model distillation
    distillation: bool

    # If the system includes meta-learning, list of broadly classified techniques used
    meta_learning: List[MetaLearning]

    # List of high-level search strategies that are available in the system
    search_strategies: List[SearchStrategy]

    # High-level characteristics of the hyperparameter search space
    search_space: SearchSpace

    # Whether the system is designed to be extensible, in the sense that a user can add
    # a single new type of model, or search algorithm, etc., in an easy manner,
    # not needing to modify any part of the system
    extensible: bool

    # Whether the models obtained from the AutoML process can be freely inspected by the user
    # up to the level of individual parameters (e.g., neural network weights)
    accessible_models: bool

    # Whether the models obtained can be exported out of the AutoML system, either on a
    # standard format, or, at least, in a format native of the underlying ML library,
    # such that they can be deployed on another platform without depending on the AutoML system itself.
    portable_models: bool

    # Computational resources that, if available, can be leveraged by the system
    computational_resources: ComputationalResources


if __name__ == "__main__":
    print(AutoMLSystem.schema_json(indent=2))
