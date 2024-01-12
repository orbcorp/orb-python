# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.beta import PriceEvaluateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPrice:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_evaluate(self, client: Orb) -> None:
        price = client.beta.price.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: Orb) -> None:
        price = client.beta.price.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="string",
            external_customer_id="string",
            filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            grouping_keys=["case when my_event_type = 'foo' then true else false end"],
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: Orb) -> None:
        response = client.beta.price.with_raw_response.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])


class TestAsyncPrice:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_evaluate(self, client: AsyncOrb) -> None:
        price = await client.beta.price.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, client: AsyncOrb) -> None:
        price = await client.beta.price.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="string",
            external_customer_id="string",
            filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            grouping_keys=["case when my_event_type = 'foo' then true else false end"],
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, client: AsyncOrb) -> None:
        response = await client.beta.price.with_raw_response.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])
