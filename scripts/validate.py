import pydantic
import yaml
import pathlib

from models import AutoMLSystem

systems_dir = pathlib.Path(__file__).parent.parent / "data" / "systems"
all_ok = True

for system_fp in systems_dir.rglob("*.yml"):
    try:
        AutoMLSystem.from_yaml(system_fp)
    except pydantic.ValidationError as err:
        print(f"🔴 {system_fp.stem} : {err}\n")
        all_ok = False

if all_ok:
    print("✅ All OK")
else:
    exit(1)
