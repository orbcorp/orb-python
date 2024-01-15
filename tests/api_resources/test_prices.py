# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Price
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPrices:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={
                "unit_amount": "string",
                "scaling_factor": 0,
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
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
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "string",
                "package_size": 0,
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                ],
                "scaling_factor": 0,
            },
            model_type="matrix",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
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
    def test_streaming_response_create_overload_3(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
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
    def test_method_create_overload_4(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
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
    def test_method_create_overload_5(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                ]
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_5(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                ]
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
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
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
    def test_method_create_overload_6(self, client: Orb) -> None:
        price = client.prices.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Orb) -> None:
        price = client.prices.create(
            bps_config={
                "bps": 0,
                "per_unit_maximum": "string",
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_6(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_6(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
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
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_bps_config={
                "tiers": [
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                ]
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_7(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_7(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_8(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Orb) -> None:
        price = client.prices.create(
            bulk_config={
                "tiers": [
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                ]
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_8(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_8(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
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
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_9(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_9(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
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
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_10(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_10(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
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
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_11(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_11(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
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
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Orb) -> None:
        price = client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_create_overload_12(self, client: Orb) -> None:
        response = client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_12(self, client: Orb) -> None:
        with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        price = client.prices.list()
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        price = client.prices.list(
            cursor="string",
            limit=0,
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
    def test_method_fetch(self, client: Orb) -> None:
        price = client.prices.fetch(
            "string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.prices.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.prices.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrices:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={
                "unit_amount": "string",
                "scaling_factor": 0,
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="unit",
            name="Annual fee",
            unit_config={"unit_amount": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={
                "package_amount": "string",
                "package_size": 0,
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package",
            name="Annual fee",
            package_config={"package_amount": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                ],
            },
            model_type="matrix",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                        "dimension_values": ["string", "string", "string"],
                    },
                ],
                "scaling_factor": 0,
            },
            model_type="matrix",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
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
    async def test_streaming_response_create_overload_3(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            matrix_config={
                "dimensions": ["string", "string", "string"],
                "default_unit_amount": "string",
                "matrix_values": [
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
                    {
                        "unit_amount": "string",
                        "dimension_values": ["string", "string", "string"],
                    },
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
    async def test_method_create_overload_4(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "last_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered",
            name="Annual fee",
            tiered_config={
                "tiers": [
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
                    },
                    {
                        "first_unit": 0,
                        "unit_amount": "string",
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
    async def test_method_create_overload_5(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                ]
            },
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_5(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "minimum_amount": "string",
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                ]
            },
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_5(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_5(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_bps",
            name="Annual fee",
            tiered_bps_config={
                "tiers": [
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
                    },
                    {
                        "minimum_amount": "string",
                        "bps": 0,
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
    async def test_method_create_overload_6(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_6(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bps_config={
                "bps": 0,
                "per_unit_maximum": "string",
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_6(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_6(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            bps_config={"bps": 0},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bps",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_7(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_7(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bulk_bps_config={
                "tiers": [
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                    {
                        "maximum_amount": "string",
                        "bps": 0,
                        "per_unit_maximum": "string",
                    },
                ]
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_7(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_7(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            bulk_bps_config={"tiers": [{"bps": 0}, {"bps": 0}, {"bps": 0}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk_bps",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_8(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_8(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            bulk_config={
                "tiers": [
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                    {
                        "maximum_units": 0,
                        "unit_amount": "string",
                    },
                ]
            },
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_8(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_8(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            bulk_config={"tiers": [{"unit_amount": "string"}, {"unit_amount": "string"}, {"unit_amount": "string"}]},
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="bulk",
            name="Annual fee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_9(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_9(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_9(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_9(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="threshold_total_amount",
            name="Annual fee",
            threshold_total_amount_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_10(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_10(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_10(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_10(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_package",
            name="Annual fee",
            tiered_package_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_11(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_11(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_11(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_11(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="tiered_with_minimum",
            name="Annual fee",
            tiered_with_minimum_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_12(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_12(self, client: AsyncOrb) -> None:
        price = await client.prices.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
            billable_metric_id="string",
            billed_in_advance=True,
            external_price_id="string",
            fixed_price_quantity=0,
            invoice_grouping_key="string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_12(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_12(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.create(
            cadence="annual",
            currency="string",
            item_id="string",
            model_type="package_with_allocation",
            name="Annual fee",
            package_with_allocation_config={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        price = await client.prices.list()
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        price = await client.prices.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(AsyncPage[Price], price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        price = await client.prices.fetch(
            "string",
        )
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, client: AsyncOrb) -> None:
        response = await client.prices.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, client: AsyncOrb) -> None:
        async with client.prices.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True
