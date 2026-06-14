from dataclasses import dataclass

import numpy as np


@dataclass
class EmbeddingResult:
    vector: np.ndarray
    dimension: int