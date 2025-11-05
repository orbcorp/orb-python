# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan, PlanVersion
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_plan_version(self, client: Orb) -> None:
        beta = client.beta.create_plan_version(
            plan_id="plan_id",
            version=0,
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    def test_method_create_plan_version_with_all_params(self, client: Orb) -> None:
        beta = client.beta.create_plan_version(
            plan_id="plan_id",
            version=0,
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
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "annual",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
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
                            "dimension_values": ["string"],
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
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
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
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "annual",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
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
                            "dimension_values": ["string"],
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
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
            set_as_default=True,
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    def test_raw_response_create_plan_version(self, client: Orb) -> None:
        response = client.beta.with_raw_response.create_plan_version(
            plan_id="plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    def test_streaming_response_create_plan_version(self, client: Orb) -> None:
        with client.beta.with_streaming_response.create_plan_version(
            plan_id="plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(PlanVersion, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_plan_version(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.beta.with_raw_response.create_plan_version(
                plan_id="",
                version=0,
            )

    @parametrize
    def test_method_fetch_plan_version(self, client: Orb) -> None:
        beta = client.beta.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    def test_raw_response_fetch_plan_version(self, client: Orb) -> None:
        response = client.beta.with_raw_response.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    def test_streaming_response_fetch_plan_version(self, client: Orb) -> None:
        with client.beta.with_streaming_response.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(PlanVersion, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_plan_version(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.beta.with_raw_response.fetch_plan_version(
                version="version",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.beta.with_raw_response.fetch_plan_version(
                version="",
                plan_id="plan_id",
            )

    @parametrize
    def test_method_set_default_plan_version(self, client: Orb) -> None:
        beta = client.beta.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        )
        assert_matches_type(Plan, beta, path=["response"])

    @parametrize
    def test_raw_response_set_default_plan_version(self, client: Orb) -> None:
        response = client.beta.with_raw_response.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(Plan, beta, path=["response"])

    @parametrize
    def test_streaming_response_set_default_plan_version(self, client: Orb) -> None:
        with client.beta.with_streaming_response.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(Plan, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_default_plan_version(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.beta.with_raw_response.set_default_plan_version(
                plan_id="",
                version=0,
            )


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_plan_version(self, async_client: AsyncOrb) -> None:
        beta = await async_client.beta.create_plan_version(
            plan_id="plan_id",
            version=0,
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    async def test_method_create_plan_version_with_all_params(self, async_client: AsyncOrb) -> None:
        beta = await async_client.beta.create_plan_version(
            plan_id="plan_id",
            version=0,
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
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "annual",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
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
                            "dimension_values": ["string"],
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
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
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
                    },
                    "plan_phase_order": 0,
                    "price": {
                        "cadence": "annual",
                        "item_id": "item_id",
                        "model_type": "unit",
                        "name": "Annual fee",
                        "unit_config": {
                            "unit_amount": "unit_amount",
                            "prorated": True,
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
                            "dimension_values": ["string"],
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
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                }
            ],
            set_as_default=True,
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    async def test_raw_response_create_plan_version(self, async_client: AsyncOrb) -> None:
        response = await async_client.beta.with_raw_response.create_plan_version(
            plan_id="plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    async def test_streaming_response_create_plan_version(self, async_client: AsyncOrb) -> None:
        async with async_client.beta.with_streaming_response.create_plan_version(
            plan_id="plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(PlanVersion, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_plan_version(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.beta.with_raw_response.create_plan_version(
                plan_id="",
                version=0,
            )

    @parametrize
    async def test_method_fetch_plan_version(self, async_client: AsyncOrb) -> None:
        beta = await async_client.beta.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        )
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    async def test_raw_response_fetch_plan_version(self, async_client: AsyncOrb) -> None:
        response = await async_client.beta.with_raw_response.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(PlanVersion, beta, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_plan_version(self, async_client: AsyncOrb) -> None:
        async with async_client.beta.with_streaming_response.fetch_plan_version(
            version="version",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(PlanVersion, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_plan_version(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.beta.with_raw_response.fetch_plan_version(
                version="version",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.beta.with_raw_response.fetch_plan_version(
                version="",
                plan_id="plan_id",
            )

    @parametrize
    async def test_method_set_default_plan_version(self, async_client: AsyncOrb) -> None:
        beta = await async_client.beta.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        )
        assert_matches_type(Plan, beta, path=["response"])

    @parametrize
    async def test_raw_response_set_default_plan_version(self, async_client: AsyncOrb) -> None:
        response = await async_client.beta.with_raw_response.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(Plan, beta, path=["response"])

    @parametrize
    async def test_streaming_response_set_default_plan_version(self, async_client: AsyncOrb) -> None:
        async with async_client.beta.with_streaming_response.set_default_plan_version(
            plan_id="plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(Plan, beta, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_default_plan_version(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.beta.with_raw_response.set_default_plan_version(
                plan_id="",
                version=0,
            )
