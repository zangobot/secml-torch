"""Basic utils for tensor handling."""

import torch


def atleast_kd(x: torch.Tensor, k: int) -> torch.Tensor:
    """
    Add dimensions to the tensor x until it reaches k dimensions.

    Parameters
    ----------
    x : torch.Tensor
        Input tensor.
    k : int
        Number of desired dimensions.

    Returns
    -------
    torch.Tensor
        The input tensor x but with k dimensions.
    """
    shape = x.shape + (1,) * (k - x.ndim)
    return x.reshape(shape)
