# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

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
            if self.pagination_metadata.next_cursor is not None:
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
            if self.pagination_metadata.next_cursor is not None:
                next_cursor = self.pagination_metadata.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
