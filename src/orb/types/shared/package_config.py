# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PackageConfig"]


class PackageConfig(BaseModel):
    package_amount: str
    """A currency amount to rate usage by"""

    package_size: int
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """
