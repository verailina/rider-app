from typing import Tuple, Callable
import numpy as np  # type: ignore
from geopy.distance import great_circle  # type: ignore


Coord = Tuple[float, float]


def distance_km(a: Coord, b: Coord):
    """
    Измерение расстояний между парами координат. Использует great_circle():
    менее точен, но быстрее чем geopy.distance.distance. См.
    https://geopy.readthedocs.io/en/stable/#module-geopy.distance
    """
    return great_circle(a, b).km


def safe_distance(a: Coord, b: Coord) -> float:
    """
    Безопасный доступ к distance_km.
    Используется с routes.distance_delta.
    """
    if a == b:
        return 0
    try:
        return distance_km(a, b)
    except ValueError:
        return np.nan

