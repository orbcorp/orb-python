# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.metric_list_response import MetricListResponse
from orb.types.metric_fetch_response import MetricFetchResponse
from orb.types.metric_create_response import MetricCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        metric = client.metrics.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        metric = client.metrics.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
            metadata={"foo": "string"},
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.metrics.with_raw_response.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.metrics.with_streaming_response.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        metric = client.metrics.list()
        assert_matches_type(SyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        metric = client.metrics.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(SyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(SyncPage[MetricListResponse], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        metric = client.metrics.fetch(
            "string",
        )
        assert_matches_type(MetricFetchResponse, metric, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.metrics.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricFetchResponse, metric, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.metrics.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricFetchResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            client.metrics.with_raw_response.fetch(
                "",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        metric = await async_client.metrics.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        metric = await async_client.metrics.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
            metadata={"foo": "string"},
        )
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.metrics.with_raw_response.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricCreateResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.metrics.with_streaming_response.create(
            description="Sum of bytes downloaded in fast mode",
            item_id="string",
            name="Bytes downloaded",
            sql="SELECT sum(bytes_downloaded) FROM events WHERE download_speed = 'fast'",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        metric = await async_client.metrics.list()
        assert_matches_type(AsyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        metric = await async_client.metrics.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(AsyncPage[MetricListResponse], metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AsyncPage[MetricListResponse], metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        metric = await async_client.metrics.fetch(
            "string",
        )
        assert_matches_type(MetricFetchResponse, metric, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.metrics.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricFetchResponse, metric, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.metrics.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricFetchResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metric_id` but received ''"):
            await async_client.metrics.with_raw_response.fetch(
                "",
            )
