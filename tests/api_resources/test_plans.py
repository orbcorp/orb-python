# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        plan = client.plans.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        plan = client.plans.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                    "billable_metric_id": "billable_metric_id",
                    "billed_in_advance": True,
                    "billing_cycle_configuration": {
                        "duration": 0,
                        "duration_unit": "day",
                    },
                    "conversion_rate": 0,
                    "currency": "currency",
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 0,
                    "invoice_grouping_key": "invoice_grouping_key",
                    "invoicing_cycle_configuration": {
                        "duration": 0,
                        "duration_unit": "day",
                    },
                    "metadata": {"foo": "string"},
                }
            ],
            default_invoice_memo="default_invoice_memo",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
            net_terms=0,
            status="active",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.plans.with_raw_response.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.plans.with_streaming_response.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        plan = client.plans.update(
            plan_id="plan_id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        plan = client.plans.update(
            plan_id="plan_id",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.plans.with_raw_response.update(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.plans.with_streaming_response.update(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.with_raw_response.update(
                plan_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        plan = client.plans.list()
        assert_matches_type(SyncPage[Plan], plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        plan = client.plans.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(SyncPage[Plan], plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncPage[Plan], plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncPage[Plan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        plan = client.plans.fetch(
            "plan_id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.plans.with_raw_response.fetch(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.plans.with_streaming_response.fetch(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.with_raw_response.fetch(
                "",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                    "billable_metric_id": "billable_metric_id",
                    "billed_in_advance": True,
                    "billing_cycle_configuration": {
                        "duration": 0,
                        "duration_unit": "day",
                    },
                    "conversion_rate": 0,
                    "currency": "currency",
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 0,
                    "invoice_grouping_key": "invoice_grouping_key",
                    "invoicing_cycle_configuration": {
                        "duration": 0,
                        "duration_unit": "day",
                    },
                    "metadata": {"foo": "string"},
                }
            ],
            default_invoice_memo="default_invoice_memo",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
            net_terms=0,
            status="active",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.with_raw_response.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.with_streaming_response.create(
            currency="currency",
            name="name",
            prices=[
                {
                    "cadence": "annual",
                    "item_id": "item_id",
                    "model_type": "unit",
                    "name": "Annual fee",
                    "unit_config": {"unit_amount": "unit_amount"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.update(
            plan_id="plan_id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.update(
            plan_id="plan_id",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.with_raw_response.update(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.with_streaming_response.update(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.with_raw_response.update(
                plan_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.list()
        assert_matches_type(AsyncPage[Plan], plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(AsyncPage[Plan], plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(AsyncPage[Plan], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncPage[Plan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        plan = await async_client.plans.fetch(
            "plan_id",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.with_raw_response.fetch(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.with_streaming_response.fetch(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.with_raw_response.fetch(
                "",
            )
