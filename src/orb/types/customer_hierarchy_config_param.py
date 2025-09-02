# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["CustomerHierarchyConfigParam"]


class CustomerHierarchyConfigParam(TypedDict, total=False):
    child_customer_ids: SequenceNotStr[str]
    """A list of child customer IDs to add to the hierarchy.

    The desired child customers must not already be part of another hierarchy.
    """

    parent_customer_id: Optional[str]
    """The ID of the parent customer in the hierarchy.

    The desired parent customer must not be a child of another customer.
    """
