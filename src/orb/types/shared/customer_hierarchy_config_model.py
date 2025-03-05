# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CustomerHierarchyConfigModel"]


class CustomerHierarchyConfigModel(BaseModel):
    child_customer_ids: Optional[List[str]] = None
    """A list of child customer IDs to add to the hierarchy.

    The desired child customers must not already be part of another hierarchy.
    """

    parent_customer_id: Optional[str] = None
    """The ID of the parent customer in the hierarchy.

    The desired parent customer must not be a child of another customer.
    """
