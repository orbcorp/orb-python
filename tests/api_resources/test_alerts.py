# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Alert,
)
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        alert = client.alerts.retrieve(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            client.alerts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    def test_method_list(self, client: Orb) -> None:
        alert = client.alerts.list()
        assert_matches_type(SyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        alert = client.alerts.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            customer_id="string",
            external_customer_id="string",
            limit=1,
            subscription_id="string",
        )
        assert_matches_type(SyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(SyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(SyncPage[Alert], alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_for_customer(self, client: Orb) -> None:
        alert = client.alerts.create_for_customer(
            "string",
            currency="string",
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_method_create_for_customer_with_all_params(self, client: Orb) -> None:
        alert = client.alerts.create_for_customer(
            "string",
            currency="string",
            type="string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_create_for_customer(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.create_for_customer(
            "string",
            currency="string",
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_create_for_customer(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.create_for_customer(
            "string",
            currency="string",
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_for_customer(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.alerts.with_raw_response.create_for_customer(
                "",
                currency="string",
                type="string",
            )

    @parametrize
    def test_method_create_for_external_customer(self, client: Orb) -> None:
        alert = client.alerts.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_method_create_for_external_customer_with_all_params(self, client: Orb) -> None:
        alert = client.alerts.create_for_external_customer(
            "string",
            currency="string",
            type="string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_create_for_external_customer(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_create_for_external_customer(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_for_external_customer(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.alerts.with_raw_response.create_for_external_customer(
                "",
                currency="string",
                type="string",
            )

    @parametrize
    def test_method_create_for_subscription(self, client: Orb) -> None:
        alert = client.alerts.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_method_create_for_subscription_with_all_params(self, client: Orb) -> None:
        alert = client.alerts.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
            metric_id="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_create_for_subscription(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_create_for_subscription(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_for_subscription(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.alerts.with_raw_response.create_for_subscription(
                "",
                thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
                type="string",
            )

    @parametrize
    def test_method_disable(self, client: Orb) -> None:
        alert = client.alerts.disable(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Orb) -> None:
        response = client.alerts.with_raw_response.disable(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Orb) -> None:
        with client.alerts.with_streaming_response.disable(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `alert_configuration_id` but received ''"
        ):
            client.alerts.with_raw_response.disable(
                "",
            )

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
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.retrieve(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            await async_client.alerts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.list()
        assert_matches_type(AsyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            customer_id="string",
            external_customer_id="string",
            limit=1,
            subscription_id="string",
        )
        assert_matches_type(AsyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AsyncPage[Alert], alert, path=["response"])

    @pytest.mark.skip(reason="plan_version=0 breaks Prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AsyncPage[Alert], alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_for_customer(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_customer(
            "string",
            currency="string",
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_method_create_for_customer_with_all_params(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_customer(
            "string",
            currency="string",
            type="string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_create_for_customer(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.create_for_customer(
            "string",
            currency="string",
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_create_for_customer(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.create_for_customer(
            "string",
            currency="string",
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_for_customer(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.alerts.with_raw_response.create_for_customer(
                "",
                currency="string",
                type="string",
            )

    @parametrize
    async def test_method_create_for_external_customer(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_method_create_for_external_customer_with_all_params(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_external_customer(
            "string",
            currency="string",
            type="string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_create_for_external_customer(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_create_for_external_customer(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.create_for_external_customer(
            "string",
            currency="string",
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_for_external_customer(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.alerts.with_raw_response.create_for_external_customer(
                "",
                currency="string",
                type="string",
            )

    @parametrize
    async def test_method_create_for_subscription(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_method_create_for_subscription_with_all_params(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
            metric_id="string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_create_for_subscription(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_create_for_subscription(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.create_for_subscription(
            "string",
            thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_for_subscription(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.alerts.with_raw_response.create_for_subscription(
                "",
                thresholds=[{"value": 0}, {"value": 0}, {"value": 0}],
                type="string",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncOrb) -> None:
        alert = await async_client.alerts.disable(
            "string",
        )
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncOrb) -> None:
        response = await async_client.alerts.with_raw_response.disable(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(Alert, alert, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncOrb) -> None:
        async with async_client.alerts.with_streaming_response.disable(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(Alert, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `alert_configuration_id` but received ''"
        ):
            await async_client.alerts.with_raw_response.disable(
                "",
            )

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
