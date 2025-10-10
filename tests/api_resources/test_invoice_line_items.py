# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import InvoiceLineItemCreateResponse
from orb._utils import parse_date
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoiceLineItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        invoice_line_item = client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        invoice_line_item = client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
            item_id="4khy3nwzktxv7",
            name="Item Name",
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.invoice_line_items.with_raw_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice_line_item = response.parse()
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.invoice_line_items.with_streaming_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice_line_item = response.parse()
            assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoiceLineItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        invoice_line_item = await async_client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice_line_item = await async_client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
            item_id="4khy3nwzktxv7",
            name="Item Name",
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoice_line_items.with_raw_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice_line_item = response.parse()
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.invoice_line_items.with_streaming_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice_line_item = await response.parse()
            assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

        assert cast(Any, response.is_closed) is True
