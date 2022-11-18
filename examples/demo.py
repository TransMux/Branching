import numpy as np
from numpy import ndarray

from Branching import Plugin


@Plugin
def get_data(seed: int) -> ndarray:
    np.random.seed(seed)
    return np.random.randn(5, 5)


@get_data.before
def fix_the_seed():
    return {"seed": 42, "source": "user"}


@get_data.after
def print_the_source(_result, source: str):
    return f"{_result} from Source: {source}"


if __name__ == '__main__':
    print(get_data(10001))
