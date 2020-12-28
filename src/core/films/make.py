import json
import shutil
from os import fspath
from pathlib import Path

import sys_vars
from jinja2 import Environment

__all__ = ["dist", "render", "page", "search_json"]


def dist(dir_names: list[str]) -> None:
    dist_path = sys_vars.get_path("DEST_PATH")

    # Create the film years folders
    for dir_name in dir_names:
        (dist_path / "films" / dir_name).mkdir(parents=True, exist_ok=True)

    # Create the film images folder
    (dist_path / "films" / "images").mkdir(parents=True, exist_ok=True)

    # Create the site static files folders and files
    (dist_path / "images").mkdir(parents=True, exist_ok=True)
    src_path = fspath(Path() / "src" / "static")
    shutil.copytree(src_path, fspath(dist_path), dirs_exist_ok=True)


def render(
    name: str,
    render_opts: dict,
    jinja: Environment,
) -> str:
    template = jinja.get_template(f"{name}.jinja2")
    return template.render(**render_opts)


def search_json(data: dict) -> None:
    json_file = sys_vars.get_path("DEST_PATH") / "js" / "films.js"
    str_data = json.dumps(data)

    # After we stringify the JSON data, append the following
    # ES Module export defaults so we can load it as
    # an ES module and search on the data way more easily.
    # This is D U M B but it works
    str_data = f"export default {str_data}"
    json_file.write_text(str_data)


def page(*args: str, data: str = ""):
    (sys_vars.get_path("DEST_PATH").joinpath(*args)).write_bytes(bytes(data, "utf-8"))
