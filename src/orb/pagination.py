# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class PagePaginationMetadata(BaseModel):
    has_more: bool

    next_cursor: Optional[str]


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.pagination_metadata.next_cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    pagination_metadata: PagePaginationMetadata

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.pagination_metadata.next_cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})
