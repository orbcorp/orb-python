# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["CustomerHierarchyConfigModel"]


class CustomerHierarchyConfigModel(TypedDict, total=False):
    child_customer_ids: List[str]
    """A list of child customer IDs to add to the hierarchy.

    The desired child customers must not already be part of another hierarchy.
    """

    parent_customer_id: Optional[str]
    """The ID of the parent customer in the hierarchy.

    The desired parent customer must not be a child of another customer.
    """
