# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.customers import (
    CustomerPaymentGatewayConnection,
    PaymentGatewayConnectionListResponse,
    PaymentGatewayConnectionListByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentGatewayConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.create(
                customer_id="",
                payment_gateway_connection_id="payment_gateway_connection_id",
            )

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.update(
                payment_gateway_connection_id="payment_gateway_connection_id",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            client.customers.payment_gateway_connections.with_raw_response.update(
                payment_gateway_connection_id="",
                customer_id="customer_id",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.list(
            customer_id="customer_id",
        )
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.list(
            customer_id="customer_id",
            billing_entity_id="billing_entity_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_delete(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.delete(
                payment_gateway_connection_id="payment_gateway_connection_id",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            client.customers.payment_gateway_connections.with_raw_response.delete(
                payment_gateway_connection_id="",
                customer_id="customer_id",
            )

    @parametrize
    def test_method_create_by_external_id(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_create_by_external_id_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_create_by_external_id(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_create_by_external_id(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.create_by_external_id(
                external_customer_id="",
                payment_gateway_connection_id="payment_gateway_connection_id",
            )

    @parametrize
    def test_method_delete_by_external_id(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_delete_by_external_id(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_external_id(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
                payment_gateway_connection_id="payment_gateway_connection_id",
                external_customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
                payment_gateway_connection_id="",
                external_customer_id="external_customer_id",
            )

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.list_by_external_id(
            external_customer_id="external_customer_id",
            billing_entity_id="billing_entity_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(
                PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.list_by_external_id(
                external_customer_id="",
            )

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.customers.payment_gateway_connections.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_update_by_external_id(self, client: Orb) -> None:
        with client.customers.payment_gateway_connections.with_streaming_response.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
                payment_gateway_connection_id="payment_gateway_connection_id",
                external_customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
                payment_gateway_connection_id="",
                external_customer_id="external_customer_id",
            )


class TestAsyncPaymentGatewayConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.create(
            customer_id="customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.create(
                customer_id="",
                payment_gateway_connection_id="payment_gateway_connection_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.update(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.update(
                payment_gateway_connection_id="payment_gateway_connection_id",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            await async_client.customers.payment_gateway_connections.with_raw_response.update(
                payment_gateway_connection_id="",
                customer_id="customer_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.list(
            customer_id="customer_id",
        )
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.list(
            customer_id="customer_id",
            billing_entity_id="billing_entity_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(PaymentGatewayConnectionListResponse, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.delete(
            payment_gateway_connection_id="payment_gateway_connection_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.delete(
                payment_gateway_connection_id="payment_gateway_connection_id",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            await async_client.customers.payment_gateway_connections.with_raw_response.delete(
                payment_gateway_connection_id="",
                customer_id="customer_id",
            )

    @parametrize
    async def test_method_create_by_external_id(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_create_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_create_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_create_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.create_by_external_id(
            external_customer_id="external_customer_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.create_by_external_id(
                external_customer_id="",
                payment_gateway_connection_id="payment_gateway_connection_id",
            )

    @parametrize
    async def test_method_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.delete_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
                payment_gateway_connection_id="payment_gateway_connection_id",
                external_customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            await async_client.customers.payment_gateway_connections.with_raw_response.delete_by_external_id(
                payment_gateway_connection_id="",
                external_customer_id="external_customer_id",
            )

    @parametrize
    async def test_method_list_by_external_id(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.list_by_external_id(
            external_customer_id="external_customer_id",
            billing_entity_id="billing_entity_id",
            payment_gateway_connection_id="payment_gateway_connection_id",
        )
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    async def test_raw_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(
            PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(
                PaymentGatewayConnectionListByExternalIDResponse, payment_gateway_connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.list_by_external_id(
                external_customer_id="",
            )

    @parametrize
    async def test_method_update_by_external_id(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.customers.payment_gateway_connections.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
            is_default=True,
            provider_customer_id="x",
        )
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.payment_gateway_connections.with_streaming_response.update_by_external_id(
            payment_gateway_connection_id="payment_gateway_connection_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(CustomerPaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
                payment_gateway_connection_id="payment_gateway_connection_id",
                external_customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            await async_client.customers.payment_gateway_connections.with_raw_response.update_by_external_id(
                payment_gateway_connection_id="",
                external_customer_id="external_customer_id",
            )
