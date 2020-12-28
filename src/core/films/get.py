from src.helpers import api


__all__ = ["years", "films_in_year"]


def years() -> list[str]:
    """Get all available film years."""
    return api.get("archive", params={"year": "all"})


def films_in_year(year: str) -> list[dict]:
    """Get all available film years."""
    return api.get("archive", params={"year": year})
