# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.types.beta.price_evaluate_response import PriceEvaluateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: Orb) -> None:
        with client.beta.price.with_streaming_response.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceEvaluateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            client.beta.price.with_raw_response.evaluate(
                "",
                timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
                timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncPrice:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncOrb) -> None:
        price = await async_client.beta.price.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.beta.price.evaluate(
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
    async def test_raw_response_evaluate(self, async_client: AsyncOrb) -> None:
        response = await async_client.beta.price.with_raw_response.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncOrb) -> None:
        async with async_client.beta.price.with_streaming_response.evaluate(
            "string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceEvaluateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            await async_client.beta.price.with_raw_response.evaluate(
                "",
                timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
                timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
