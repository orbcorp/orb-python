# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    PriceEvaluateResponse,
    PriceEvaluateMultipleResponse,
    PriceEvaluatePreviewEventsResponse,
)
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.shared import Price

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={
                "unit_amount": "unit_amount",
                "prorated": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                        "last_unit": 0,
                    }
                ],
                "prorated": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_config={
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "maximum_units": 0,
                    }
                ]
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_5(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_5(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_6(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_6(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_6(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_7(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ],
                "prorate": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_7(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_7(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_8(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_8(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_8(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_9(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
                "hide_zero_amount_tiers": True,
                "prorate": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_9(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_9(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_10(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_10(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_10(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_11(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_11(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_11(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_12(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_12(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_12(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_13(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_13(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_13(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_14(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_14(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_14(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_15(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_15(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_15(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_15(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_16(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_16(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_16(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_16(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_17(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_17(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_17(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_17(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_18(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_18(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_with_proration_config={
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ]
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_18(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_18(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_19(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_19(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_19(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_19(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_20(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_20(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_20(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_20(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_21(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_21(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_21(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_21(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_22(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_22(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_22(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_22(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_23(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_23(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_23(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_23(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_24(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_24(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_24(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_24(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_25(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_25(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                        "second_dimension_value": "second_dimension_value",
                    }
                ],
                "unit_price": "unit_price",
                "prorate": True,
                "second_dimension": "second_dimension",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_25(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_25(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_26(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_26(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                        "second_dimension_value": "second_dimension_value",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
                "second_dimension": "second_dimension",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_26(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_26(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_27(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_27(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_27(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_27(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_28(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_28(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_28(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_28(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_29(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_29(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={
                "minimum_amount": "minimum_amount",
                "prorated": True,
            },
            model_type="minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_29(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_29(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_30(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_30(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_30(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_30(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_31(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_31(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="currency",
            event_output_config={
                "unit_rating_key": "x",
                "default_unit_rate": "default_unit_rate",
                "grouping_key": "grouping_key",
            },
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_31(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_31(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        price = client.prices.update(
            price_id="price_id",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        price = client.prices.update(
            price_id="price_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.prices.with_raw_response.update(
            price_id="price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.prices.with_streaming_response.update(
            price_id="price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            client.prices.with_raw_response.update(
                price_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        price = client.prices.list()
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        price = client.prices.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.prices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.prices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(SyncPage[Price], price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_evaluate(self, client: Orb) -> None:
        price = client.prices.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: Orb) -> None:
        price = client.prices.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            external_customer_id="external_customer_id",
            filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            grouping_keys=["case when my_event_type = 'foo' then true else false end"],
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: Orb) -> None:
        response = client.prices.with_raw_response.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: Orb) -> None:
        with client.prices.with_streaming_response.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceEvaluateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            client.prices.with_raw_response.evaluate(
                price_id="",
                timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
                timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    def test_method_evaluate_multiple(self, client: Orb) -> None:
        price = client.prices.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    def test_method_evaluate_multiple_with_all_params(self, client: Orb) -> None:
        price = client.prices.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            external_customer_id="external_customer_id",
            price_evaluations=[
                {
                    "external_price_id": "external_price_id",
                    "filter": "my_numeric_property > 100 AND my_other_property = 'bar'",
                    "grouping_keys": ["case when my_event_type = 'foo' then true else false end"],
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                    "price_id": "price_id",
                }
            ],
        )
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    def test_raw_response_evaluate_multiple(self, client: Orb) -> None:
        response = client.prices.with_raw_response.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_evaluate_multiple(self, client: Orb) -> None:
        with client.prices.with_streaming_response.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_evaluate_preview_events(self, client: Orb) -> None:
        price = client.prices.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    def test_method_evaluate_preview_events_with_all_params(self, client: Orb) -> None:
        price = client.prices.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "properties": {"foo": "bar"},
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                }
            ],
            external_customer_id="external_customer_id",
            price_evaluations=[
                {
                    "external_price_id": "external_price_id",
                    "filter": "my_numeric_property > 100 AND my_other_property = 'bar'",
                    "grouping_keys": ["case when my_event_type = 'foo' then true else false end"],
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                    "price_id": "price_id",
                }
            ],
        )
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    def test_raw_response_evaluate_preview_events(self, client: Orb) -> None:
        response = client.prices.with_raw_response.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_evaluate_preview_events(self, client: Orb) -> None:
        with client.prices.with_streaming_response.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        price = client.prices.fetch(
            "price_id",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.prices.with_raw_response.fetch(
            "price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.prices.with_streaming_response.fetch(
            "price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            client.prices.with_raw_response.fetch(
                "",
            )


class TestAsyncPrices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={
                "unit_amount": "unit_amount",
                "prorated": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "unit_amount"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                        "last_unit": 0,
                    }
                ],
                "prorated": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_config={
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "maximum_units": 0,
                    }
                ]
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            bulk_config={"tiers": [{"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            bulk_with_filters_config={
                "filters": [
                    {
                        "property_key": "x",
                        "property_value": "x",
                    }
                ],
                "tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}],
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_filters",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "package_amount",
                "package_size": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_config={
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ],
                "prorate": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={
                "consumption_table": [
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                    {
                        "threshold": "threshold",
                        "total_amount": "total_amount",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
                "hide_zero_amount_tiers": True,
                "prorate": True,
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_config={
                "grouping_key": "x",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_package_with_minimum",
            name="Annual fee",
            tiered_package_with_minimum_config={
                "package_size": 0,
                "tiers": [
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "minimum_amount": "minimum_amount",
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={
                "allocation": "allocation",
                "package_amount": "package_amount",
                "package_size": "package_size",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_percent",
            name="Annual fee",
            unit_with_percent_config={
                "percent": "percent",
                "unit_amount": "unit_amount",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_allocation_config={
                "allocation": "allocation",
                "default_unit_amount": "default_unit_amount",
                "dimensions": ["string"],
                "matrix_values": [
                    {
                        "dimension_values": ["string"],
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_15(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_15(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="tiered_with_proration",
            name="Annual fee",
            tiered_with_proration_config={
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_16(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_16(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="unit_with_proration",
            name="Annual fee",
            unit_with_proration_config={"unit_amount": "unit_amount"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_17(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_17(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_17(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_17(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_allocation_config={
                "allocation": "allocation",
                "grouping_key": "x",
                "overage_unit_rate": "overage_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_18(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_18(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            bulk_with_proration_config={
                "tiers": [
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "unit_amount": "unit_amount",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ]
            },
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_18(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_18(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            bulk_with_proration_config={"tiers": [{"unit_amount": "unit_amount"}, {"unit_amount": "unit_amount"}]},
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="bulk_with_proration",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_19(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_19(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_19(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_19(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_prorated_minimum_config={
                "grouping_key": "x",
                "minimum": "minimum",
                "unit_rate": "unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_prorated_minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_20(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_20(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_20(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_20(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_metered_minimum_config={
                "grouping_key": "x",
                "minimum_unit_amount": "minimum_unit_amount",
                "pricing_key": "pricing_key",
                "scaling_factors": [
                    {
                        "scaling_factor": "scaling_factor",
                        "scaling_value": "scaling_value",
                    }
                ],
                "scaling_key": "scaling_key",
                "unit_amounts": [
                    {
                        "pricing_value": "pricing_value",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            item_id="item_id",
            model_type="grouped_with_metered_minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_21(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_21(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_21(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_21(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_with_min_max_thresholds_config={
                "grouping_key": "x",
                "maximum_charge": "maximum_charge",
                "minimum_charge": "minimum_charge",
                "per_unit_rate": "per_unit_rate",
            },
            item_id="item_id",
            model_type="grouped_with_min_max_thresholds",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_22(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_22(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_22(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_22(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            matrix_with_display_name_config={
                "dimension": "dimension",
                "unit_amounts": [
                    {
                        "dimension_value": "dimension_value",
                        "display_name": "display_name",
                        "unit_amount": "unit_amount",
                    }
                ],
            },
            model_type="matrix_with_display_name",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_23(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_23(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_23(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_23(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            grouped_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                    {
                        "per_unit": "per_unit",
                        "tier_lower_bound": "tier_lower_bound",
                    },
                ],
            },
            item_id="item_id",
            model_type="grouped_tiered_package",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_24(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_24(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_24(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_24(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            max_group_tiered_package_config={
                "grouping_key": "x",
                "package_size": "package_size",
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
            model_type="max_group_tiered_package",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_25(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_25(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                        "second_dimension_value": "second_dimension_value",
                    }
                ],
                "unit_price": "unit_price",
                "prorate": True,
                "second_dimension": "second_dimension",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_25(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_25(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_unit_pricing",
            name="Annual fee",
            scalable_matrix_with_unit_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "unit_price": "unit_price",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_26(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_26(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                        "second_dimension_value": "second_dimension_value",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
                "second_dimension": "second_dimension",
            },
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_26(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_26(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="scalable_matrix_with_tiered_pricing",
            name="Annual fee",
            scalable_matrix_with_tiered_pricing_config={
                "first_dimension": "first_dimension",
                "matrix_scaling_factors": [
                    {
                        "first_dimension_value": "first_dimension_value",
                        "scaling_factor": "scaling_factor",
                    }
                ],
                "tiers": [
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                    {
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_27(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_27(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_27(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_27(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            cumulative_grouped_bulk_config={
                "dimension_values": [
                    {
                        "grouping_key": "x",
                        "tier_lower_bound": "tier_lower_bound",
                        "unit_amount": "unit_amount",
                    }
                ],
                "group": "group",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_bulk",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_28(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_28(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_28(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_28(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            cumulative_grouped_allocation_config={
                "cumulative_allocation": "cumulative_allocation",
                "group_allocation": "group_allocation",
                "grouping_key": "x",
                "unit_amount": "unit_amount",
            },
            currency="currency",
            item_id="item_id",
            model_type="cumulative_grouped_allocation",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_29(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_29(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={
                "minimum_amount": "minimum_amount",
                "prorated": True,
            },
            model_type="minimum",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_29(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_29(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            minimum_config={"minimum_amount": "minimum_amount"},
            model_type="minimum",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_30(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_30(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_30(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_30(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            item_id="item_id",
            model_type="percent",
            name="Annual fee",
            percent_config={"percent": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_31(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_31(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.create(
            cadence="annual",
            currency="currency",
            event_output_config={
                "unit_rating_key": "x",
                "default_unit_rate": "default_unit_rate",
                "grouping_key": "grouping_key",
            },
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
            billable_metric_id="billable_metric_id",
            billed_in_advance=True,
            billing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            conversion_rate=0,
            conversion_rate_config={
                "conversion_rate_type": "unit",
                "unit_config": {"unit_amount": "unit_amount"},
            },
            dimensional_price_configuration={
                "dimension_values": ["string"],
                "dimensional_price_group_id": "dimensional_price_group_id",
                "external_dimensional_price_group_id": "external_dimensional_price_group_id",
            },
            external_price_id="external_price_id",
            fixed_price_quantity=0,
            invoice_grouping_key="x",
            invoicing_cycle_configuration={
                "duration": 0,
                "duration_unit": "day",
            },
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_31(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_31(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.create(
            cadence="annual",
            currency="currency",
            event_output_config={"unit_rating_key": "x"},
            item_id="item_id",
            model_type="event_output",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.update(
            price_id="price_id",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.update(
            price_id="price_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.update(
            price_id="price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.update(
            price_id="price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            await async_client.prices.with_raw_response.update(
                price_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.list()
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(AsyncPage[Price], price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            external_customer_id="external_customer_id",
            filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            grouping_keys=["case when my_event_type = 'foo' then true else false end"],
        )
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.evaluate(
            price_id="price_id",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceEvaluateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            await async_client.prices.with_raw_response.evaluate(
                price_id="",
                timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
                timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    async def test_method_evaluate_multiple(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    async def test_method_evaluate_multiple_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            external_customer_id="external_customer_id",
            price_evaluations=[
                {
                    "external_price_id": "external_price_id",
                    "filter": "my_numeric_property > 100 AND my_other_property = 'bar'",
                    "grouping_keys": ["case when my_event_type = 'foo' then true else false end"],
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                    "price_id": "price_id",
                }
            ],
        )
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_evaluate_multiple(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate_multiple(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.evaluate_multiple(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceEvaluateMultipleResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_evaluate_preview_events(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    async def test_method_evaluate_preview_events_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "properties": {"foo": "bar"},
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                }
            ],
            external_customer_id="external_customer_id",
            price_evaluations=[
                {
                    "external_price_id": "external_price_id",
                    "filter": "my_numeric_property > 100 AND my_other_property = 'bar'",
                    "grouping_keys": ["case when my_event_type = 'foo' then true else false end"],
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                    "price_id": "price_id",
                }
            ],
        )
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_evaluate_preview_events(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate_preview_events(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.evaluate_preview_events(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceEvaluatePreviewEventsResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        price = await async_client.prices.fetch(
            "price_id",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.with_raw_response.fetch(
            "price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.with_streaming_response.fetch(
            "price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `price_id` but received ''"):
            await async_client.prices.with_raw_response.fetch(
                "",
            )
