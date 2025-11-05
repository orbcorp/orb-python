# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    InvoiceFetchUpcomingResponse,
)
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.shared import Invoice

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        invoice = client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {
                        "unit_amount": "unit_amount",
                        "prorated": True,
                    },
                }
            ],
            customer_id="4khy3nwzktxv7",
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0.15,
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "filters": [
                    {
                        "field": "price_id",
                        "operator": "includes",
                        "values": ["string"],
                    }
                ],
                "reason": "reason",
            },
            due_date=parse_date("2023-09-22"),
            external_customer_id="external-customer-id",
            memo="An optional memo for my invoice.",
            metadata={"foo": "string"},
            net_terms=0,
            will_auto_issue=False,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        invoice = client.invoices.update(
            invoice_id="invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.update(
            invoice_id="invoice_id",
            due_date=parse_date("2023-09-22"),
            invoice_date=parse_date("2023-09-22"),
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.update(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.update(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.update(
                invoice_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.list(
            amount="amount",
            amount_gt="amount[gt]",
            amount_lt="amount[lt]",
            cursor="cursor",
            customer_id="customer_id",
            date_type="due_date",
            due_date=parse_date("2019-12-27"),
            due_date_window="due_date_window",
            due_date_gt=parse_date("2019-12-27"),
            due_date_lt=parse_date("2019-12-27"),
            external_customer_id="external_customer_id",
            invoice_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_recurring=True,
            limit=1,
            status=["draft"],
            subscription_id="subscription_id",
        )
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        invoice = client.invoices.fetch(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.fetch(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.fetch(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_upcoming(self, client: Orb) -> None:
        invoice = client.invoices.fetch_upcoming(
            subscription_id="subscription_id",
        )
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_fetch_upcoming(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.fetch_upcoming(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_fetch_upcoming(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.fetch_upcoming(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_issue(self, client: Orb) -> None:
        invoice = client.invoices.issue(
            invoice_id="invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_issue_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.issue(
            invoice_id="invoice_id",
            synchronous=True,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_issue(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.issue(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_issue(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.issue(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_issue(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.issue(
                invoice_id="",
            )

    @parametrize
    def test_method_mark_paid(self, client: Orb) -> None:
        invoice = client.invoices.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_mark_paid_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
            external_id="external_payment_id_123",
            notes="notes",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_mark_paid(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_mark_paid(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mark_paid(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.mark_paid(
                invoice_id="",
                payment_received_date=parse_date("2023-09-22"),
            )

    @parametrize
    def test_method_pay(self, client: Orb) -> None:
        invoice = client.invoices.pay(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_pay(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.pay(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_pay(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.pay(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pay(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.pay(
                "",
            )

    @parametrize
    def test_method_void(self, client: Orb) -> None:
        invoice = client.invoices.void(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.void(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.void(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_void(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.void(
                "",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {
                        "unit_amount": "unit_amount",
                        "prorated": True,
                    },
                }
            ],
            customer_id="4khy3nwzktxv7",
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0.15,
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "filters": [
                    {
                        "field": "price_id",
                        "operator": "includes",
                        "values": ["string"],
                    }
                ],
                "reason": "reason",
            },
            due_date=parse_date("2023-09-22"),
            external_customer_id="external-customer-id",
            memo="An optional memo for my invoice.",
            metadata={"foo": "string"},
            net_terms=0,
            will_auto_issue=False,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "end_date": parse_date("2023-09-22"),
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "name": "Line Item Name",
                    "quantity": 1,
                    "start_date": parse_date("2023-09-22"),
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.update(
            invoice_id="invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.update(
            invoice_id="invoice_id",
            due_date=parse_date("2023-09-22"),
            invoice_date=parse_date("2023-09-22"),
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.update(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.update(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.update(
                invoice_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.list(
            amount="amount",
            amount_gt="amount[gt]",
            amount_lt="amount[lt]",
            cursor="cursor",
            customer_id="customer_id",
            date_type="due_date",
            due_date=parse_date("2019-12-27"),
            due_date_window="due_date_window",
            due_date_gt=parse_date("2019-12-27"),
            due_date_lt=parse_date("2019-12-27"),
            external_customer_id="external_customer_id",
            invoice_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_recurring=True,
            limit=1,
            status=["draft"],
            subscription_id="subscription_id",
        )
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.fetch(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.fetch(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.fetch(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_upcoming(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.fetch_upcoming(
            subscription_id="subscription_id",
        )
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_fetch_upcoming(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.fetch_upcoming(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_upcoming(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.fetch_upcoming(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_issue(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.issue(
            invoice_id="invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_issue_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.issue(
            invoice_id="invoice_id",
            synchronous=True,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_issue(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.issue(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_issue(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.issue(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_issue(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.issue(
                invoice_id="",
            )

    @parametrize
    async def test_method_mark_paid(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_mark_paid_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
            external_id="external_payment_id_123",
            notes="notes",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_mark_paid(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_mark_paid(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.mark_paid(
            invoice_id="invoice_id",
            payment_received_date=parse_date("2023-09-22"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mark_paid(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.mark_paid(
                invoice_id="",
                payment_received_date=parse_date("2023-09-22"),
            )

    @parametrize
    async def test_method_pay(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.pay(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_pay(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.pay(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_pay(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.pay(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pay(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.pay(
                "",
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.void(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.void(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.void(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_void(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.void(
                "",
            )
