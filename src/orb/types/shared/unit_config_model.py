# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["UnitConfigModel"]


class UnitConfigModel(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""
