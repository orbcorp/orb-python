# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    EventIngestResponse,
    EventSearchResponse,
    EventUpdateResponse,
    EventDeprecateResponse,
)
from orb._utils import parse_datetime
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestEvents:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        event = client.events.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        event = client.events.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
            customer_id="string",
            external_customer_id="string",
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.events.with_raw_response.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.events.with_streaming_response.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventUpdateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.events.with_raw_response.update(
                "",
                event_name="string",
                properties={},
                timestamp=parse_datetime("2020-12-09T16:09:53Z"),
            )

    @parametrize
    def test_method_deprecate(self, client: Orb) -> None:
        event = client.events.deprecate(
            "string",
        )
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

    @parametrize
    def test_raw_response_deprecate(self, client: Orb) -> None:
        response = client.events.with_raw_response.deprecate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_deprecate(self, client: Orb) -> None:
        with client.events.with_streaming_response.deprecate(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventDeprecateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deprecate(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.events.with_raw_response.deprecate(
                "",
            )

    @parametrize
    def test_method_ingest(self, client: Orb) -> None:
        event = client.events.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    def test_method_ingest_with_all_params(self, client: Orb) -> None:
        event = client.events.ingest(
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
            backfill_id="string",
            debug=True,
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    def test_raw_response_ingest(self, client: Orb) -> None:
        response = client.events.with_raw_response.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_ingest(self, client: Orb) -> None:
        with client.events.with_streaming_response.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventIngestResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Orb) -> None:
        event = client.events.search(
            event_ids=["string"],
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Orb) -> None:
        event = client.events.search(
            event_ids=["string"],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Orb) -> None:
        response = client.events.with_raw_response.search(
            event_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Orb) -> None:
        with client.events.with_streaming_response.search(
            event_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventSearchResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncOrb) -> None:
        event = await client.events.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncOrb) -> None:
        event = await client.events.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
            customer_id="string",
            external_customer_id="string",
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncOrb) -> None:
        response = await client.events.with_raw_response.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncOrb) -> None:
        async with client.events.with_streaming_response.update(
            "string",
            event_name="string",
            properties={},
            timestamp=parse_datetime("2020-12-09T16:09:53Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventUpdateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await client.events.with_raw_response.update(
                "",
                event_name="string",
                properties={},
                timestamp=parse_datetime("2020-12-09T16:09:53Z"),
            )

    @parametrize
    async def test_method_deprecate(self, client: AsyncOrb) -> None:
        event = await client.events.deprecate(
            "string",
        )
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_deprecate(self, client: AsyncOrb) -> None:
        response = await client.events.with_raw_response.deprecate(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_deprecate(self, client: AsyncOrb) -> None:
        async with client.events.with_streaming_response.deprecate(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventDeprecateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deprecate(self, client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await client.events.with_raw_response.deprecate(
                "",
            )

    @parametrize
    async def test_method_ingest(self, client: AsyncOrb) -> None:
        event = await client.events.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    async def test_method_ingest_with_all_params(self, client: AsyncOrb) -> None:
        event = await client.events.ingest(
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
            backfill_id="string",
            debug=True,
        )
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_ingest(self, client: AsyncOrb) -> None:
        response = await client.events.with_raw_response.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_ingest(self, client: AsyncOrb) -> None:
        async with client.events.with_streaming_response.ingest(
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                    "idempotency_key": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventIngestResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, client: AsyncOrb) -> None:
        event = await client.events.search(
            event_ids=["string"],
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, client: AsyncOrb) -> None:
        event = await client.events.search(
            event_ids=["string"],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_search(self, client: AsyncOrb) -> None:
        response = await client.events.with_raw_response.search(
            event_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, client: AsyncOrb) -> None:
        async with client.events.with_streaming_response.search(
            event_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventSearchResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
