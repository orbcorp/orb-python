# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Alert
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_enable(self, client: Orb) -> None:
        alert = client.alerts.enable(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.enable(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.enable(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `alert_configuration_id` but received ''"
        ):
            client.alerts.with_raw_response.enable(
                "",
            )


class TestAsyncAlerts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_enable(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.enable(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.enable(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.enable(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `alert_configuration_id` but received ''"
        ):
            await async_client.alerts.with_raw_response.enable(
                "",
            )
