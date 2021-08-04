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

For each of them we are creating a system card that describes, in our opinion, the most relevant features of the system, both from the scientific and the engineering points of view.
To describe an AutoML system, we use a YAML-based definition.
Most of the features are self-explanatory.
Check [data/systems/_template.yml](data/systems/_template.yml) for an overview and starting template.

## How to contribute

If you are an author or a user of any practical AutoML system that roughly fits the previous criteria, we would love to have your contributions.
You can add new systems, add information for existing ones, or fix anything that is incorrect.

To do this, either create a new file or modifying an existing file in [data/systems](data/systems).
Once done, you can run `make check` to ensure that the modifications are valid with respect to the schema defined in [scripts/models.py](scripts/models.py).
If you need to add new fields, or new values to any of the enumerations defined, feel free to modify the corresponding schema as well.
Once validated, you can open a pull request.
