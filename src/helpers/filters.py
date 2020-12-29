from datetime import date
from math import floor
from typing import Callable


def format_film_runtime(runtime: str) -> str:
    # A film is always >= 1 second. If this case is hit,
    #  it is probably a film that we can't get the runtime for
    if not runtime:
        return "Unknown"

    # https://stackoverflow.com/a/3856312
    runtime: int = int(runtime)
    hours = floor(runtime / 3600)
    mins = floor(runtime / 60 % 60)
    secs = floor(runtime % 60)

    # Only display the hours if needed
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"


def format_film_release_date(release_date: str) -> str:
    return date.fromisoformat(release_date).strftime("%B %d, %Y")


def convert_bb_code(text: str) -> str:
    bb_tags = ["[b]", "[/b]", "[i]", "[/i]", "\n"]
    html_tags = ["<strong>", "</strong>", "<em>", "</em>", "<br>\n"]

    # Convert the BBCode tags to HTML
    for i, v in enumerate(bb_tags):
        text = text.replace(v, html_tags[i])
    return text.strip()


ALL_FILTERS: list[Callable] = [
    format_film_runtime,
    format_film_release_date,
    convert_bb_code,
]
