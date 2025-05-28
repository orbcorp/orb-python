# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.plans.external_plan_id import VersionCreateResponse, VersionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        version = client.plans.external_plan_id.versions.create(
            external_plan_id="external_plan_id",
            version=0,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        version = client.plans.external_plan_id.versions.create(
            external_plan_id="external_plan_id",
            version=0,
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "is_invoice_level": True,
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
                        "expires_at_end_of_cadence": True,
                    },
                    "plan_phase_order": 0,
                    "price": {
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
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "is_invoice_level": True,
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
                        "expires_at_end_of_cadence": True,
                    },
                    "plan_phase_order": 0,
                    "price": {
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
                    },
                }
            ],
            set_as_default=True,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.plans.external_plan_id.versions.with_raw_response.create(
            external_plan_id="external_plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.plans.external_plan_id.versions.with_streaming_response.create(
            external_plan_id="external_plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionCreateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            client.plans.external_plan_id.versions.with_raw_response.create(
                external_plan_id="",
                version=0,
            )

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        version = client.plans.external_plan_id.versions.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.plans.external_plan_id.versions.with_raw_response.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.plans.external_plan_id.versions.with_streaming_response.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            client.plans.external_plan_id.versions.with_raw_response.retrieve(
                version="version",
                external_plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.plans.external_plan_id.versions.with_raw_response.retrieve(
                version="",
                external_plan_id="external_plan_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        version = await async_client.plans.external_plan_id.versions.create(
            external_plan_id="external_plan_id",
            version=0,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        version = await async_client.plans.external_plan_id.versions.create(
            external_plan_id="external_plan_id",
            version=0,
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "percentage_discount": 0,
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "is_invoice_level": True,
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
                        "expires_at_end_of_cadence": True,
                    },
                    "plan_phase_order": 0,
                    "price": {
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
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "is_invoice_level": True,
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
                        "expires_at_end_of_cadence": True,
                    },
                    "plan_phase_order": 0,
                    "price": {
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
                    },
                }
            ],
            set_as_default=True,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.external_plan_id.versions.with_raw_response.create(
            external_plan_id="external_plan_id",
            version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.external_plan_id.versions.with_streaming_response.create(
            external_plan_id="external_plan_id",
            version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionCreateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            await async_client.plans.external_plan_id.versions.with_raw_response.create(
                external_plan_id="",
                version=0,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        version = await async_client.plans.external_plan_id.versions.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.external_plan_id.versions.with_raw_response.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.external_plan_id.versions.with_streaming_response.retrieve(
            version="version",
            external_plan_id="external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            await async_client.plans.external_plan_id.versions.with_raw_response.retrieve(
                version="version",
                external_plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.plans.external_plan_id.versions.with_raw_response.retrieve(
                version="",
                external_plan_id="external_plan_id",
            )
