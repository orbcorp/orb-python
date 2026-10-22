# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    WebhookEndpoint,
    WebhookEndpointWithSecret,
)
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.create(
            url="url",
        )
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.create(
            url="url",
            enabled_event_types=["string"],
            payload_style="expanded",
        )
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.retrieve(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.retrieve(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.retrieve(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            client.webhook_endpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.update(
            webhook_endpoint_id="webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.update(
            webhook_endpoint_id="webhook_endpoint_id",
            enabled_event_types=["string"],
            payload_style="expanded",
            url="url",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.update(
            webhook_endpoint_id="webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.update(
            webhook_endpoint_id="webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            client.webhook_endpoints.with_raw_response.update(
                webhook_endpoint_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.list()
        assert_matches_type(SyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(SyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(SyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.delete(
            "webhook_endpoint_id",
        )
        assert webhook_endpoint is None

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.delete(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert webhook_endpoint is None

    @parametrize
    def test_streaming_response_delete(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.delete(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert webhook_endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            client.webhook_endpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_disable(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.disable(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.disable(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.disable(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            client.webhook_endpoints.with_raw_response.disable(
                "",
            )

    @parametrize
    def test_method_enable(self, client: Orb) -> None:
        webhook_endpoint = client.webhook_endpoints.enable(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Orb) -> None:
        response = client.webhook_endpoints.with_raw_response.enable(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Orb) -> None:
        with client.webhook_endpoints.with_streaming_response.enable(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            client.webhook_endpoints.with_raw_response.enable(
                "",
            )


class TestAsyncWebhookEndpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.create(
            url="url",
        )
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.create(
            url="url",
            enabled_event_types=["string"],
            payload_style="expanded",
        )
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(WebhookEndpointWithSecret, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.retrieve(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.retrieve(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.retrieve(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            await async_client.webhook_endpoints.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.update(
            webhook_endpoint_id="webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.update(
            webhook_endpoint_id="webhook_endpoint_id",
            enabled_event_types=["string"],
            payload_style="expanded",
            url="url",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.update(
            webhook_endpoint_id="webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.update(
            webhook_endpoint_id="webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            await async_client.webhook_endpoints.with_raw_response.update(
                webhook_endpoint_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.list()
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(AsyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(AsyncPage[WebhookEndpoint], webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.delete(
            "webhook_endpoint_id",
        )
        assert webhook_endpoint is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.delete(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert webhook_endpoint is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.delete(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert webhook_endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            await async_client.webhook_endpoints.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.disable(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.disable(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.disable(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            await async_client.webhook_endpoints.with_raw_response.disable(
                "",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncOrb) -> None:
        webhook_endpoint = await async_client.webhook_endpoints.enable(
            "webhook_endpoint_id",
        )
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncOrb) -> None:
        response = await async_client.webhook_endpoints.with_raw_response.enable(
            "webhook_endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_endpoint = response.parse()
        assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncOrb) -> None:
        async with async_client.webhook_endpoints.with_streaming_response.enable(
            "webhook_endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_endpoint = await response.parse()
            assert_matches_type(WebhookEndpoint, webhook_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_endpoint_id` but received ''"):
            await async_client.webhook_endpoints.with_raw_response.enable(
                "",
            )
