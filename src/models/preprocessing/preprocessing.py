from abc import ABC, abstractmethod

import torch


class Preprocessing(ABC):
    @abstractmethod
    def preprocess(self, x: torch.Tensor) -> torch.Tensor:
        ...

    def invert(self, x: torch.Tensor) -> torch.Tensor:
        ...

    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        return self.preprocess(x)
