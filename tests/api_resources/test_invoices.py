# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Invoice,
    InvoiceFetchUpcomingResponse,
)
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

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
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
            customer_id="4khy3nwzktxv7",
            external_customer_id="external-customer-id",
            memo="An optional memo for my invoice.",
            metadata={"foo": "string"},
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
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
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
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.list(
            amount="string",
            amount_gt="string",
            amount_lt="string",
            cursor="string",
            customer_id="string",
            date_type="due_date",
            due_date=parse_date("2019-12-27"),
            due_date_window="string",
            due_date_gt=parse_date("2019-12-27"),
            due_date_lt=parse_date("2019-12-27"),
            external_customer_id="string",
            invoice_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_recurring=True,
            limit=1,
            status=["draft", "issued", "paid"],
            subscription_id="string",
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
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.fetch(
            "string",
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
        invoice = client.invoices.fetch_upcoming()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    def test_method_fetch_upcoming_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.fetch_upcoming(
            subscription_id="string",
        )
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_fetch_upcoming(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.fetch_upcoming()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_fetch_upcoming(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.fetch_upcoming() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_issue(self, client: Orb) -> None:
        invoice = client.invoices.issue(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_issue(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.issue(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_issue(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.issue(
            "string",
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
                "",
            )

    @parametrize
    def test_method_mark_paid(self, client: Orb) -> None:
        invoice = client.invoices.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_mark_paid_with_all_params(self, client: Orb) -> None:
        invoice = client.invoices.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
            external_id="external_payment_id_123",
            notes="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_mark_paid(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_mark_paid(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.mark_paid(
            "string",
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
                "",
                payment_received_date=parse_date("2023-09-22"),
            )

    @parametrize
    def test_method_void(self, client: Orb) -> None:
        invoice = client.invoices.void(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Orb) -> None:
        response = client.invoices.with_raw_response.void(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Orb) -> None:
        with client.invoices.with_streaming_response.void(
            "string",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.create(
            currency="USD",
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
            customer_id="4khy3nwzktxv7",
            external_customer_id="external-customer-id",
            memo="An optional memo for my invoice.",
            metadata={"foo": "string"},
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
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
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
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "start_date": parse_date("2023-09-22"),
                    "end_date": parse_date("2023-09-22"),
                    "quantity": 1,
                    "name": "Line Item Name",
                    "item_id": "4khy3nwzktxv7",
                    "model_type": "unit",
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            net_terms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(AsyncPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.list(
            amount="string",
            amount_gt="string",
            amount_lt="string",
            cursor="string",
            customer_id="string",
            date_type="due_date",
            due_date=parse_date("2019-12-27"),
            due_date_window="string",
            due_date_gt=parse_date("2019-12-27"),
            due_date_lt=parse_date("2019-12-27"),
            external_customer_id="string",
            invoice_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            invoice_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_recurring=True,
            limit=1,
            status=["draft", "issued", "paid"],
            subscription_id="string",
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
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.fetch(
            "string",
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
        invoice = await async_client.invoices.fetch_upcoming()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    async def test_method_fetch_upcoming_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.fetch_upcoming(
            subscription_id="string",
        )
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_fetch_upcoming(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.fetch_upcoming()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_upcoming(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.fetch_upcoming() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceFetchUpcomingResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_issue(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.issue(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_issue(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.issue(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_issue(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.issue(
            "string",
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
                "",
            )

    @parametrize
    async def test_method_mark_paid(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_mark_paid_with_all_params(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
            external_id="external_payment_id_123",
            notes="string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_mark_paid(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.mark_paid(
            "string",
            payment_received_date=parse_date("2023-09-22"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_mark_paid(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.mark_paid(
            "string",
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
                "",
                payment_received_date=parse_date("2023-09-22"),
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncOrb) -> None:
        invoice = await async_client.invoices.void(
            "string",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncOrb) -> None:
        response = await async_client.invoices.with_raw_response.void(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncOrb) -> None:
        async with async_client.invoices.with_streaming_response.void(
            "string",
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
