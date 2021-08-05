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
Based on these characteristics, we created a taxonomy of commonly used theoretical concepts in AutoML, which guide this survey.
We provide follow-up references on many of the topics we cover.

## AutoML in a nutshell
