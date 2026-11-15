# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import PlanVersion
from tests.utils import assert_matches_type
from orb.types.plans import PlanVersionDraft

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_discard(self, client: Orb) -> None:
        draft = client.plans.draft.discard(
            "plan_id",
        )
        assert draft is None

    @parametrize
    def test_raw_response_discard(self, client: Orb) -> None:
        response = client.plans.draft.with_raw_response.discard(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @parametrize
    def test_streaming_response_discard(self, client: Orb) -> None:
        with client.plans.draft.with_streaming_response.discard(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_discard(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.draft.with_raw_response.discard(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        draft = client.plans.draft.fetch(
            "plan_id",
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.plans.draft.with_raw_response.fetch(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.plans.draft.with_streaming_response.fetch(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PlanVersionDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.draft.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_publish(self, client: Orb) -> None:
        draft = client.plans.draft.publish(
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    def test_method_publish_with_all_params(self, client: Orb) -> None:
        draft = client.plans.draft.publish(
            plan_id="plan_id",
            set_as_default=True,
        )
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    def test_raw_response_publish(self, client: Orb) -> None:
        response = client.plans.draft.with_raw_response.publish(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    def test_streaming_response_publish(self, client: Orb) -> None:
        with client.plans.draft.with_streaming_response.publish(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PlanVersion, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_publish(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.draft.with_raw_response.publish(
                plan_id="",
            )

    @parametrize
    def test_method_save(self, client: Orb) -> None:
        draft = client.plans.draft.save(
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    def test_method_save_with_all_params(self, client: Orb) -> None:
        draft = client.plans.draft.save(
            plan_id="plan_id",
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_all": True,
                        "applies_to_item_ids": ["item_1", "item_2"],
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "currency": "currency",
                        "filters": [
                            {
                                "field": "price_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "is_invoice_level": True,
                        "price_type": "usage",
                    },
                    "plan_phase_order": 0,
                }
            ],
            add_prices=[
                {
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "monthly",
                        "currency": "USD",
                        "custom_expiration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "expires_at_end_of_cadence": True,
                        "filters": [
                            {
                                "field": "item_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "item_id": "item_id",
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "per_unit_cost_basis": "per_unit_cost_basis",
                    },
                    "license_allocation_price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "license_allocations": [
                            {
                                "amount": "amount",
                                "currency": "currency",
                                "write_off_overage": True,
                            }
                        ],
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
            description="description",
            remove_adjustments=[
                {
                    "adjustment_id": "adjustment_id",
                    "plan_phase_order": 0,
                }
            ],
            remove_prices=[
                {
                    "price_id": "price_id",
                    "plan_phase_order": 0,
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_all": True,
                        "applies_to_item_ids": ["item_1", "item_2"],
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "currency": "currency",
                        "filters": [
                            {
                                "field": "price_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "is_invoice_level": True,
                        "price_type": "usage",
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                    "plan_phase_order": 0,
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "monthly",
                        "currency": "USD",
                        "custom_expiration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "expires_at_end_of_cadence": True,
                        "filters": [
                            {
                                "field": "item_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "item_id": "item_id",
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "per_unit_cost_basis": "per_unit_cost_basis",
                    },
                    "license_allocation_price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "license_allocations": [
                            {
                                "amount": "amount",
                                "currency": "currency",
                                "write_off_overage": True,
                            }
                        ],
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    def test_raw_response_save(self, client: Orb) -> None:
        response = client.plans.draft.with_raw_response.save(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    def test_streaming_response_save(self, client: Orb) -> None:
        with client.plans.draft.with_streaming_response.save(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PlanVersionDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_save(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.draft.with_raw_response.save(
                plan_id="",
            )


class TestAsyncDraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_discard(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.discard(
            "plan_id",
        )
        assert draft is None

    @parametrize
    async def test_raw_response_discard(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.draft.with_raw_response.discard(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @parametrize
    async def test_streaming_response_discard(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.draft.with_streaming_response.discard(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_discard(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.draft.with_raw_response.discard(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.fetch(
            "plan_id",
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.draft.with_raw_response.fetch(
            "plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.draft.with_streaming_response.fetch(
            "plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PlanVersionDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.draft.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_publish(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.publish(
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.publish(
            plan_id="plan_id",
            set_as_default=True,
        )
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.draft.with_raw_response.publish(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersion, draft, path=["response"])

    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.draft.with_streaming_response.publish(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PlanVersion, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_publish(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.draft.with_raw_response.publish(
                plan_id="",
            )

    @parametrize
    async def test_method_save(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.save(
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    async def test_method_save_with_all_params(self, async_client: AsyncOrb) -> None:
        draft = await async_client.plans.draft.save(
            plan_id="plan_id",
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_all": True,
                        "applies_to_item_ids": ["item_1", "item_2"],
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "currency": "currency",
                        "filters": [
                            {
                                "field": "price_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "is_invoice_level": True,
                        "price_type": "usage",
                    },
                    "plan_phase_order": 0,
                }
            ],
            add_prices=[
                {
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "monthly",
                        "currency": "USD",
                        "custom_expiration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "expires_at_end_of_cadence": True,
                        "filters": [
                            {
                                "field": "item_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "item_id": "item_id",
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "per_unit_cost_basis": "per_unit_cost_basis",
                    },
                    "license_allocation_price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "license_allocations": [
                            {
                                "amount": "amount",
                                "currency": "currency",
                                "write_off_overage": True,
                            }
                        ],
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
            description="description",
            remove_adjustments=[
                {
                    "adjustment_id": "adjustment_id",
                    "plan_phase_order": 0,
                }
            ],
            remove_prices=[
                {
                    "price_id": "price_id",
                    "plan_phase_order": 0,
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_all": True,
                        "applies_to_item_ids": ["item_1", "item_2"],
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "currency": "currency",
                        "filters": [
                            {
                                "field": "price_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "is_invoice_level": True,
                        "price_type": "usage",
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                    "plan_phase_order": 0,
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "monthly",
                        "currency": "USD",
                        "custom_expiration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "expires_at_end_of_cadence": True,
                        "filters": [
                            {
                                "field": "item_id",
                                "operator": "includes",
                                "values": ["string"],
                            }
                        ],
                        "item_id": "item_id",
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "per_unit_cost_basis": "per_unit_cost_basis",
                    },
                    "license_allocation_price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "license_allocations": [
                            {
                                "amount": "amount",
                                "currency": "currency",
                                "write_off_overage": True,
                            }
                        ],
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "one_time",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
                            "scaling_factor": 0,
                        },
                        "billable_metric_id": "billable_metric_id",
                        "billed_in_advance": True,
                        "billing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "conversion_rate": 0,
                        "conversion_rate_config": {
                            "conversion_rate_type": "unit",
                            "unit_config": {"unit_amount": "unit_amount"},
                        },
                        "currency": "currency",
                        "dimensional_price_configuration": {
                            "dimension_values": ["x"],
                            "dimensional_price_group_id": "dimensional_price_group_id",
                            "external_dimensional_price_group_id": "external_dimensional_price_group_id",
                        },
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "x",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "license_type_id": "license_type_id",
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
        )
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    async def test_raw_response_save(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.draft.with_raw_response.save(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PlanVersionDraft, draft, path=["response"])

    @parametrize
    async def test_streaming_response_save(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.draft.with_streaming_response.save(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PlanVersionDraft, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_save(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.draft.with_raw_response.save(
                plan_id="",
            )
