# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Customer,
)
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        customer = client.customers.create(
            email="dev@stainless.com",
            name="x",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        customer = client.customers.create(
            email="dev@stainless.com",
            name="x",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["dev@stainless.com"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
            timezone="timezone",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.customers.with_raw_response.create(
            email="dev@stainless.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.customers.with_streaming_response.create(
            email="dev@stainless.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        customer = client.customers.update(
            customer_id="customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        customer = client.customers.update(
            customer_id="customer_id",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["string"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email="dev@stainless.com",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            name="name",
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.customers.with_streaming_response.update(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.update(
                customer_id="",
            )

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
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Customer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncPage[Customer], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Orb) -> None:
        customer = client.customers.delete(
            "customer_id",
        )
        assert customer is None

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.customers.with_raw_response.delete(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_delete(self, client: Orb) -> None:
        with client.customers.with_streaming_response.delete(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        customer = client.customers.fetch(
            "customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.customers.with_streaming_response.fetch(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_by_external_id(self, client: Orb) -> None:
        customer = client.customers.fetch_by_external_id(
            "external_customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch_by_external_id(
            "external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_fetch_by_external_id(self, client: Orb) -> None:
        with client.customers.with_streaming_response.fetch_by_external_id(
            "external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.with_raw_response.fetch_by_external_id(
                "",
            )

    @parametrize
    def test_method_sync_payment_methods_from_gateway(self, client: Orb) -> None:
        customer = client.customers.sync_payment_methods_from_gateway(
            "customer_id",
        )
        assert customer is None

    @parametrize
    def test_raw_response_sync_payment_methods_from_gateway(self, client: Orb) -> None:
        response = client.customers.with_raw_response.sync_payment_methods_from_gateway(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_sync_payment_methods_from_gateway(self, client: Orb) -> None:
        with client.customers.with_streaming_response.sync_payment_methods_from_gateway(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync_payment_methods_from_gateway(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.with_raw_response.sync_payment_methods_from_gateway(
                "",
            )

    @parametrize
    def test_method_sync_payment_methods_from_gateway_by_external_customer_id(self, client: Orb) -> None:
        customer = client.customers.sync_payment_methods_from_gateway_by_external_customer_id(
            "external_customer_id",
        )
        assert customer is None

    @parametrize
    def test_raw_response_sync_payment_methods_from_gateway_by_external_customer_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.sync_payment_methods_from_gateway_by_external_customer_id(
            "external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_sync_payment_methods_from_gateway_by_external_customer_id(self, client: Orb) -> None:
        with client.customers.with_streaming_response.sync_payment_methods_from_gateway_by_external_customer_id(
            "external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync_payment_methods_from_gateway_by_external_customer_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.with_raw_response.sync_payment_methods_from_gateway_by_external_customer_id(
                "",
            )

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        customer = client.customers.update_by_external_id(
            id="external_customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        customer = client.customers.update_by_external_id(
            id="external_customer_id",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["string"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email="dev@stainless.com",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            name="name",
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update_by_external_id(
            id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_update_by_external_id(self, client: Orb) -> None:
        with client.customers.with_streaming_response.update_by_external_id(
            id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.update_by_external_id(
                id="",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.create(
            email="dev@stainless.com",
            name="x",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.create(
            email="dev@stainless.com",
            name="x",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["dev@stainless.com"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
            timezone="timezone",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.create(
            email="dev@stainless.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.create(
            email="dev@stainless.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update(
            customer_id="customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update(
            customer_id="customer_id",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["string"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email="dev@stainless.com",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            name="name",
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.update(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.update(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.update(
                customer_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.list()
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(AsyncPage[Customer], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.delete(
            "customer_id",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.delete(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.delete(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.fetch(
            "customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.fetch(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.fetch(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.fetch_by_external_id(
            "external_customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.fetch_by_external_id(
            "external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.fetch_by_external_id(
            "external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.with_raw_response.fetch_by_external_id(
                "",
            )

    @parametrize
    async def test_method_sync_payment_methods_from_gateway(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.sync_payment_methods_from_gateway(
            "customer_id",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_sync_payment_methods_from_gateway(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.sync_payment_methods_from_gateway(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_sync_payment_methods_from_gateway(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.sync_payment_methods_from_gateway(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync_payment_methods_from_gateway(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.with_raw_response.sync_payment_methods_from_gateway(
                "",
            )

    @parametrize
    async def test_method_sync_payment_methods_from_gateway_by_external_customer_id(
        self, async_client: AsyncOrb
    ) -> None:
        customer = await async_client.customers.sync_payment_methods_from_gateway_by_external_customer_id(
            "external_customer_id",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_sync_payment_methods_from_gateway_by_external_customer_id(
        self, async_client: AsyncOrb
    ) -> None:
        response = (
            await async_client.customers.with_raw_response.sync_payment_methods_from_gateway_by_external_customer_id(
                "external_customer_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_sync_payment_methods_from_gateway_by_external_customer_id(
        self, async_client: AsyncOrb
    ) -> None:
        async with (
            async_client.customers.with_streaming_response.sync_payment_methods_from_gateway_by_external_customer_id(
                "external_customer_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync_payment_methods_from_gateway_by_external_customer_id(
        self, async_client: AsyncOrb
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.with_raw_response.sync_payment_methods_from_gateway_by_external_customer_id(
                "",
            )

    @parametrize
    async def test_method_update_by_external_id(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update_by_external_id(
            id="external_customer_id",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update_by_external_id(
            id="external_customer_id",
            accounting_sync_configuration={
                "accounting_providers": [
                    {
                        "external_provider_id": "external_provider_id",
                        "provider_type": "provider_type",
                    }
                ],
                "excluded": True,
            },
            additional_emails=["string"],
            auto_collection=True,
            auto_issuance=True,
            billing_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            currency="currency",
            email="dev@stainless.com",
            email_delivery=True,
            external_customer_id="external_customer_id",
            hierarchy={
                "child_customer_ids": ["string"],
                "parent_customer_id": "parent_customer_id",
            },
            metadata={"foo": "string"},
            name="name",
            payment_provider="quickbooks",
            payment_provider_id="payment_provider_id",
            reporting_configuration={"exempt": True},
            shipping_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            tax_configuration={
                "tax_exempt": True,
                "tax_provider": "avalara",
                "automatic_tax_enabled": True,
                "tax_exemption_code": "tax_exemption_code",
            },
            tax_id={
                "country": "AD",
                "type": "ad_nrt",
                "value": "value",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.update_by_external_id(
            id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.update_by_external_id(
            id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.update_by_external_id(
                id="",
            )
