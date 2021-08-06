# Introduction to AutoML

*Automated Machine Learning*, or AutoML for short, is a novel and expanding field in the intersection of machine learning, optimization, and software engineering.
It's purpose is to progresively automate the most common (and often boring) tasks of conventional ML workflows.
Tasks such as data preprocessing, feature extraction and selection, model selection, hyperparameter tunning, model validation, deployment, and monitoring.
Despite its novelty, AutoML has become prominent in the last few years, as more profesionals from every field get into machine learning, often without a solid background in machine learning and no time to learn all the necessary theory.

The following is a beginner-friendly introduction to the AutoML field.
Our purpose is not to survey all the deep theory behind AutoML, but rather to provide an entry-point for newcommers, interested both in the research aspects and the practical aspects of AutoML.
To narrow our focus, we decided to analize a set of practical AutoML systems, and extend outwards into the underlying theory guided by the paradigms and concepts that are most commonly used in these practical scenarios.
To consider an AutoML system for inclusion, we defined a set of loose criteria, mostly regarding its status as a software product intended for broad use rather than, say, a reference implementation of a novel technique for research purposes.
Thus, we consider a broad range of systems, both open-source and commercial, in different levels of maturity and with widely different features, as long as they fit the above criteria.
The [list of AutoML systems](./systems) considered in this survey, and the [features](./comparison) that are evaluated, are the result of [a colaborative effort](https://github.com/autogoal/survey).

Based on the analized systems we defined a set of conceptual features that help mapping the AutoML field, at least from a practical point-of-view.
These features involve both internal and external characteristics of the systems.
The internal characteristics refer to how the system works, e.g., the techniques it uses for optimizing and searching machine learning pipelines, and the types of hyperparameters it can represent.
The external characteristics refer to the types of tasks that can be solved with the system and the way the user interacts with it.
Based on these characteristics, we created a taxonomy of commonly used theoretical concepts, principle, and paradigims in the AutoML field, which guide this survey.
We provide follow-up references on many of the topics we cover.

## AutoML in a nutshell

At its core, AutoML is about providing tools to automate the process of designing, training, validating, and deploying a machine learning pipeline for a given problem.
ML pipelines come in varied flavour, but they are often composed of a set of atomic steps~(e.g., a feature selection algorithm, or a specific machine learning model), each of which can be configured by one or more *hyperparameters*~(e.g., the number and type of layers and neurons per layer in a neural network, or the regularization factor in logistic regression).
Each step performs some task, often associated with an input data source, and producing an output that is fed to subsequent steps.
The objective is to find a pipeline that is optimal, or close to optimal, in solving a given machine learning problem, among a set of posible pipelines.

Thus, we can see an AutoML system, on a broad perspective, as a computational solution that receives a machine learning problem definition of some kind~(e.g., classification, regression, clustering) and associated training data, and it outputs a suitable machine learning pipeline, composed of one or more atomic steps, that is close to optimal in solve that problem according to some predefined performance metric(s).

The core of any AutoML system is a *machine learning pipeline optimization engine*.
Three key components can be identified in any such engine: a search space, a search strategy, and a performance estimation function.

The [search space](./search-space) defines which types of pipelines are available. It is often restricted by an underlying machine learning library (or libraries) that support the actual implementation of said pipelines.
For example, AutoML systems based on [scikit-learn](https://scikit-learn.org) can only output pipelines composed of scikit-learn estimators and transformers, while AutoML systems based on [keras]() or [pytorch] can output pipelines that correspond to neural network architectures.
The search space also defines which hyperparameters are optimized, and to what extent.

A [search strategy](./search-strategy) is an algorithm to efficiently explore a given search space and find the optimal pipelines.
The search space can be arbitrarily big, exponential in size with respect to the number of available algorithms, and potentially unbounded in some hyperparameters~(e.g., you can add as many layers as you want to a neural network).
Thus, an effective search strategy must be able to quickly find promising regions of the search space.

Finally, the [performance estimation function](./performance-estimation) measures the expected performance of any given pipeline in the task at hand.
The simplest performance estimation consists in evaluating the pipeline in a validation dataset, but evaluating machine learning algorithms is a costly task, especially when using models with millions or billions of parameters, like the largest neural networks.
Thus, we often want to estimate this performance either by evaluating in smaller sets or by creating surrogate functions that approximate it.
Furthermore, we often want to optimize more than one performance indicator, which may be in contradiction, such as accuracy versus model complexity (to reduce inference time).

These three components make up the core of what we call the "internal characteristics" of an AutoML system.
In this survey, we are also interested in "external" characteristics, such as the types of machine learning tasks that can be solved, the interfaces by which users interact with the system, the steps of the machine learning workflow that are covered, and other software engineering concerns.

In the next few sections we'll review the basic theory behind the core AutoML process.
We'll introduce the most common types of search spaces and strategies, and some interesting performance estimation functions.
Finally, we'll present a comparison of many practical AutoML systems in terms of all of these characteristics, and provide some rules guidelines for choosing an appropiate tool for a given task.
