# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    SubscriptionChangeApplyResponse,
    SubscriptionChangeCancelResponse,
    SubscriptionChangeRetrieveResponse,
)
from orb._utils import parse_date
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptionChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        subscription_change = client.subscription_changes.retrieve(
            "subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.subscription_changes.with_raw_response.retrieve(
            "subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.subscription_changes.with_streaming_response.retrieve(
            "subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = response.parse()
            assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            client.subscription_changes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_apply(self, client: Orb) -> None:
        subscription_change = client.subscription_changes.apply(
            subscription_change_id="subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Orb) -> None:
        subscription_change = client.subscription_changes.apply(
            subscription_change_id="subscription_change_id",
            description="description",
            mark_as_paid=True,
            payment_external_id="payment_external_id",
            payment_notes="payment_notes",
            payment_received_date=parse_date("2019-12-27"),
            previously_collected_amount="previously_collected_amount",
        )
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Orb) -> None:
        response = client.subscription_changes.with_raw_response.apply(
            subscription_change_id="subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Orb) -> None:
        with client.subscription_changes.with_streaming_response.apply(
            subscription_change_id="subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = response.parse()
            assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            client.subscription_changes.with_raw_response.apply(
                subscription_change_id="",
            )

    @parametrize
    def test_method_cancel(self, client: Orb) -> None:
        subscription_change = client.subscription_changes.cancel(
            "subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Orb) -> None:
        response = client.subscription_changes.with_raw_response.cancel(
            "subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Orb) -> None:
        with client.subscription_changes.with_streaming_response.cancel(
            "subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = response.parse()
            assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            client.subscription_changes.with_raw_response.cancel(
                "",
            )


class TestAsyncSubscriptionChanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        subscription_change = await async_client.subscription_changes.retrieve(
            "subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscription_changes.with_raw_response.retrieve(
            "subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.subscription_changes.with_streaming_response.retrieve(
            "subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = await response.parse()
            assert_matches_type(SubscriptionChangeRetrieveResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            await async_client.subscription_changes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_apply(self, async_client: AsyncOrb) -> None:
        subscription_change = await async_client.subscription_changes.apply(
            subscription_change_id="subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription_change = await async_client.subscription_changes.apply(
            subscription_change_id="subscription_change_id",
            description="description",
            mark_as_paid=True,
            payment_external_id="payment_external_id",
            payment_notes="payment_notes",
            payment_received_date=parse_date("2019-12-27"),
            previously_collected_amount="previously_collected_amount",
        )
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscription_changes.with_raw_response.apply(
            subscription_change_id="subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncOrb) -> None:
        async with async_client.subscription_changes.with_streaming_response.apply(
            subscription_change_id="subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = await response.parse()
            assert_matches_type(SubscriptionChangeApplyResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            await async_client.subscription_changes.with_raw_response.apply(
                subscription_change_id="",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOrb) -> None:
        subscription_change = await async_client.subscription_changes.cancel(
            "subscription_change_id",
        )
        assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscription_changes.with_raw_response.cancel(
            "subscription_change_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription_change = response.parse()
        assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOrb) -> None:
        async with async_client.subscription_changes.with_streaming_response.cancel(
            "subscription_change_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription_change = await response.parse()
            assert_matches_type(SubscriptionChangeCancelResponse, subscription_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_change_id` but received ''"
        ):
            await async_client.subscription_changes.with_raw_response.cancel(
                "",
            )
