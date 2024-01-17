# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Dict, Optional, cast, overload
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import Price, price_list_params, price_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .external_price_id import (
    ExternalPriceID,
    AsyncExternalPriceID,
    ExternalPriceIDWithRawResponse,
    AsyncExternalPriceIDWithRawResponse,
    ExternalPriceIDWithStreamingResponse,
    AsyncExternalPriceIDWithStreamingResponse,
)

__all__ = ["Prices", "AsyncPrices"]


class Prices(SyncAPIResource):
    @cached_property
    def external_price_id(self) -> ExternalPriceID:
        return ExternalPriceID(self._client)

    @cached_property
    def with_raw_response(self) -> PricesWithRawResponse:
        return PricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesWithStreamingResponse:
        return PricesWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["package"],
        name: str,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig,
        model_type: Literal["matrix"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered"],
        name: str,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_bps"],
        name: str,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["threshold_total_amount"],
        name: str,
        threshold_total_amount_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package"],
        name: str,
        tiered_package_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_minimum"],
        name: str,
        tiered_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["package_with_allocation"],
        name: str,
        package_with_allocation_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["cadence", "currency", "item_id", "model_type", "name", "unit_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_config"],
        ["cadence", "currency", "item_id", "matrix_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_bps_config"],
        ["bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "threshold_total_amount_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_with_allocation_config"],
    )
    def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"]
        | Literal["package"]
        | Literal["matrix"]
        | Literal["tiered"]
        | Literal["tiered_bps"]
        | Literal["bps"]
        | Literal["bulk_bps"]
        | Literal["bulk"]
        | Literal["threshold_total_amount"]
        | Literal["tiered_package"]
        | Literal["tiered_with_minimum"]
        | Literal["package_with_allocation"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig | NotGiven = NOT_GIVEN,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig | NotGiven = NOT_GIVEN,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig | NotGiven = NOT_GIVEN,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig | NotGiven = NOT_GIVEN,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig | NotGiven = NOT_GIVEN,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig | NotGiven = NOT_GIVEN,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig | NotGiven = NOT_GIVEN,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig | NotGiven = NOT_GIVEN,
        threshold_total_amount_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        package_with_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        return cast(
            Price,
            self._post(
                "/prices",
                body=maybe_transform(
                    {
                        "cadence": cadence,
                        "currency": currency,
                        "item_id": item_id,
                        "model_type": model_type,
                        "name": name,
                        "unit_config": unit_config,
                        "billable_metric_id": billable_metric_id,
                        "billed_in_advance": billed_in_advance,
                        "external_price_id": external_price_id,
                        "fixed_price_quantity": fixed_price_quantity,
                        "invoice_grouping_key": invoice_grouping_key,
                        "package_config": package_config,
                        "matrix_config": matrix_config,
                        "tiered_config": tiered_config,
                        "tiered_bps_config": tiered_bps_config,
                        "bps_config": bps_config,
                        "bulk_bps_config": bulk_bps_config,
                        "bulk_config": bulk_config,
                        "threshold_total_amount_config": threshold_total_amount_config,
                        "tiered_package_config": tiered_package_config,
                        "tiered_with_minimum_config": tiered_with_minimum_config,
                        "package_with_allocation_config": package_with_allocation_config,
                    },
                    price_create_params.PriceCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Price]:
        """
        This endpoint is used to list all add-on prices created using the
        [price creation endpoint](../reference/create-price).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/prices",
            page=SyncPage[Price],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            model=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
        )

    def fetch(
        self,
        price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Price:
        """
        This endpoint returns a price given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return cast(
            Price,
            self._get(
                f"/prices/{price_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPrices(AsyncAPIResource):
    @cached_property
    def external_price_id(self) -> AsyncExternalPriceID:
        return AsyncExternalPriceID(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPricesWithRawResponse:
        return AsyncPricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesWithStreamingResponse:
        return AsyncPricesWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["package"],
        name: str,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig,
        model_type: Literal["matrix"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered"],
        name: str,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_bps"],
        name: str,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["threshold_total_amount"],
        name: str,
        threshold_total_amount_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package"],
        name: str,
        tiered_package_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_minimum"],
        name: str,
        tiered_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["package_with_allocation"],
        name: str,
        package_with_allocation_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint is used to create a [price](../reference/price).

        A price created
        using this endpoint is always an add-on, meaning that it’s not associated with a
        specific plan and can instead be individually added to subscriptions, including
        subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](../reference/price) for the specification of different
        price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the plan will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["cadence", "currency", "item_id", "model_type", "name", "unit_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_config"],
        ["cadence", "currency", "item_id", "matrix_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_bps_config"],
        ["bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "threshold_total_amount_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_with_allocation_config"],
    )
    async def create(
        self,
        *,
        cadence: Literal["annual", "monthly", "quarterly", "one_time"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"]
        | Literal["package"]
        | Literal["matrix"]
        | Literal["tiered"]
        | Literal["tiered_bps"]
        | Literal["bps"]
        | Literal["bulk_bps"]
        | Literal["bulk"]
        | Literal["threshold_total_amount"]
        | Literal["tiered_package"]
        | Literal["tiered_with_minimum"]
        | Literal["package_with_allocation"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig | NotGiven = NOT_GIVEN,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig | NotGiven = NOT_GIVEN,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig | NotGiven = NOT_GIVEN,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig | NotGiven = NOT_GIVEN,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig | NotGiven = NOT_GIVEN,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig | NotGiven = NOT_GIVEN,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig | NotGiven = NOT_GIVEN,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig | NotGiven = NOT_GIVEN,
        threshold_total_amount_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        package_with_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        return cast(
            Price,
            await self._post(
                "/prices",
                body=maybe_transform(
                    {
                        "cadence": cadence,
                        "currency": currency,
                        "item_id": item_id,
                        "model_type": model_type,
                        "name": name,
                        "unit_config": unit_config,
                        "billable_metric_id": billable_metric_id,
                        "billed_in_advance": billed_in_advance,
                        "external_price_id": external_price_id,
                        "fixed_price_quantity": fixed_price_quantity,
                        "invoice_grouping_key": invoice_grouping_key,
                        "package_config": package_config,
                        "matrix_config": matrix_config,
                        "tiered_config": tiered_config,
                        "tiered_bps_config": tiered_bps_config,
                        "bps_config": bps_config,
                        "bulk_bps_config": bulk_bps_config,
                        "bulk_config": bulk_config,
                        "threshold_total_amount_config": threshold_total_amount_config,
                        "tiered_package_config": tiered_package_config,
                        "tiered_with_minimum_config": tiered_with_minimum_config,
                        "package_with_allocation_config": package_with_allocation_config,
                    },
                    price_create_params.PriceCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Price, AsyncPage[Price]]:
        """
        This endpoint is used to list all add-on prices created using the
        [price creation endpoint](../reference/create-price).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/prices",
            page=AsyncPage[Price],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            model=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
        )

    async def fetch(
        self,
        price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Price:
        """
        This endpoint returns a price given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return cast(
            Price,
            await self._get(
                f"/prices/{price_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PricesWithRawResponse:
    def __init__(self, prices: Prices) -> None:
        self._prices = prices

        self.create = _legacy_response.to_raw_response_wrapper(
            prices.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            prices.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            prices.fetch,
        )

    @cached_property
    def external_price_id(self) -> ExternalPriceIDWithRawResponse:
        return ExternalPriceIDWithRawResponse(self._prices.external_price_id)


class AsyncPricesWithRawResponse:
    def __init__(self, prices: AsyncPrices) -> None:
        self._prices = prices

        self.create = _legacy_response.async_to_raw_response_wrapper(
            prices.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            prices.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            prices.fetch,
        )

    @cached_property
    def external_price_id(self) -> AsyncExternalPriceIDWithRawResponse:
        return AsyncExternalPriceIDWithRawResponse(self._prices.external_price_id)


class PricesWithStreamingResponse:
    def __init__(self, prices: Prices) -> None:
        self._prices = prices

        self.create = to_streamed_response_wrapper(
            prices.create,
        )
        self.list = to_streamed_response_wrapper(
            prices.list,
        )
        self.fetch = to_streamed_response_wrapper(
            prices.fetch,
        )

    @cached_property
    def external_price_id(self) -> ExternalPriceIDWithStreamingResponse:
        return ExternalPriceIDWithStreamingResponse(self._prices.external_price_id)


class AsyncPricesWithStreamingResponse:
    def __init__(self, prices: AsyncPrices) -> None:
        self._prices = prices

        self.create = async_to_streamed_response_wrapper(
            prices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prices.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            prices.fetch,
        )

    @cached_property
    def external_price_id(self) -> AsyncExternalPriceIDWithStreamingResponse:
        return AsyncExternalPriceIDWithStreamingResponse(self._prices.external_price_id)
