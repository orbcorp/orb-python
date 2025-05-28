# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ... import _legacy_response
from ...types import (
    price_list_params,
    price_create_params,
    price_update_params,
    price_evaluate_params,
    price_evaluate_multiple_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ...types.price import Price
from ..._base_client import AsyncPaginator, make_request_options
from .external_price_id import (
    ExternalPriceID,
    AsyncExternalPriceID,
    ExternalPriceIDWithRawResponse,
    AsyncExternalPriceIDWithRawResponse,
    ExternalPriceIDWithStreamingResponse,
    AsyncExternalPriceIDWithStreamingResponse,
)
from ...types.price_evaluate_response import PriceEvaluateResponse
from ...types.price_evaluate_multiple_response import PriceEvaluateMultipleResponse

__all__ = ["Prices", "AsyncPrices"]


class Prices(SyncAPIResource):
    @cached_property
    def external_price_id(self) -> ExternalPriceID:
        return ExternalPriceID(self._client)

    @cached_property
    def with_raw_response(self) -> PricesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return PricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return PricesWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingUnitPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["package"],
        name: str,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingPackagePriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingPackagePriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig,
        model_type: Literal["matrix"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingMatrixPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingMatrixPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_with_allocation_config: price_create_params.NewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig,
        model_type: Literal["matrix_with_allocation"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered"],
        name: str,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingTieredPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingTieredPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_bps"],
        name: str,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingTieredBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredBpsPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredBpsPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingBpsPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBpsPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBulkBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingBulkBpsPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBulkBpsPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBulkPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingBulkPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBulkPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["threshold_total_amount"],
        name: str,
        threshold_total_amount_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package"],
        name: str,
        tiered_package_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_tiered_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_tiered"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        max_group_tiered_package_config: Dict[str, object],
        model_type: Literal["max_group_tiered_package"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_minimum"],
        name: str,
        tiered_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["package_with_allocation"],
        name: str,
        package_with_allocation_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package_with_minimum"],
        name: str,
        tiered_package_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit_with_percent"],
        name: str,
        unit_with_percent_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_proration"],
        name: str,
        tiered_with_proration_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit_with_proration"],
        name: str,
        unit_with_proration_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_allocation_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_allocation"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_with_prorated_minimum_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_with_prorated_minimum"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_with_metered_minimum_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_with_metered_minimum"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_with_display_name_config: Dict[str, object],
        model_type: Literal["matrix_with_display_name"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        bulk_with_proration_config: Dict[str, object],
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_with_proration"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_tiered_package_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_tiered_package"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["scalable_matrix_with_unit_pricing"],
        name: str,
        scalable_matrix_with_unit_pricing_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["scalable_matrix_with_tiered_pricing"],
        name: str,
        scalable_matrix_with_tiered_pricing_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        cumulative_grouped_bulk_config: Dict[str, object],
        currency: str,
        item_id: str,
        model_type: Literal["cumulative_grouped_bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        ["cadence", "currency", "item_id", "matrix_with_allocation_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_bps_config"],
        ["bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "threshold_total_amount_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_config"],
        ["cadence", "currency", "grouped_tiered_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "max_group_tiered_package_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_with_allocation_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "unit_with_percent_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_proration_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "unit_with_proration_config"],
        ["cadence", "currency", "grouped_allocation_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_with_prorated_minimum_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_with_metered_minimum_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "matrix_with_display_name_config", "model_type", "name"],
        ["bulk_with_proration_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_tiered_package_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "scalable_matrix_with_unit_pricing_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "scalable_matrix_with_tiered_pricing_config"],
        ["cadence", "cumulative_grouped_bulk_config", "currency", "item_id", "model_type", "name"],
    )
    def create(
        self,
        *,
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"]
        | Literal["package"]
        | Literal["matrix"]
        | Literal["matrix_with_allocation"]
        | Literal["tiered"]
        | Literal["tiered_bps"]
        | Literal["bps"]
        | Literal["bulk_bps"]
        | Literal["bulk"]
        | Literal["threshold_total_amount"]
        | Literal["tiered_package"]
        | Literal["grouped_tiered"]
        | Literal["max_group_tiered_package"]
        | Literal["tiered_with_minimum"]
        | Literal["package_with_allocation"]
        | Literal["tiered_package_with_minimum"]
        | Literal["unit_with_percent"]
        | Literal["tiered_with_proration"]
        | Literal["unit_with_proration"]
        | Literal["grouped_allocation"]
        | Literal["grouped_with_prorated_minimum"]
        | Literal["grouped_with_metered_minimum"]
        | Literal["matrix_with_display_name"]
        | Literal["bulk_with_proration"]
        | Literal["grouped_tiered_package"]
        | Literal["scalable_matrix_with_unit_pricing"]
        | Literal["scalable_matrix_with_tiered_pricing"]
        | Literal["cumulative_grouped_bulk"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig | NotGiven = NOT_GIVEN,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingUnitPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig | NotGiven = NOT_GIVEN,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig | NotGiven = NOT_GIVEN,
        matrix_with_allocation_config: price_create_params.NewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig
        | NotGiven = NOT_GIVEN,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig | NotGiven = NOT_GIVEN,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig | NotGiven = NOT_GIVEN,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig | NotGiven = NOT_GIVEN,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig | NotGiven = NOT_GIVEN,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig | NotGiven = NOT_GIVEN,
        threshold_total_amount_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_tiered_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        max_group_tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        package_with_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        unit_with_percent_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        unit_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_with_prorated_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_with_metered_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        matrix_with_display_name_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        bulk_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        scalable_matrix_with_unit_pricing_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        scalable_matrix_with_tiered_pricing_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        cumulative_grouped_bulk_config: Dict[str, object] | NotGiven = NOT_GIVEN,
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
                        "billing_cycle_configuration": billing_cycle_configuration,
                        "conversion_rate": conversion_rate,
                        "dimensional_price_configuration": dimensional_price_configuration,
                        "external_price_id": external_price_id,
                        "fixed_price_quantity": fixed_price_quantity,
                        "invoice_grouping_key": invoice_grouping_key,
                        "invoicing_cycle_configuration": invoicing_cycle_configuration,
                        "metadata": metadata,
                        "package_config": package_config,
                        "matrix_config": matrix_config,
                        "matrix_with_allocation_config": matrix_with_allocation_config,
                        "tiered_config": tiered_config,
                        "tiered_bps_config": tiered_bps_config,
                        "bps_config": bps_config,
                        "bulk_bps_config": bulk_bps_config,
                        "bulk_config": bulk_config,
                        "threshold_total_amount_config": threshold_total_amount_config,
                        "tiered_package_config": tiered_package_config,
                        "grouped_tiered_config": grouped_tiered_config,
                        "max_group_tiered_package_config": max_group_tiered_package_config,
                        "tiered_with_minimum_config": tiered_with_minimum_config,
                        "package_with_allocation_config": package_with_allocation_config,
                        "tiered_package_with_minimum_config": tiered_package_with_minimum_config,
                        "unit_with_percent_config": unit_with_percent_config,
                        "tiered_with_proration_config": tiered_with_proration_config,
                        "unit_with_proration_config": unit_with_proration_config,
                        "grouped_allocation_config": grouped_allocation_config,
                        "grouped_with_prorated_minimum_config": grouped_with_prorated_minimum_config,
                        "grouped_with_metered_minimum_config": grouped_with_metered_minimum_config,
                        "matrix_with_display_name_config": matrix_with_display_name_config,
                        "bulk_with_proration_config": bulk_with_proration_config,
                        "grouped_tiered_package_config": grouped_tiered_package_config,
                        "scalable_matrix_with_unit_pricing_config": scalable_matrix_with_unit_pricing_config,
                        "scalable_matrix_with_tiered_pricing_config": scalable_matrix_with_tiered_pricing_config,
                        "cumulative_grouped_bulk_config": cumulative_grouped_bulk_config,
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

    def update(
        self,
        price_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint allows you to update the `metadata` property on a price.

        If you
        pass null for the metadata value, it will clear any existing metadata for that
        price.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return cast(
            Price,
            self._put(
                f"/prices/{price_id}",
                body=maybe_transform({"metadata": metadata}, price_update_params.PriceUpdateParams),
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
        [price creation endpoint](/api-reference/price/create-price).

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

    def evaluate(
        self,
        price_id: str,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        grouping_keys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateResponse:
        """
        [NOTE] It is recommended to use the `/v1/prices/evaluate` which offers further
        functionality, such as multiple prices, inline price definitions, and querying
        over preview events.

        This endpoint is used to evaluate the output of a price for a given customer and
        time range. It enables filtering and grouping the output using
        [computed properties](/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        By default, the start of the time range must be no more than 100 days ago and
        the length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          filter: A boolean
              [computed property](/extensibility/advanced-metrics#computed-properties) used to
              filter the underlying billable metric

          grouping_keys: Properties (or
              [computed properties](/extensibility/advanced-metrics#computed-properties)) used
              to group the underlying billable metric

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return self._post(
            f"/prices/{price_id}/evaluate",
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "filter": filter,
                    "grouping_keys": grouping_keys,
                },
                price_evaluate_params.PriceEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateResponse,
        )

    def evaluate_multiple(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        events: Optional[Iterable[price_evaluate_multiple_params.Event]] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_evaluations: Iterable[price_evaluate_multiple_params.PriceEvaluation] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateMultipleResponse:
        """
        This endpoint is used to evaluate the output of price(s) for a given customer
        and time range over either ingested events or preview events. It enables
        filtering and grouping the output using
        [computed properties](/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        Prices may either reference existing prices in your Orb account or be defined
        inline in the request body. Up to 100 prices can be evaluated in a single
        request.

        Price evaluation by default uses ingested events, but you can also provide a
        list of preview events to use instead. Up to 500 preview events can be provided
        in a single request. When using ingested events, the start of the time range
        must be no more than 100 days ago.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        The length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          events: Optional list of preview events to use instead of actual usage data (max 500)

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          price_evaluations: List of prices to evaluate (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/prices/evaluate",
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "events": events,
                    "external_customer_id": external_customer_id,
                    "price_evaluations": price_evaluations,
                },
                price_evaluate_multiple_params.PriceEvaluateMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateMultipleResponse,
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncPricesWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingUnitPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["package"],
        name: str,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingPackagePriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingPackagePriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig,
        model_type: Literal["matrix"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingMatrixPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingMatrixPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_with_allocation_config: price_create_params.NewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig,
        model_type: Literal["matrix_with_allocation"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered"],
        name: str,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingTieredPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingTieredPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_bps"],
        name: str,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingTieredBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredBpsPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredBpsPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingBpsPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBpsPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_bps"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBulkBpsPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingBulkBpsPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBulkBpsPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingBulkPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingBulkPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingBulkPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["threshold_total_amount"],
        name: str,
        threshold_total_amount_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package"],
        name: str,
        tiered_package_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_tiered_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_tiered"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        max_group_tiered_package_config: Dict[str, object],
        model_type: Literal["max_group_tiered_package"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_minimum"],
        name: str,
        tiered_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["package_with_allocation"],
        name: str,
        package_with_allocation_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_package_with_minimum"],
        name: str,
        tiered_package_with_minimum_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit_with_percent"],
        name: str,
        unit_with_percent_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithPercentPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["tiered_with_proration"],
        name: str,
        tiered_with_proration_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingTieredWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit_with_proration"],
        name: str,
        unit_with_proration_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingUnitWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_allocation_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_allocation"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedAllocationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_with_prorated_minimum_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_with_prorated_minimum"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_with_metered_minimum_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_with_metered_minimum"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        matrix_with_display_name_config: Dict[str, object],
        model_type: Literal["matrix_with_display_name"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        bulk_with_proration_config: Dict[str, object],
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["bulk_with_proration"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingBulkWithProrationPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        grouped_tiered_package_config: Dict[str, object],
        item_id: str,
        model_type: Literal["grouped_tiered_package"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["scalable_matrix_with_unit_pricing"],
        name: str,
        scalable_matrix_with_unit_pricing_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["scalable_matrix_with_tiered_pricing"],
        name: str,
        scalable_matrix_with_tiered_pricing_config: Dict[str, object],
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        cumulative_grouped_bulk_config: Dict[str, object],
        currency: str,
        item_id: str,
        model_type: Literal["cumulative_grouped_bulk"],
        name: str,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[
            price_create_params.NewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """
        This endpoint is used to create a [price](/product-catalog/price-configuration).
        A price created using this endpoint is always an add-on, meaning that it's not
        associated with a specific plan and can instead be individually added to
        subscriptions, including subscriptions on different plans.

        An `external_price_id` can be optionally specified as an alias to allow
        ergonomic interaction with prices in the Orb API.

        See the [Price resource](/product-catalog/price-configuration) for the
        specification of different price model configurations possible in this endpoint.

        Args:
          cadence: The cadence to bill for this price on.

          currency: An ISO 4217 currency string for which this price is billed in.

          item_id: The id of the item the price will be associated with.

          name: The name of the price.

          billable_metric_id: The id of the billable metric for the price. Only needed if the price is
              usage-based.

          billed_in_advance: If the Price represents a fixed cost, the price will be billed in-advance if
              this is true, and in-arrears if this is false.

          billing_cycle_configuration: For custom cadence: specifies the duration of the billing period in days or
              months.

          conversion_rate: The per unit conversion rate of the price currency to the invoicing currency.

          dimensional_price_configuration: For dimensional price: specifies a price group and dimension values

          external_price_id: An alias for the price.

          fixed_price_quantity: If the Price represents a fixed cost, this represents the quantity of units
              applied.

          invoice_grouping_key: The property used to group this price on an invoice

          invoicing_cycle_configuration: Within each billing cycle, specifies the cadence at which invoices are produced.
              If unspecified, a single invoice is produced per billing cycle.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

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
        ["cadence", "currency", "item_id", "matrix_with_allocation_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_bps_config"],
        ["bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_bps_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["bulk_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "threshold_total_amount_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_config"],
        ["cadence", "currency", "grouped_tiered_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "max_group_tiered_package_config", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "package_with_allocation_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_package_with_minimum_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "unit_with_percent_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "tiered_with_proration_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "unit_with_proration_config"],
        ["cadence", "currency", "grouped_allocation_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_with_prorated_minimum_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_with_metered_minimum_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "matrix_with_display_name_config", "model_type", "name"],
        ["bulk_with_proration_config", "cadence", "currency", "item_id", "model_type", "name"],
        ["cadence", "currency", "grouped_tiered_package_config", "item_id", "model_type", "name"],
        ["cadence", "currency", "item_id", "model_type", "name", "scalable_matrix_with_unit_pricing_config"],
        ["cadence", "currency", "item_id", "model_type", "name", "scalable_matrix_with_tiered_pricing_config"],
        ["cadence", "cumulative_grouped_bulk_config", "currency", "item_id", "model_type", "name"],
    )
    async def create(
        self,
        *,
        cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"],
        currency: str,
        item_id: str,
        model_type: Literal["unit"]
        | Literal["package"]
        | Literal["matrix"]
        | Literal["matrix_with_allocation"]
        | Literal["tiered"]
        | Literal["tiered_bps"]
        | Literal["bps"]
        | Literal["bulk_bps"]
        | Literal["bulk"]
        | Literal["threshold_total_amount"]
        | Literal["tiered_package"]
        | Literal["grouped_tiered"]
        | Literal["max_group_tiered_package"]
        | Literal["tiered_with_minimum"]
        | Literal["package_with_allocation"]
        | Literal["tiered_package_with_minimum"]
        | Literal["unit_with_percent"]
        | Literal["tiered_with_proration"]
        | Literal["unit_with_proration"]
        | Literal["grouped_allocation"]
        | Literal["grouped_with_prorated_minimum"]
        | Literal["grouped_with_metered_minimum"]
        | Literal["matrix_with_display_name"]
        | Literal["bulk_with_proration"]
        | Literal["grouped_tiered_package"]
        | Literal["scalable_matrix_with_unit_pricing"]
        | Literal["scalable_matrix_with_tiered_pricing"]
        | Literal["cumulative_grouped_bulk"],
        name: str,
        unit_config: price_create_params.NewFloatingUnitPriceUnitConfig | NotGiven = NOT_GIVEN,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        billed_in_advance: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceBillingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        conversion_rate: Optional[float] | NotGiven = NOT_GIVEN,
        dimensional_price_configuration: Optional[price_create_params.NewFloatingUnitPriceDimensionalPriceConfiguration]
        | NotGiven = NOT_GIVEN,
        external_price_id: Optional[str] | NotGiven = NOT_GIVEN,
        fixed_price_quantity: Optional[float] | NotGiven = NOT_GIVEN,
        invoice_grouping_key: Optional[str] | NotGiven = NOT_GIVEN,
        invoicing_cycle_configuration: Optional[price_create_params.NewFloatingUnitPriceInvoicingCycleConfiguration]
        | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        package_config: price_create_params.NewFloatingPackagePricePackageConfig | NotGiven = NOT_GIVEN,
        matrix_config: price_create_params.NewFloatingMatrixPriceMatrixConfig | NotGiven = NOT_GIVEN,
        matrix_with_allocation_config: price_create_params.NewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig
        | NotGiven = NOT_GIVEN,
        tiered_config: price_create_params.NewFloatingTieredPriceTieredConfig | NotGiven = NOT_GIVEN,
        tiered_bps_config: price_create_params.NewFloatingTieredBpsPriceTieredBpsConfig | NotGiven = NOT_GIVEN,
        bps_config: price_create_params.NewFloatingBpsPriceBpsConfig | NotGiven = NOT_GIVEN,
        bulk_bps_config: price_create_params.NewFloatingBulkBpsPriceBulkBpsConfig | NotGiven = NOT_GIVEN,
        bulk_config: price_create_params.NewFloatingBulkPriceBulkConfig | NotGiven = NOT_GIVEN,
        threshold_total_amount_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_tiered_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        max_group_tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        package_with_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_package_with_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        unit_with_percent_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        tiered_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        unit_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_allocation_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_with_prorated_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_with_metered_minimum_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        matrix_with_display_name_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        bulk_with_proration_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        grouped_tiered_package_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        scalable_matrix_with_unit_pricing_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        scalable_matrix_with_tiered_pricing_config: Dict[str, object] | NotGiven = NOT_GIVEN,
        cumulative_grouped_bulk_config: Dict[str, object] | NotGiven = NOT_GIVEN,
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
                body=await async_maybe_transform(
                    {
                        "cadence": cadence,
                        "currency": currency,
                        "item_id": item_id,
                        "model_type": model_type,
                        "name": name,
                        "unit_config": unit_config,
                        "billable_metric_id": billable_metric_id,
                        "billed_in_advance": billed_in_advance,
                        "billing_cycle_configuration": billing_cycle_configuration,
                        "conversion_rate": conversion_rate,
                        "dimensional_price_configuration": dimensional_price_configuration,
                        "external_price_id": external_price_id,
                        "fixed_price_quantity": fixed_price_quantity,
                        "invoice_grouping_key": invoice_grouping_key,
                        "invoicing_cycle_configuration": invoicing_cycle_configuration,
                        "metadata": metadata,
                        "package_config": package_config,
                        "matrix_config": matrix_config,
                        "matrix_with_allocation_config": matrix_with_allocation_config,
                        "tiered_config": tiered_config,
                        "tiered_bps_config": tiered_bps_config,
                        "bps_config": bps_config,
                        "bulk_bps_config": bulk_bps_config,
                        "bulk_config": bulk_config,
                        "threshold_total_amount_config": threshold_total_amount_config,
                        "tiered_package_config": tiered_package_config,
                        "grouped_tiered_config": grouped_tiered_config,
                        "max_group_tiered_package_config": max_group_tiered_package_config,
                        "tiered_with_minimum_config": tiered_with_minimum_config,
                        "package_with_allocation_config": package_with_allocation_config,
                        "tiered_package_with_minimum_config": tiered_package_with_minimum_config,
                        "unit_with_percent_config": unit_with_percent_config,
                        "tiered_with_proration_config": tiered_with_proration_config,
                        "unit_with_proration_config": unit_with_proration_config,
                        "grouped_allocation_config": grouped_allocation_config,
                        "grouped_with_prorated_minimum_config": grouped_with_prorated_minimum_config,
                        "grouped_with_metered_minimum_config": grouped_with_metered_minimum_config,
                        "matrix_with_display_name_config": matrix_with_display_name_config,
                        "bulk_with_proration_config": bulk_with_proration_config,
                        "grouped_tiered_package_config": grouped_tiered_package_config,
                        "scalable_matrix_with_unit_pricing_config": scalable_matrix_with_unit_pricing_config,
                        "scalable_matrix_with_tiered_pricing_config": scalable_matrix_with_tiered_pricing_config,
                        "cumulative_grouped_bulk_config": cumulative_grouped_bulk_config,
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

    async def update(
        self,
        price_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint allows you to update the `metadata` property on a price.

        If you
        pass null for the metadata value, it will clear any existing metadata for that
        price.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return cast(
            Price,
            await self._put(
                f"/prices/{price_id}",
                body=await async_maybe_transform({"metadata": metadata}, price_update_params.PriceUpdateParams),
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
        [price creation endpoint](/api-reference/price/create-price).

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

    async def evaluate(
        self,
        price_id: str,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        grouping_keys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateResponse:
        """
        [NOTE] It is recommended to use the `/v1/prices/evaluate` which offers further
        functionality, such as multiple prices, inline price definitions, and querying
        over preview events.

        This endpoint is used to evaluate the output of a price for a given customer and
        time range. It enables filtering and grouping the output using
        [computed properties](/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        By default, the start of the time range must be no more than 100 days ago and
        the length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          filter: A boolean
              [computed property](/extensibility/advanced-metrics#computed-properties) used to
              filter the underlying billable metric

          grouping_keys: Properties (or
              [computed properties](/extensibility/advanced-metrics#computed-properties)) used
              to group the underlying billable metric

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return await self._post(
            f"/prices/{price_id}/evaluate",
            body=await async_maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "filter": filter,
                    "grouping_keys": grouping_keys,
                },
                price_evaluate_params.PriceEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateResponse,
        )

    async def evaluate_multiple(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        events: Optional[Iterable[price_evaluate_multiple_params.Event]] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_evaluations: Iterable[price_evaluate_multiple_params.PriceEvaluation] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateMultipleResponse:
        """
        This endpoint is used to evaluate the output of price(s) for a given customer
        and time range over either ingested events or preview events. It enables
        filtering and grouping the output using
        [computed properties](/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        Prices may either reference existing prices in your Orb account or be defined
        inline in the request body. Up to 100 prices can be evaluated in a single
        request.

        Price evaluation by default uses ingested events, but you can also provide a
        list of preview events to use instead. Up to 500 preview events can be provided
        in a single request. When using ingested events, the start of the time range
        must be no more than 100 days ago.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        The length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          events: Optional list of preview events to use instead of actual usage data (max 500)

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          price_evaluations: List of prices to evaluate (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/prices/evaluate",
            body=await async_maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "events": events,
                    "external_customer_id": external_customer_id,
                    "price_evaluations": price_evaluations,
                },
                price_evaluate_multiple_params.PriceEvaluateMultipleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateMultipleResponse,
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
        self.update = _legacy_response.to_raw_response_wrapper(
            prices.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            prices.list,
        )
        self.evaluate = _legacy_response.to_raw_response_wrapper(
            prices.evaluate,
        )
        self.evaluate_multiple = _legacy_response.to_raw_response_wrapper(
            prices.evaluate_multiple,
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
        self.update = _legacy_response.async_to_raw_response_wrapper(
            prices.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            prices.list,
        )
        self.evaluate = _legacy_response.async_to_raw_response_wrapper(
            prices.evaluate,
        )
        self.evaluate_multiple = _legacy_response.async_to_raw_response_wrapper(
            prices.evaluate_multiple,
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
        self.update = to_streamed_response_wrapper(
            prices.update,
        )
        self.list = to_streamed_response_wrapper(
            prices.list,
        )
        self.evaluate = to_streamed_response_wrapper(
            prices.evaluate,
        )
        self.evaluate_multiple = to_streamed_response_wrapper(
            prices.evaluate_multiple,
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
        self.update = async_to_streamed_response_wrapper(
            prices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prices.list,
        )
        self.evaluate = async_to_streamed_response_wrapper(
            prices.evaluate,
        )
        self.evaluate_multiple = async_to_streamed_response_wrapper(
            prices.evaluate_multiple,
        )
        self.fetch = async_to_streamed_response_wrapper(
            prices.fetch,
        )

    @cached_property
    def external_price_id(self) -> AsyncExternalPriceIDWithStreamingResponse:
        return AsyncExternalPriceIDWithStreamingResponse(self._prices.external_price_id)
