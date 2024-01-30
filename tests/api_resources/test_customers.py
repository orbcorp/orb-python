# File generated from our OpenAPI spec by Stainless.

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
                "country": "AD",
                "type": "ad_nrt",
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.customers.with_streaming_response.create(
            email="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            external_customer_id="string",
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
                "country": "AD",
                "type": "ad_nrt",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.customers.with_streaming_response.update(
            "string",
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
                "",
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
            cursor="string",
            limit=0,
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
            "string",
        )
        assert customer is None

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.customers.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_delete(self, client: Orb) -> None:
        with client.customers.with_streaming_response.delete(
            "string",
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
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.customers.with_streaming_response.fetch(
            "string",
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
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_fetch_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.fetch_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_fetch_by_external_id(self, client: Orb) -> None:
        with client.customers.with_streaming_response.fetch_by_external_id(
            "string",
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
            external_customer_id="string",
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
                "country": "AD",
                "type": "ad_nrt",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.customers.with_raw_response.update_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_update_by_external_id(self, client: Orb) -> None:
        with client.customers.with_streaming_response.update_by_external_id(
            "string",
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
                "",
                external_customer_id="",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.create(
            email="string",
            name="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.create(
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
                "country": "AD",
                "type": "ad_nrt",
                "value": "string",
            },
            timezone="string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.create(
            email="string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.create(
            email="string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update(
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
            external_customer_id="string",
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
                "country": "AD",
                "type": "ad_nrt",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.update(
            "string",
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
                "",
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
            cursor="string",
            limit=0,
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
            "string",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.delete(
            "string",
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
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.fetch(
            "string",
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
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.fetch_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.fetch_by_external_id(
            "string",
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
    async def test_method_update_by_external_id(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update_by_external_id(
            "string",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        customer = await async_client.customers.update_by_external_id(
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
            external_customer_id="string",
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
                "country": "AD",
                "type": "ad_nrt",
                "value": "string",
            },
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.with_raw_response.update_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.with_streaming_response.update_by_external_id(
            "string",
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
                "",
                external_customer_id="",
            )
