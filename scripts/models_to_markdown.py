#%%
import jinja2
from pathlib import Path
from typing import List
from models import AutoMLSystem

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
