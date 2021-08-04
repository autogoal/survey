from typing import List, Optional
import pydantic
import enum
from utils import StrEnum


class Domain(StrEnum):
    images = enum.auto()
    nlp = enum.auto()
    tabular = enum.auto()
    time_series = enum.auto()


class Technique(StrEnum):
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
    ad_hoc = enum.auto()


class MetaLearning(StrEnum):
    portfolio = enum.auto()
    warm_start = enum.auto()


class Task(StrEnum):
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
    data_preprocessing = enum.auto()
    domain_preprocessing = enum.auto()


class SearchStrategy(StrEnum):
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


class Hyperparameters(StrEnum):
    continuous = enum.auto()
    discrete = enum.auto()
    categorical = enum.auto()
    conditional = enum.auto()


class Pipeline(pydantic.BaseModel):
    single: bool
    fixed: bool
    linear: bool
    graph: bool


class SearchSpace(pydantic.BaseModel):
    hierarchical: bool
    probabilistic: bool
    differentiable: bool
    automatic_construction: bool

    hyperparameters: List[Hyperparameters]

    pipelines: Pipeline

    invalid_pipelines: bool


class ComputationalResources(pydantic.BaseModel):
    gpu: bool
    tpu: bool
    cluster: bool


class AutoMLSystem(pydantic.BaseModel):
    name: str
    website: Optional[pydantic.HttpUrl]
    open_source: bool
    institutions: List[str]
    repository: Optional[pydantic.HttpUrl]
    license: Optional[str]

    references: List[pydantic.HttpUrl]

    cli: bool
    gui: bool
    http: bool
    library: bool
    programming_languages: List[str]

    domains: List[Domain]
    multi_domain: bool

    techniques: List[Technique]
    ml_libraries: List[str]

    multi_task: bool
    tasks: List[Task]

    distillation: bool

    search_strategies: List[SearchStrategy]
    search_space: SearchSpace
    meta_learning: List[MetaLearning]

    extensible: bool
    accessible_models: bool
    portable_models: bool
    computational_resources: ComputationalResources


if __name__ == "__main__":
    print(AutoMLSystem.schema_json(indent=2))
