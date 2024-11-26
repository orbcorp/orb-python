# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    Subscription,
    SubscriptionUsage,
    SubscriptionCancelResponse,
    SubscriptionCreateResponse,
    SubscriptionFetchCostsResponse,
    SubscriptionUpdateTrialResponse,
    SubscriptionTriggerPhaseResponse,
    SubscriptionFetchScheduleResponse,
    SubscriptionPriceIntervalsResponse,
    SubscriptionSchedulePlanChangeResponse,
    SubscriptionUnscheduleCancellationResponse,
    SubscriptionUpdateFixedFeeQuantityResponse,
    SubscriptionUnschedulePendingPlanChangesResponse,
    SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse,
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
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.create(
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "plan_phase_order": 0,
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            add_prices=[
                {
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            align_billing_with_subscription_start_date=True,
            auto_collection=True,
            aws_region="aws_region",
            billing_cycle_anchor_configuration={
                "day": 1,
                "month": 1,
                "year": 0,
            },
            coupon_redemption_code="coupon_redemption_code",
            credits_overage_rate=0,
            customer_id="customer_id",
            default_invoice_memo="default_invoice_memo",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_customer_id="external_customer_id",
            external_marketplace="google",
            external_marketplace_reporting_id="external_marketplace_reporting_id",
            external_plan_id="ZMwNQefe7J3ecf7W",
            filter="my_property > 100 AND my_other_property = 'bar'",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
            per_credit_overage_amount=0,
            plan_id="ZMwNQefe7J3ecf7W",
            plan_version_number=0,
            price_overrides=[{}],
            remove_adjustments=[{"adjustment_id": "h74gfhdjvn7ujokd"}],
            remove_prices=[
                {
                    "external_price_id": "external_price_id",
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 2,
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            trial_duration_days=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        subscription = client.subscriptions.update(
            subscription_id="subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.update(
            subscription_id="subscription_id",
            auto_collection=True,
            default_invoice_memo="default_invoice_memo",
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.update(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.update(
            subscription_id="subscription_id",
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
                subscription_id="",
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
            cursor="cursor",
            customer_id=["string"],
            external_customer_id="external_customer_id",
            limit=1,
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
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        )
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
            cancellation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.cancel(
                subscription_id="",
                cancel_option="end_of_subscription_term",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch(
            "subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch(
            "subscription_id",
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
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_method_fetch_costs_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_costs(
            subscription_id="subscription_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch_costs(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_costs(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch_costs(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_costs(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @parametrize
    def test_method_fetch_schedule(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_schedule(
            subscription_id="subscription_id",
        )
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_method_fetch_schedule_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_schedule(
            subscription_id="subscription_id",
            cursor="cursor",
            limit=1,
            start_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_raw_response_fetch_schedule(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_schedule(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    def test_streaming_response_fetch_schedule(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_schedule(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_fetch_usage(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_usage(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_fetch_usage_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch_usage(
            subscription_id="subscription_id",
            billable_metric_id="billable_metric_id",
            first_dimension_key="first_dimension_key",
            first_dimension_value="first_dimension_value",
            granularity="day",
            group_by="group_by",
            second_dimension_key="second_dimension_key",
            second_dimension_value="second_dimension_value",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_raw_response_fetch_usage(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.fetch_usage(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_streaming_response_fetch_usage(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.fetch_usage(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_price_intervals(self, client: Orb) -> None:
        subscription = client.subscriptions.price_intervals(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_method_price_intervals_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.price_intervals(
            subscription_id="subscription_id",
            add=[
                {
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "one_time",
                        "currency": "USD",
                        "expires_at_end_of_cadence": True,
                    },
                    "discounts": [
                        {
                            "amount_discount": 0,
                            "discount_type": "amount",
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "fixed_fee_quantity_transitions": [
                        {
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "quantity": 5,
                        }
                    ],
                    "maximum_amount": 0,
                    "minimum_amount": 0,
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            edit=[
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "billing_cycle_day": 0,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "quantity": 5,
                        }
                    ],
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            edit_adjustments=[
                {
                    "adjustment_interval_id": "sdfs6wdjvn7ujokd",
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_raw_response_price_intervals(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.price_intervals(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_streaming_response_price_intervals(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.price_intervals(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    def test_path_params_price_intervals(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.price_intervals(
                subscription_id="",
            )

    @parametrize
    def test_method_schedule_plan_change(self, client: Orb) -> None:
        subscription = client.subscriptions.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        )
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    def test_method_schedule_plan_change_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "plan_phase_order": 0,
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            add_prices=[
                {
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            align_billing_with_plan_change_date=True,
            auto_collection=True,
            billing_cycle_alignment="unchanged",
            billing_cycle_anchor_configuration={
                "day": 1,
                "month": 1,
                "year": 0,
            },
            change_date=parse_datetime("2017-07-21T17:32:28Z"),
            coupon_redemption_code="coupon_redemption_code",
            credits_overage_rate=0,
            default_invoice_memo="default_invoice_memo",
            external_plan_id="ZMwNQefe7J3ecf7W",
            filter="my_property > 100 AND my_other_property = 'bar'",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            net_terms=0,
            per_credit_overage_amount=0,
            plan_id="ZMwNQefe7J3ecf7W",
            plan_version_number=0,
            price_overrides=[{}],
            remove_adjustments=[{"adjustment_id": "h74gfhdjvn7ujokd"}],
            remove_prices=[
                {
                    "external_price_id": "external_price_id",
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 2,
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            trial_duration_days=0,
        )
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_schedule_plan_change(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_schedule_plan_change(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schedule_plan_change(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.schedule_plan_change(
                subscription_id="",
                change_option="requested_date",
            )

    @parametrize
    def test_method_trigger_phase(self, client: Orb) -> None:
        subscription = client.subscriptions.trigger_phase(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    def test_method_trigger_phase_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.trigger_phase(
            subscription_id="subscription_id",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_trigger_phase(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.trigger_phase(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_trigger_phase(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.trigger_phase(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger_phase(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.trigger_phase(
                subscription_id="",
            )

    @parametrize
    def test_method_unschedule_cancellation(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_cancellation(
            "subscription_id",
        )
        assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_cancellation(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_cancellation(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_cancellation(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_cancellation(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

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
            subscription_id="subscription_id",
            price_id="price_id",
        )
        assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
            subscription_id="subscription_id",
            price_id="price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_fixed_fee_quantity_updates(
            subscription_id="subscription_id",
            price_id="price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
                subscription_id="",
                price_id="price_id",
            )

    @parametrize
    def test_method_unschedule_pending_plan_changes(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_pending_plan_changes(
            "subscription_id",
        )
        assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_unschedule_pending_plan_changes(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unschedule_pending_plan_changes(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.unschedule_pending_plan_changes(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

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
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        )
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    def test_method_update_fixed_fee_quantity_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
            change_option="immediate",
            effective_date=parse_date("2022-12-21"),
        )
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update_fixed_fee_quantity(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update_fixed_fee_quantity(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_fixed_fee_quantity(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_fixed_fee_quantity(
                subscription_id="",
                price_id="price_id",
                quantity=0,
            )

    @parametrize
    def test_method_update_trial(self, client: Orb) -> None:
        subscription = client.subscriptions.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        )
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    def test_method_update_trial_with_all_params(self, client: Orb) -> None:
        subscription = client.subscriptions.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
            shift=True,
        )
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update_trial(self, client: Orb) -> None:
        response = client.subscriptions.with_raw_response.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update_trial(self, client: Orb) -> None:
        with client.subscriptions.with_streaming_response.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_trial(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_trial(
                subscription_id="",
                trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.create()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.create(
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "plan_phase_order": 0,
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            add_prices=[
                {
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            align_billing_with_subscription_start_date=True,
            auto_collection=True,
            aws_region="aws_region",
            billing_cycle_anchor_configuration={
                "day": 1,
                "month": 1,
                "year": 0,
            },
            coupon_redemption_code="coupon_redemption_code",
            credits_overage_rate=0,
            customer_id="customer_id",
            default_invoice_memo="default_invoice_memo",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_customer_id="external_customer_id",
            external_marketplace="google",
            external_marketplace_reporting_id="external_marketplace_reporting_id",
            external_plan_id="ZMwNQefe7J3ecf7W",
            filter="my_property > 100 AND my_other_property = 'bar'",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
            per_credit_overage_amount=0,
            plan_id="ZMwNQefe7J3ecf7W",
            plan_version_number=0,
            price_overrides=[{}],
            remove_adjustments=[{"adjustment_id": "h74gfhdjvn7ujokd"}],
            remove_prices=[
                {
                    "external_price_id": "external_price_id",
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 2,
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            trial_duration_days=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_id="subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_id="subscription_id",
            auto_collection=True,
            default_invoice_memo="default_invoice_memo",
            invoicing_threshold="10.00",
            metadata={"foo": "string"},
            net_terms=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.update(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.update(
            subscription_id="subscription_id",
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
                subscription_id="",
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
            cursor="cursor",
            customer_id=["string"],
            external_customer_id="external_customer_id",
            limit=1,
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
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        )
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
            cancellation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.cancel(
            subscription_id="subscription_id",
            cancel_option="end_of_subscription_term",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCancelResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.cancel(
                subscription_id="",
                cancel_option="end_of_subscription_term",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch(
            "subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch(
            "subscription_id",
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
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_method_fetch_costs_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_costs(
            subscription_id="subscription_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch_costs(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_costs(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_costs(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_costs(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @parametrize
    async def test_method_fetch_schedule(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_schedule(
            subscription_id="subscription_id",
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_method_fetch_schedule_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_schedule(
            subscription_id="subscription_id",
            cursor="cursor",
            limit=1,
            start_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_raw_response_fetch_schedule(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_schedule(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_schedule(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_schedule(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_usage(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.fetch_usage(
            subscription_id="subscription_id",
            billable_metric_id="billable_metric_id",
            first_dimension_key="first_dimension_key",
            first_dimension_value="first_dimension_value",
            granularity="day",
            group_by="group_by",
            second_dimension_key="second_dimension_key",
            second_dimension_value="second_dimension_value",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_raw_response_fetch_usage(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.fetch_usage(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_streaming_response_fetch_usage(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.fetch_usage(
            subscription_id="subscription_id",
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
                subscription_id="",
            )

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.price_intervals(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.price_intervals(
            subscription_id="subscription_id",
            add=[
                {
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "allocation_price": {
                        "amount": "10.00",
                        "cadence": "one_time",
                        "currency": "USD",
                        "expires_at_end_of_cadence": True,
                    },
                    "discounts": [
                        {
                            "amount_discount": 0,
                            "discount_type": "amount",
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "fixed_fee_quantity_transitions": [
                        {
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "quantity": 5,
                        }
                    ],
                    "maximum_amount": 0,
                    "minimum_amount": 0,
                    "price": {
                        "cadence": "annual",
                        "currency": "currency",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            edit=[
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "billing_cycle_day": 0,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "quantity": 5,
                        }
                    ],
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            edit_adjustments=[
                {
                    "adjustment_interval_id": "sdfs6wdjvn7ujokd",
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_raw_response_price_intervals(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.price_intervals(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_streaming_response_price_intervals(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.price_intervals(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionPriceIntervalsResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_path_params_price_intervals(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.price_intervals(
                subscription_id="",
            )

    @parametrize
    async def test_method_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        )
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    async def test_method_schedule_plan_change_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
            add_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "plan_phase_order": 0,
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            add_prices=[
                {
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_price_id": "external_price_id",
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            align_billing_with_plan_change_date=True,
            auto_collection=True,
            billing_cycle_alignment="unchanged",
            billing_cycle_anchor_configuration={
                "day": 1,
                "month": 1,
                "year": 0,
            },
            change_date=parse_datetime("2017-07-21T17:32:28Z"),
            coupon_redemption_code="coupon_redemption_code",
            credits_overage_rate=0,
            default_invoice_memo="default_invoice_memo",
            external_plan_id="ZMwNQefe7J3ecf7W",
            filter="my_property > 100 AND my_other_property = 'bar'",
            initial_phase_order=2,
            invoicing_threshold="10.00",
            net_terms=0,
            per_credit_overage_amount=0,
            plan_id="ZMwNQefe7J3ecf7W",
            plan_version_number=0,
            price_overrides=[{}],
            remove_adjustments=[{"adjustment_id": "h74gfhdjvn7ujokd"}],
            remove_prices=[
                {
                    "external_price_id": "external_price_id",
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            replace_adjustments=[
                {
                    "adjustment": {
                        "adjustment_type": "percentage_discount",
                        "applies_to_price_ids": ["price_1", "price_2"],
                        "percentage_discount": 0,
                        "is_invoice_level": True,
                    },
                    "replaces_adjustment_id": "replaces_adjustment_id",
                }
            ],
            replace_prices=[
                {
                    "replaces_price_id": "replaces_price_id",
                    "discounts": [
                        {
                            "discount_type": "percentage",
                            "amount_discount": "amount_discount",
                            "percentage_discount": 0.15,
                            "usage_discount": 0,
                        }
                    ],
                    "external_price_id": "external_price_id",
                    "fixed_price_quantity": 2,
                    "maximum_amount": "1.23",
                    "minimum_amount": "1.23",
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
                        "external_price_id": "external_price_id",
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "invoice_grouping_key",
                        "invoicing_cycle_configuration": {
                            "duration": 0,
                            "duration_unit": "day",
                        },
                        "metadata": {"foo": "string"},
                        "reference_id": "reference_id",
                    },
                    "price_id": "h74gfhdjvn7ujokd",
                }
            ],
            trial_duration_days=0,
        )
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.schedule_plan_change(
            subscription_id="subscription_id",
            change_option="requested_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionSchedulePlanChangeResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schedule_plan_change(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.schedule_plan_change(
                subscription_id="",
                change_option="requested_date",
            )

    @parametrize
    async def test_method_trigger_phase(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.trigger_phase(
            subscription_id="subscription_id",
        )
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    async def test_method_trigger_phase_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.trigger_phase(
            subscription_id="subscription_id",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_trigger_phase(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.trigger_phase(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_trigger_phase(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.trigger_phase(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionTriggerPhaseResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger_phase(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.trigger_phase(
                subscription_id="",
            )

    @parametrize
    async def test_method_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.unschedule_cancellation(
            "subscription_id",
        )
        assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_cancellation(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_cancellation(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_cancellation(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUnscheduleCancellationResponse, subscription, path=["response"])

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
            subscription_id="subscription_id",
            price_id="price_id",
        )
        assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
            subscription_id="subscription_id",
            price_id="price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_fixed_fee_quantity_updates(
            subscription_id="subscription_id",
            price_id="price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUnscheduleFixedFeeQuantityUpdatesResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unschedule_fixed_fee_quantity_updates(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.unschedule_fixed_fee_quantity_updates(
                subscription_id="",
                price_id="price_id",
            )

    @parametrize
    async def test_method_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.unschedule_pending_plan_changes(
            "subscription_id",
        )
        assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.unschedule_pending_plan_changes(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unschedule_pending_plan_changes(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.unschedule_pending_plan_changes(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUnschedulePendingPlanChangesResponse, subscription, path=["response"])

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
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        )
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    async def test_method_update_fixed_fee_quantity_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
            change_option="immediate",
            effective_date=parse_date("2022-12-21"),
        )
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.update_fixed_fee_quantity(
            subscription_id="subscription_id",
            price_id="price_id",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateFixedFeeQuantityResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_fixed_fee_quantity(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_fixed_fee_quantity(
                subscription_id="",
                price_id="price_id",
                quantity=0,
            )

    @parametrize
    async def test_method_update_trial(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        )
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    async def test_method_update_trial_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.subscriptions.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
            shift=True,
        )
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update_trial(self, async_client: AsyncOrb) -> None:
        response = await async_client.subscriptions.with_raw_response.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update_trial(self, async_client: AsyncOrb) -> None:
        async with async_client.subscriptions.with_streaming_response.update_trial(
            subscription_id="subscription_id",
            trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateTrialResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_trial(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_trial(
                subscription_id="",
                trial_end_date=parse_datetime("2017-07-21T17:32:28Z"),
            )
