# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers import (
    CreditListResponse,
    CreditListByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCredits:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        credit = client.customers.credits.list(
            "string",
        )
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        credit = client.customers.credits.list(
            "string",
            currency="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.credits.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.credits.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncPage[CreditListResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        credit = client.customers.credits.list_by_external_id(
            "string",
        )
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        credit = client.customers.credits.list_by_external_id(
            "string",
            currency="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.with_raw_response.list_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.with_streaming_response.list_by_external_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncPage[CreditListByExternalIDResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        credit = await client.customers.credits.list(
            "string",
        )
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        credit = await client.customers.credits.list(
            "string",
            currency="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.customers.credits.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncOrb) -> None:
        async with client.customers.credits.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncPage[CreditListResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_by_external_id(self, client: AsyncOrb) -> None:
        credit = await client.customers.credits.list_by_external_id(
            "string",
        )
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, client: AsyncOrb) -> None:
        credit = await client.customers.credits.list_by_external_id(
            "string",
            currency="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, client: AsyncOrb) -> None:
        response = await client.customers.credits.with_raw_response.list_by_external_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_external_id(self, client: AsyncOrb) -> None:
        async with client.customers.credits.with_streaming_response.list_by_external_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncPage[CreditListByExternalIDResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True
