# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    def test_method_search(self, client: Orb) -> None:
        event = client.events.search(
            event_ids=["string", "string", "string"],
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Orb) -> None:
        response = client.events.with_raw_response.search(
            event_ids=["string", "string", "string"],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventSearchResponse, event, path=["response"])


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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeprecateResponse, event, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=["response"])

    @parametrize
    async def test_method_search(self, client: AsyncOrb) -> None:
        event = await client.events.search(
            event_ids=["string", "string", "string"],
        )
        assert_matches_type(EventSearchResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_search(self, client: AsyncOrb) -> None:
        response = await client.events.with_raw_response.search(
            event_ids=["string", "string", "string"],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventSearchResponse, event, path=["response"])
