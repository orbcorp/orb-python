# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.account import PaymentGatewayConnection

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentGatewayConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        payment_gateway_connection = client.account.payment_gateway_connections.list()
        assert_matches_type(SyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        payment_gateway_connection = client.account.payment_gateway_connections.list(
            billing_entity_id="billing_entity_id",
            cursor="cursor",
            limit=1,
            provider_type="stripe",
        )
        assert_matches_type(SyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.account.payment_gateway_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(SyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.account.payment_gateway_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(SyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        payment_gateway_connection = client.account.payment_gateway_connections.fetch(
            "payment_gateway_connection_id",
        )
        assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.account.payment_gateway_connections.with_raw_response.fetch(
            "payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.account.payment_gateway_connections.with_streaming_response.fetch(
            "payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = response.parse()
            assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            client.account.payment_gateway_connections.with_raw_response.fetch(
                "",
            )


class TestAsyncPaymentGatewayConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.account.payment_gateway_connections.list()
        assert_matches_type(AsyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.account.payment_gateway_connections.list(
            billing_entity_id="billing_entity_id",
            cursor="cursor",
            limit=1,
            provider_type="stripe",
        )
        assert_matches_type(AsyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.payment_gateway_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(AsyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.account.payment_gateway_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(AsyncPage[PaymentGatewayConnection], payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        payment_gateway_connection = await async_client.account.payment_gateway_connections.fetch(
            "payment_gateway_connection_id",
        )
        assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.payment_gateway_connections.with_raw_response.fetch(
            "payment_gateway_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway_connection = response.parse()
        assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.account.payment_gateway_connections.with_streaming_response.fetch(
            "payment_gateway_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway_connection = await response.parse()
            assert_matches_type(PaymentGatewayConnection, payment_gateway_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `payment_gateway_connection_id` but received ''"
        ):
            await async_client.account.payment_gateway_connections.with_raw_response.fetch(
                "",
            )
