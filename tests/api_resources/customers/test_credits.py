# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers import (
    CreditListResponse,
    CreditListByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        credit = client.customers.credits.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        credit = client.customers.credits.list(
            customer_id="customer_id",
            currency="currency",
            cursor="cursor",
            include_all_blocks=True,
            limit=1,
        )
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.credits.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.credits.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        credit = client.customers.credits.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        credit = client.customers.credits.list_by_external_id(
            external_customer_id="external_customer_id",
            currency="currency",
            cursor="cursor",
            include_all_blocks=True,
            limit=1,
        )
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.with_raw_response.list_by_external_id(
                external_customer_id="",
            )


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        credit = await async_client.customers.credits.list(
            customer_id="customer_id",
        )
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        credit = await async_client.customers.credits.list(
            customer_id="customer_id",
            currency="currency",
            cursor="cursor",
            include_all_blocks=True,
            limit=1,
        )
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_list_by_external_id(self, async_client: AsyncOrb) -> None:
        credit = await async_client.customers.credits.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        credit = await async_client.customers.credits.list_by_external_id(
            external_customer_id="external_customer_id",
            currency="currency",
            cursor="cursor",
            include_all_blocks=True,
            limit=1,
        )
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.with_raw_response.list_by_external_id(
                external_customer_id="",
            )
