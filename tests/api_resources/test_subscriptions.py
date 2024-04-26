# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Subscription,
    SubscriptionUsage,
    SubscriptionFetchCostsResponse,
    SubscriptionFetchScheduleResponse,
)
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        subscription = client.subscriptions.create()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.create(
            align_billing_with_subscription_start_date=True,
            auto_collection=True,
            aws_region="string",
            coupon_redemption_code="string",
            credits_overage_rate=0,
            customer_id="string",
            default_invoice_memo="string",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_customer_id="string",
            external_marketplace="google",
            external_marketplace_reporting_id="string",
            external_plan_id="ZMwNQefe7J3ecf7W",
            initial_phase_order=0,
            invoicing_threshold="string",
            metadata={"foo": "string"},
            net_terms=0,
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        subscription = client.subscriptions.update(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.update(
            "string",
            auto_collection=True,
            default_invoice_memo="string",
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        subscription = client.subscriptions.list()
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            customer_id="string",
            external_customer_id="string",
            limit=0,
            status="active",
        )
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Orb) -> None:
        subscription = client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
            cancellation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.cancel(
                "",
                cancel_option="end_of_subscription_term",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_costs(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_costs(
            "string",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_method_fetch_costs_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_costs(
            "string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch_costs(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_costs(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch_costs(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_costs(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_costs(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.fetch_costs(
                "",
            )

    @parametrize
    def test_method_fetch_schedule(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_schedule(
            "string",
        )
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_method_fetch_schedule_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_schedule(
            "string",
            cursor="string",
            limit=0,
            start_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch_schedule(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_schedule(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch_schedule(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_schedule(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_schedule(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.fetch_schedule(
                "",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_fetch_usage(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_usage(
            "string",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_fetch_usage_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_usage(
            "string",
            billable_metric_id="string",
            cursor="string",
            first_dimension_key="string",
            first_dimension_value="string",
            granularity="day",
            group_by="string",
            limit=0,
            second_dimension_key="string",
            second_dimension_value="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_raw_response_fetch_usage(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_usage(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_streaming_response_fetch_usage(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_usage(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUsage, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_path_params_fetch_usage(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.fetch_usage(
                "",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_price_intervals(self, client: Orb) -> None:
        subscription = client.subscriptions.price_intervals(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_price_intervals_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.price_intervals(
            "string",
            add=[
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
            ],
            edit=[
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_raw_response_price_intervals(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.price_intervals(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_streaming_response_price_intervals(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.price_intervals(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_path_params_price_intervals(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.price_intervals(
                "",
            )

    @parametrize
    def test_method_schedule_plan_change(self, client: Orb) -> None:
        subscription = client.subscriptions.schedule_plan_change(
            "string",
            change_option="requested_date",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_schedule_plan_change_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.schedule_plan_change(
            "string",
            change_option="requested_date",
            align_billing_with_plan_change_date=True,
            billing_cycle_alignment="unchanged",
            change_date="2017-07-21T17:32:28Z",
            coupon_redemption_code="string",
            credits_overage_rate=0,
            external_plan_id="ZMwNQefe7J3ecf7W",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_schedule_plan_change(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.schedule_plan_change(
            "string",
            change_option="requested_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_schedule_plan_change(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.schedule_plan_change(
            "string",
            change_option="requested_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schedule_plan_change(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.schedule_plan_change(
                "",
                change_option="requested_date",
            )

    @parametrize
    def test_method_trigger_phase(self, client: Orb) -> None:
        subscription = client.subscriptions.trigger_phase(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_trigger_phase_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.trigger_phase(
            "string",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_trigger_phase(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.trigger_phase(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_trigger_phase(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.trigger_phase(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger_phase(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.trigger_phase(
                "",
            )

    @parametrize
    def test_method_unschedule_cancellation(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_cancellation(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_cancellation(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_cancellation(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_cancellation(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_cancellation(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unschedule_cancellation(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.unschedule_cancellation(
                "",
            )

    @parametrize
    def test_method_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
                "",
                price_id="string",
            )

    @parametrize
    def test_method_unschedule_pending_plan_changes(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_pending_plan_changes(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_pending_plan_changes(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_pending_plan_changes(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_pending_plan_changes(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unschedule_pending_plan_changes(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
                "",
            )

    @parametrize
    def test_method_update_fixed_fee_quantity(self, client: Orb) -> None:
        subscription = client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_update_fixed_fee_quantity_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
            change_option="immediate",
            effective_date=parse_date("2022-12-21"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_update_fixed_fee_quantity(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update_fixed_fee_quantity(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_fixed_fee_quantity(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_fixed_fee_quantity(
                "",
                price_id="string",
                quantity=0,
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.create()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.create(
            align_billing_with_subscription_start_date=True,
            auto_collection=True,
            aws_region="string",
            coupon_redemption_code="string",
            credits_overage_rate=0,
            customer_id="string",
            default_invoice_memo="string",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_customer_id="string",
            external_marketplace="google",
            external_marketplace_reporting_id="string",
            external_plan_id="ZMwNQefe7J3ecf7W",
            initial_phase_order=0,
            invoicing_threshold="string",
            metadata={"foo": "string"},
            net_terms=0,
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update(
            "string",
            auto_collection=True,
            default_invoice_memo="string",
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.list()
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            customer_id="string",
            external_customer_id="string",
            limit=0,
            status="active",
        )
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
            cancellation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.cancel(
                "",
                cancel_option="end_of_subscription_term",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_costs(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_costs(
            "string",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_method_fetch_costs_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_costs(
            "string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch_costs(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_costs(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_costs(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_costs(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_costs(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.fetch_costs(
                "",
            )

    @parametrize
    async def test_method_fetch_schedule(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_schedule(
            "string",
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_method_fetch_schedule_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_schedule(
            "string",
            cursor="string",
            limit=0,
            start_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch_schedule(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_schedule(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_schedule(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_schedule(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_schedule(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.fetch_schedule(
                "",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_usage(
            "string",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_usage(
            "string",
            billable_metric_id="string",
            cursor="string",
            first_dimension_key="string",
            first_dimension_value="string",
            granularity="day",
            group_by="string",
            limit=0,
            second_dimension_key="string",
            second_dimension_value="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_raw_response_fetch_usage(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_usage(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_streaming_response_fetch_usage(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_usage(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUsage, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_path_params_fetch_usage(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.fetch_usage(
                "",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.price_intervals(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.price_intervals(
            "string",
            add=[
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "conversion_rate": 0,
                        "model_type": "unit",
                        "unit_config": {"unit_amount": "string"},
                        "currency": "string",
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "discounts": [
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                        {
                            "discount_type": "amount",
                            "amount_discount": 0,
                        },
                    ],
                    "minimum_amount": 0,
                    "maximum_amount": 0,
                },
            ],
            edit=[
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                    ],
                    "billing_cycle_day": 0,
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_raw_response_price_intervals(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.price_intervals(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_streaming_response_price_intervals(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.price_intervals(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_path_params_price_intervals(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.price_intervals(
                "",
            )

    @parametrize
    async def test_method_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.schedule_plan_change(
            "string",
            change_option="requested_date",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_schedule_plan_change_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.schedule_plan_change(
            "string",
            change_option="requested_date",
            align_billing_with_plan_change_date=True,
            billing_cycle_alignment="unchanged",
            change_date="2017-07-21T17:32:28Z",
            coupon_redemption_code="string",
            credits_overage_rate=0,
            external_plan_id="ZMwNQefe7J3ecf7W",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "currency": "string",
                    "conversion_rate": 0,
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {"unit_amount": "string"},
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.schedule_plan_change(
            "string",
            change_option="requested_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.schedule_plan_change(
            "string",
            change_option="requested_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.schedule_plan_change(
                "",
                change_option="requested_date",
            )

    @parametrize
    async def test_method_trigger_phase(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.trigger_phase(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_trigger_phase_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.trigger_phase(
            "string",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_trigger_phase(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.trigger_phase(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_trigger_phase(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.trigger_phase(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger_phase(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.trigger_phase(
                "",
            )

    @parametrize
    async def test_method_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.unschedule_cancellation(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_cancellation(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_cancellation(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.unschedule_cancellation(
                "",
            )

    @parametrize
    async def test_method_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
                "",
                price_id="string",
            )

    @parametrize
    async def test_method_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.unschedule_pending_plan_changes(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_pending_plan_changes(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
                "",
            )

    @parametrize
    async def test_method_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_fixed_fee_quantity_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
            change_option="immediate",
            effective_date=parse_date("2022-12-21"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_fixed_fee_quantity(
                "",
                price_id="string",
                quantity=0,
            )
