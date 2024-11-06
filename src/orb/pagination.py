# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ._models import BaseModel

from typing import Optional, List

from typing_extensions import override

import re
from typing import Optional, TypeVar, List, Generic, Dict, Any, Type, Mapping, cast
from typing_extensions import TypedDict, Literal, Annotated, Protocol, runtime_checkable

from httpx import URL, Response
from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._utils import PropertyInfo, is_mapping
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage, PageInfo

__all__ = ["PagePaginationMetadata", "SyncPage", "AsyncPage"]

_T = TypeVar("_T")


class PagePaginationMetadata(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.pagination_metadata is not None:  # pyright: ignore[reportUnnecessaryComparison]
            next_cursor = self.pagination_metadata.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = None
        if self.pagination_metadata is not None:  # pyright: ignore[reportUnnecessaryComparison]
            next_cursor = self.pagination_metadata.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
