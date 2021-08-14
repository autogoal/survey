#%%
import jinja2
from pathlib import Path
from typing import List

from models import AutoMLSystem, MetaLearning, Pipeline, SearchSpace, SearchStrategy

# %%
systems: List[AutoMLSystem] = []

for system in (Path(__file__).parent.parent / "data" / "systems").rglob("*.yml"):
    if system.name == "_template.yml":
        continue

    systems.append(AutoMLSystem.from_yaml(system))

systems.sort(key=lambda s: s.name)

# %%
with (Path(__file__).parent.parent / "data" / "templates" / "systems_list.jinja").open() as fp:
    template = jinja2.Template(fp.read())

# %%
with (Path(__file__).parent.parent / "docs" / "systems_list.md").open("w") as fp:
    fp.write(template.render(systems=systems))

# %%
with (Path(__file__).parent.parent / "data" / "templates" / "examples.jinja").open() as fp:
    template = jinja2.Template(fp.read())

for pipeline in Pipeline:
    with (Path(__file__).parent.parent / "docs" / f"{pipeline}_pipeline_examples.md").open("w") as fp:
        fp.write(template.render(systems=[s for s in systems if pipeline in s.search_space.pipelines]))

for strategy in SearchStrategy:
    with (Path(__file__).parent.parent / "docs" / f"{strategy.name}_strategy_examples.md").open("w") as fp:
        fp.write(template.render(systems=[s for s in systems if strategy in s.search_strategies]))

for strategy in MetaLearning:
    with (Path(__file__).parent.parent / "docs" / f"{strategy.name}_meta_examples.md").open("w") as fp:
        fp.write(template.render(systems=[s for s in systems if strategy in s.meta_learning]))
