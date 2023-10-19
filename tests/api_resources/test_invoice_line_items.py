# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import InvoiceLineItemCreateResponse
from orb._utils import parse_date
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInvoiceLineItems:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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


class TestAsyncInvoiceLineItems:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        invoice_line_item = await client.invoice_line_items.create(
            amount="12.00",
            end_date=parse_date("2023-09-22"),
            invoice_id="4khy3nwzktxv7",
            name="Item Name",
            quantity=1,
            start_date=parse_date("2023-09-22"),
        )
        assert_matches_type(InvoiceLineItemCreateResponse, invoice_line_item, path=["response"])
