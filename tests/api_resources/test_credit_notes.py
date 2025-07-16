# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.shared import CreditNote

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        credit_note = client.credit_notes.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        credit_note = client.credit_notes.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                    "end_date": parse_date("2023-09-22"),
                    "start_date": parse_date("2023-09-22"),
                }
            ],
            reason="duplicate",
            end_date=parse_date("2023-09-22"),
            memo="An optional memo for my credit note.",
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.credit_notes.with_raw_response.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.credit_notes.with_streaming_response.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = response.parse()
            assert_matches_type(CreditNote, credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        credit_note = client.credit_notes.list()
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        credit_note = client.credit_notes.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                    "end_date": parse_date("2023-09-22"),
                    "start_date": parse_date("2023-09-22"),
                }
            ],
            reason="duplicate",
            end_date=parse_date("2023-09-22"),
            memo="An optional memo for my credit note.",
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.credit_notes.with_raw_response.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_note = response.parse()
        assert_matches_type(CreditNote, credit_note, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.credit_notes.with_streaming_response.create(
            line_items=[
                {
                    "amount": "amount",
                    "invoice_line_item_id": "4khy3nwzktxv7",
                }
            ],
            reason="duplicate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_note = await response.parse()
            assert_matches_type(CreditNote, credit_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.list()
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        credit_note = await async_client.credit_notes.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
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
