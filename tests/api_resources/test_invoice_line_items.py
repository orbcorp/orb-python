# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from orb import Orb, AsyncOrb

from orb.types import InvoiceLineItemCreateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types import invoice_line_item_create_params
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date
from orb._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoiceLineItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        invoice_line_item = client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            name="Item Name",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.invoice_line_items.with_raw_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            name="Item Name",
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
            name="Item Name",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice_line_item = response.parse()
            assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoiceLineItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        invoice_line_item = await async_client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            name="Item Name",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoice_line_items.with_raw_response.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            name="Item Name",
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
            name="Item Name",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice_line_item = await response.parse()
            assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])

        assert cast(Any, response.is_closed) is True
