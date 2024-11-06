# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from orb import Orb, AsyncOrb

from orb.types import CreditNote

from orb.pagination import SyncPage, AsyncPage

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types import credit_note_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        credit_note = client.credit_notes.list()
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        credit_note = client.credit_notes.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.credit_notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.credit_notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = response.parse()
            assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        credit_note = client.credit_notes.fetch(
            "credit_note_id",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.credit_notes.with_raw_response.fetch(
            "credit_note_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.credit_notes.with_streaming_response.fetch(
            "credit_note_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = response.parse()
            assert_matches_type(CreditNote, credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_note_id` but received ''"):
            client.credit_notes.with_raw_response.fetch(
                "",
            )


class TestAsyncCreditNotes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.list()
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.credit_notes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.credit_notes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = await response.parse()
            assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.fetch(
            "credit_note_id",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.credit_notes.with_raw_response.fetch(
            "credit_note_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.credit_notes.with_streaming_response.fetch(
            "credit_note_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = await response.parse()
            assert_matches_type(CreditNote, credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_note_id` but received ''"):
            await async_client.credit_notes.with_raw_response.fetch(
                "",
            )
