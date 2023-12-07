# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, Optional
from typing_extensions import override

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PagePaginationMetadata", "SyncPage", "AsyncPage"]


class PagePaginationMetadata(BaseModel):
    has_more: bool

    next_cursor: Optional[str]


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[ModelT]:
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


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[ModelT]:
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
