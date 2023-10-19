# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

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
api_key = "My API Key"


class TestSubscriptions:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
            metadata={},
            net_terms=0,
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

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
    def test_method_fetch(self, client: Orb) -> None:
        subscription = client.subscriptions.fetch(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

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
            group_by="string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

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
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

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
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

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
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

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
    def test_method_unschedule_cancellation(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_cancellation(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_unschedule_fixed_fee_quantity_updates(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_unschedule_pending_plan_changes(self, client: Orb) -> None:
        subscription = client.subscriptions.unschedule_pending_plan_changes(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

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


class TestAsyncSubscriptions:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.create()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.create(
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
            metadata={},
            net_terms=0,
            per_credit_overage_amount="string",
            plan_id="ZMwNQefe7J3ecf7W",
            price_overrides=[
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
            ],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.list()
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.list(
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
    async def test_method_cancel(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.cancel(
            "string",
            cancel_option="end_of_subscription_term",
            cancellation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_fetch_costs(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_costs(
            "string",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_method_fetch_costs_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_costs(
            "string",
            group_by="string",
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionFetchCostsResponse, subscription, path=["response"])

    @parametrize
    async def test_method_fetch_schedule(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_schedule(
            "string",
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @parametrize
    async def test_method_fetch_schedule_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_schedule(
            "string",
            cursor="string",
            limit=0,
            start_date_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[SubscriptionFetchScheduleResponse], subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_usage(
            "string",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_fetch_usage_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.fetch_usage(
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
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            view_mode="periodic",
        )
        assert_matches_type(SubscriptionUsage, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.price_intervals(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Incorrect example breaks Prism")
    @parametrize
    async def test_method_price_intervals_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.price_intervals(
            "string",
            add=[
                {
                    "price_id": "h74gfhdjvn7ujokd",
                    "external_price_id": "external_price_id",
                    "price": {
                        "external_price_id": "string",
                        "name": "Annual fee",
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                        "currency": "string",
                        "billable_metric_id": "string",
                        "item_id": "string",
                        "billed_in_advance": True,
                        "fixed_price_quantity": 0,
                        "invoice_grouping_key": "string",
                        "cadence": "annual",
                        "model_type": "unit",
                        "unit_config": {
                            "unit_amount": "string",
                            "scaling_factor": 0,
                        },
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
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
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
                {
                    "price_interval_id": "sdfs6wdjvn7ujokd",
                    "start_date": parse_datetime("2023-05-01"),
                    "end_date": parse_datetime("2023-07-10"),
                    "fixed_fee_quantity_transitions": [
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                        {
                            "quantity": 5,
                            "effective_date": parse_date("2023-05-01"),
                        },
                    ],
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_schedule_plan_change(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.schedule_plan_change(
            "string",
            change_option="requested_date",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_schedule_plan_change_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.schedule_plan_change(
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
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
                {
                    "id": "string",
                    "model_type": "unit",
                    "minimum_amount": "1.23",
                    "maximum_amount": "1.23",
                    "discount": {
                        "discount_type": "percentage",
                        "percentage_discount": 0.15,
                        "trial_amount_discount": "string",
                        "usage_discount": 0,
                        "amount_discount": "string",
                        "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                    },
                    "fixed_price_quantity": 2,
                    "unit_config": {
                        "unit_amount": "string",
                        "scaling_factor": 0,
                    },
                },
            ],
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_trigger_phase(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.trigger_phase(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_trigger_phase_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.trigger_phase(
            "string",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_unschedule_cancellation(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.unschedule_cancellation(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_unschedule_fixed_fee_quantity_updates(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.unschedule_fixed_fee_quantity_updates(
            "string",
            price_id="string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_unschedule_pending_plan_changes(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.unschedule_pending_plan_changes(
            "string",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_fixed_fee_quantity(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_fixed_fee_quantity_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.subscriptions.update_fixed_fee_quantity(
            "string",
            price_id="string",
            quantity=0,
            change_option="immediate",
            effective_date=parse_date("2022-12-21"),
        )
        assert_matches_type(Subscription, subscription, path=["response"])
