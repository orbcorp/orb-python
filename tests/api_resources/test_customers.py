# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Customer,
)
from orb._utils import parse_datetime
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCustomers:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        customer = client.customers.create(
            email="string",
            name="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        customer = client.customers.create(
            email="string",
            name="string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string", "string", "string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email_delivery=True,
            external_customer_id="string",
            metadata={"foo": "string"},
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
            timezone="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.customers.with_raw_response.create(
            email="string",
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        customer = client.customers.update(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        customer = client.customers.update(
            "string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email="string",
            email_delivery=True,
            metadata={"foo": "string"},
            name="string",
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        customer = client.customers.list()
        assert_matches_type(SyncPage[Customer], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        customer = client.customers.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[Customer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncPage[Customer], customer, path=["response"])

    @parametrize
    def test_method_delete(self, client: Orb) -> None:
        customer = client.customers.delete(
            "string",
        )
        assert customer is None

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.customers.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        customer = client.customers.fetch(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_fetch_by_external_id(self, client: Orb) -> None:
        customer = client.customers.fetch_by_external_id(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        customer = client.customers.update_by_external_id(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        customer = client.customers.update_by_external_id(
            "string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email="string",
            email_delivery=True,
            metadata={"foo": "string"},
            name="string",
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])


class TestAsyncCustomers:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        customer = await client.customers.create(
            email="string",
            name="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        customer = await client.customers.create(
            email="string",
            name="string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string", "string", "string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email_delivery=True,
            external_customer_id="string",
            metadata={"foo": "string"},
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
            timezone="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.create(
            email="string",
            name="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncOrb) -> None:
        customer = await client.customers.update(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncOrb) -> None:
        customer = await client.customers.update(
            "string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email="string",
            email_delivery=True,
            metadata={"foo": "string"},
            name="string",
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        customer = await client.customers.list()
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        customer = await client.customers.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncOrb) -> None:
        customer = await client.customers.delete(
            "string",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        customer = await client.customers.fetch(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.fetch(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_fetch_by_external_id(self, client: AsyncOrb) -> None:
        customer = await client.customers.fetch_by_external_id(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch_by_external_id(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.fetch_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_by_external_id(self, client: AsyncOrb) -> None:
        customer = await client.customers.update_by_external_id(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, client: AsyncOrb) -> None:
        customer = await client.customers.update_by_external_id(
            "string",
            accounting_sync_configuration={
                "excluded": True,
                "accounting_providers": [
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                    {
                        "provider_type": "string",
                        "external_provider_id": "string",
                    },
                ],
            },
            additional_emails=["string"],
            auto_collection=True,
            billing_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            currency="string",
            email="string",
            email_delivery=True,
            metadata={"foo": "string"},
            name="string",
            payment_provider="quickbooks",
            payment_provider_id="string",
            reporting_configuration={"exempt": True},
            shipping_address={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
            tax_id={
                "country": "AE",
                "type": "ae_trn",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, client: AsyncOrb) -> None:
        response = await client.customers.with_raw_response.update_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])
