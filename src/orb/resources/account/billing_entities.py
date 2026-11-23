# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.account import (
    billing_entity_list_params,
    billing_entity_create_params,
    billing_entity_update_params,
    billing_entity_update_by_external_id_params,
)
from ...types.address_input_param import AddressInputParam
from ...types.account.billing_entity import BillingEntity

__all__ = ["BillingEntities", "AsyncBillingEntities"]


class BillingEntities(SyncAPIResource):
    """
    A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
    registrations.
    """

    @cached_property
    def with_raw_response(self) -> BillingEntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return BillingEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingEntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return BillingEntitiesWithStreamingResponse(self)

    def create(
        self,
        *,
        address: AddressInputParam,
        legal_name: str,
        name: str,
        external_billing_entity_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_create_params.InvoiceSettings] | Omit = omit,
        tax_registrations: Iterable[billing_entity_create_params.TaxRegistration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """
        This endpoint creates a billing entity: a legal entity the account invoices
        from, with its own legal name, address, tax registrations, and invoice settings.
        `external_billing_entity_id` cannot be changed after creation. This endpoint
        requires an admin API key.

        Args:
          address: The address printed on invoices.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          external_billing_entity_id: An optional user-defined ID for this billing entity, unique within the account.
              This cannot be changed after creation.

          invoice_settings: Settings that override the account's for this billing entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/account/billing_entities",
            body=maybe_transform(
                {
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                    "external_billing_entity_id": external_billing_entity_id,
                    "invoice_settings": invoice_settings,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_create_params.BillingEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def update(
        self,
        billing_entity_id: str,
        *,
        address: Optional[AddressInputParam] | Omit = omit,
        default_payment_gateway_connection_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_update_params.InvoiceSettings] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_gateway_connections: Optional[Iterable[billing_entity_update_params.PaymentGatewayConnection]]
        | Omit = omit,
        tax_registrations: Optional[Iterable[billing_entity_update_params.TaxRegistration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint updates a billing entity, including the default one.

        Omitted
        fields keep their value. A change to the name, legal name, address, or tax
        registrations writes a new version of the billing entity; invoices already
        issued keep the version they were issued with. In `invoice_settings`, a null
        `memo` clears it so the billing entity uses the account's memo. An archived
        billing entity cannot be updated until it is unarchived. This endpoint requires
        an admin API key.

        `payment_gateway_connections` is the full set of connections the billing entity
        collects payments through; a connection left out is disconnected from the
        billing entity. If a payment through a connection left out is still in progress,
        the whole update is rejected and can be retried once the payment finishes.

        Args:
          address: Replaces the whole address. Omit it to keep the current one.

          default_payment_gateway_connection_id: The ID of the connection Orb charges when the customer is not mapped to any of
              the billing entity's connections. Required when `payment_gateway_connections`
              has more than one entry.

          invoice_settings: The invoice settings to change. Omitted fields keep their value; null clears a
              field so it inherits the account's setting.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          payment_gateway_connections: The full set of payment gateway connections the billing entity collects payments
              through. Omit it to keep the current ones. Naming another billing entity's
              connection gives this billing entity a connection of its own through the same
              Stripe account or Adyen merchant account.

          tax_registrations: The full list of registrations. Omit it to keep the current ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return self._put(
            path_template("/account/billing_entities/{billing_entity_id}", billing_entity_id=billing_entity_id),
            body=maybe_transform(
                {
                    "address": address,
                    "default_payment_gateway_connection_id": default_payment_gateway_connection_id,
                    "invoice_settings": invoice_settings,
                    "legal_name": legal_name,
                    "name": name,
                    "payment_gateway_connections": payment_gateway_connections,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_update_params.BillingEntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["active", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[BillingEntity]:
        """
        This endpoint returns the account's billing entities, including the default
        billing entity (`is_default: true`), ordered in descending order by creation
        time.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: Only return billing entities with this status. Omit to return both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account/billing_entities",
            page=SyncPage[BillingEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    billing_entity_list_params.BillingEntityListParams,
                ),
            ),
            model=BillingEntity,
        )

    def archive(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint archives a billing entity.

        An archived billing entity cannot be
        updated; invoices already issued keep it. The default billing entity cannot be
        archived. Archiving a billing entity that is already archived returns it
        unchanged. This endpoint requires an admin API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return self._post(
            path_template("/account/billing_entities/{billing_entity_id}/archive", billing_entity_id=billing_entity_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def archive_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint archives a billing entity.

        An archived billing entity cannot be
        updated; invoices already issued keep it. The default billing entity cannot be
        archived. Archiving a billing entity that is already archived returns it
        unchanged. This endpoint requires an admin API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return self._post(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}/archive",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def fetch(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingEntity:
        """
        This endpoint returns a billing entity identified by its ID, or by the
        `external_billing_entity_id` set when it was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return self._get(
            path_template("/account/billing_entities/{billing_entity_id}", billing_entity_id=billing_entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingEntity,
        )

    def fetch_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingEntity:
        """
        This endpoint returns a billing entity identified by its ID, or by the
        `external_billing_entity_id` set when it was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return self._get(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingEntity,
        )

    def unarchive(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint restores an archived billing entity to active.

        Unarchiving an
        active billing entity returns it unchanged. This endpoint requires an admin API
        key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return self._post(
            path_template(
                "/account/billing_entities/{billing_entity_id}/unarchive", billing_entity_id=billing_entity_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def unarchive_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint restores an archived billing entity to active.

        Unarchiving an
        active billing entity returns it unchanged. This endpoint requires an admin API
        key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return self._post(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}/unarchive",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def update_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        address: Optional[AddressInputParam] | Omit = omit,
        default_payment_gateway_connection_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_update_by_external_id_params.InvoiceSettings] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_gateway_connections: Optional[
            Iterable[billing_entity_update_by_external_id_params.PaymentGatewayConnection]
        ]
        | Omit = omit,
        tax_registrations: Optional[Iterable[billing_entity_update_by_external_id_params.TaxRegistration]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint updates a billing entity, including the default one.

        Omitted
        fields keep their value. A change to the name, legal name, address, or tax
        registrations writes a new version of the billing entity; invoices already
        issued keep the version they were issued with. In `invoice_settings`, a null
        `memo` clears it so the billing entity uses the account's memo. An archived
        billing entity cannot be updated until it is unarchived. This endpoint requires
        an admin API key.

        `payment_gateway_connections` is the full set of connections the billing entity
        collects payments through; a connection left out is disconnected from the
        billing entity. If a payment through a connection left out is still in progress,
        the whole update is rejected and can be retried once the payment finishes.

        Args:
          address: Replaces the whole address. Omit it to keep the current one.

          default_payment_gateway_connection_id: The ID of the connection Orb charges when the customer is not mapped to any of
              the billing entity's connections. Required when `payment_gateway_connections`
              has more than one entry.

          invoice_settings: The invoice settings to change. Omitted fields keep their value; null clears a
              field so it inherits the account's setting.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          payment_gateway_connections: The full set of payment gateway connections the billing entity collects payments
              through. Omit it to keep the current ones. Naming another billing entity's
              connection gives this billing entity a connection of its own through the same
              Stripe account or Adyen merchant account.

          tax_registrations: The full list of registrations. Omit it to keep the current ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return self._put(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}",
                external_billing_entity_id=external_billing_entity_id,
            ),
            body=maybe_transform(
                {
                    "address": address,
                    "default_payment_gateway_connection_id": default_payment_gateway_connection_id,
                    "invoice_settings": invoice_settings,
                    "legal_name": legal_name,
                    "name": name,
                    "payment_gateway_connections": payment_gateway_connections,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_update_by_external_id_params.BillingEntityUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )


class AsyncBillingEntities(AsyncAPIResource):
    """
    A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
    registrations.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBillingEntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingEntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncBillingEntitiesWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: AddressInputParam,
        legal_name: str,
        name: str,
        external_billing_entity_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_create_params.InvoiceSettings] | Omit = omit,
        tax_registrations: Iterable[billing_entity_create_params.TaxRegistration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """
        This endpoint creates a billing entity: a legal entity the account invoices
        from, with its own legal name, address, tax registrations, and invoice settings.
        `external_billing_entity_id` cannot be changed after creation. This endpoint
        requires an admin API key.

        Args:
          address: The address printed on invoices.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          external_billing_entity_id: An optional user-defined ID for this billing entity, unique within the account.
              This cannot be changed after creation.

          invoice_settings: Settings that override the account's for this billing entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/account/billing_entities",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                    "external_billing_entity_id": external_billing_entity_id,
                    "invoice_settings": invoice_settings,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_create_params.BillingEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    async def update(
        self,
        billing_entity_id: str,
        *,
        address: Optional[AddressInputParam] | Omit = omit,
        default_payment_gateway_connection_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_update_params.InvoiceSettings] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_gateway_connections: Optional[Iterable[billing_entity_update_params.PaymentGatewayConnection]]
        | Omit = omit,
        tax_registrations: Optional[Iterable[billing_entity_update_params.TaxRegistration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint updates a billing entity, including the default one.

        Omitted
        fields keep their value. A change to the name, legal name, address, or tax
        registrations writes a new version of the billing entity; invoices already
        issued keep the version they were issued with. In `invoice_settings`, a null
        `memo` clears it so the billing entity uses the account's memo. An archived
        billing entity cannot be updated until it is unarchived. This endpoint requires
        an admin API key.

        `payment_gateway_connections` is the full set of connections the billing entity
        collects payments through; a connection left out is disconnected from the
        billing entity. If a payment through a connection left out is still in progress,
        the whole update is rejected and can be retried once the payment finishes.

        Args:
          address: Replaces the whole address. Omit it to keep the current one.

          default_payment_gateway_connection_id: The ID of the connection Orb charges when the customer is not mapped to any of
              the billing entity's connections. Required when `payment_gateway_connections`
              has more than one entry.

          invoice_settings: The invoice settings to change. Omitted fields keep their value; null clears a
              field so it inherits the account's setting.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          payment_gateway_connections: The full set of payment gateway connections the billing entity collects payments
              through. Omit it to keep the current ones. Naming another billing entity's
              connection gives this billing entity a connection of its own through the same
              Stripe account or Adyen merchant account.

          tax_registrations: The full list of registrations. Omit it to keep the current ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return await self._put(
            path_template("/account/billing_entities/{billing_entity_id}", billing_entity_id=billing_entity_id),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "default_payment_gateway_connection_id": default_payment_gateway_connection_id,
                    "invoice_settings": invoice_settings,
                    "legal_name": legal_name,
                    "name": name,
                    "payment_gateway_connections": payment_gateway_connections,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_update_params.BillingEntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["active", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BillingEntity, AsyncPage[BillingEntity]]:
        """
        This endpoint returns the account's billing entities, including the default
        billing entity (`is_default: true`), ordered in descending order by creation
        time.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: Only return billing entities with this status. Omit to return both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account/billing_entities",
            page=AsyncPage[BillingEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    billing_entity_list_params.BillingEntityListParams,
                ),
            ),
            model=BillingEntity,
        )

    async def archive(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint archives a billing entity.

        An archived billing entity cannot be
        updated; invoices already issued keep it. The default billing entity cannot be
        archived. Archiving a billing entity that is already archived returns it
        unchanged. This endpoint requires an admin API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return await self._post(
            path_template("/account/billing_entities/{billing_entity_id}/archive", billing_entity_id=billing_entity_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    async def archive_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint archives a billing entity.

        An archived billing entity cannot be
        updated; invoices already issued keep it. The default billing entity cannot be
        archived. Archiving a billing entity that is already archived returns it
        unchanged. This endpoint requires an admin API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return await self._post(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}/archive",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    async def fetch(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingEntity:
        """
        This endpoint returns a billing entity identified by its ID, or by the
        `external_billing_entity_id` set when it was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return await self._get(
            path_template("/account/billing_entities/{billing_entity_id}", billing_entity_id=billing_entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingEntity,
        )

    async def fetch_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingEntity:
        """
        This endpoint returns a billing entity identified by its ID, or by the
        `external_billing_entity_id` set when it was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return await self._get(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingEntity,
        )

    async def unarchive(
        self,
        billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint restores an archived billing entity to active.

        Unarchiving an
        active billing entity returns it unchanged. This endpoint requires an admin API
        key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not billing_entity_id:
            raise ValueError(f"Expected a non-empty value for `billing_entity_id` but received {billing_entity_id!r}")
        return await self._post(
            path_template(
                "/account/billing_entities/{billing_entity_id}/unarchive", billing_entity_id=billing_entity_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    async def unarchive_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint restores an archived billing entity to active.

        Unarchiving an
        active billing entity returns it unchanged. This endpoint requires an admin API
        key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return await self._post(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}/unarchive",
                external_billing_entity_id=external_billing_entity_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )

    async def update_by_external_id(
        self,
        external_billing_entity_id: str,
        *,
        address: Optional[AddressInputParam] | Omit = omit,
        default_payment_gateway_connection_id: Optional[str] | Omit = omit,
        invoice_settings: Optional[billing_entity_update_by_external_id_params.InvoiceSettings] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_gateway_connections: Optional[
            Iterable[billing_entity_update_by_external_id_params.PaymentGatewayConnection]
        ]
        | Omit = omit,
        tax_registrations: Optional[Iterable[billing_entity_update_by_external_id_params.TaxRegistration]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingEntity:
        """This endpoint updates a billing entity, including the default one.

        Omitted
        fields keep their value. A change to the name, legal name, address, or tax
        registrations writes a new version of the billing entity; invoices already
        issued keep the version they were issued with. In `invoice_settings`, a null
        `memo` clears it so the billing entity uses the account's memo. An archived
        billing entity cannot be updated until it is unarchived. This endpoint requires
        an admin API key.

        `payment_gateway_connections` is the full set of connections the billing entity
        collects payments through; a connection left out is disconnected from the
        billing entity. If a payment through a connection left out is still in progress,
        the whole update is rejected and can be retried once the payment finishes.

        Args:
          address: Replaces the whole address. Omit it to keep the current one.

          default_payment_gateway_connection_id: The ID of the connection Orb charges when the customer is not mapped to any of
              the billing entity's connections. Required when `payment_gateway_connections`
              has more than one entry.

          invoice_settings: The invoice settings to change. Omitted fields keep their value; null clears a
              field so it inherits the account's setting.

          legal_name: The legal name printed on invoices.

          name: An internal name for the billing entity.

          payment_gateway_connections: The full set of payment gateway connections the billing entity collects payments
              through. Omit it to keep the current ones. Naming another billing entity's
              connection gives this billing entity a connection of its own through the same
              Stripe account or Adyen merchant account.

          tax_registrations: The full list of registrations. Omit it to keep the current ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_billing_entity_id:
            raise ValueError(
                f"Expected a non-empty value for `external_billing_entity_id` but received {external_billing_entity_id!r}"
            )
        return await self._put(
            path_template(
                "/account/billing_entities/external_billing_entity_id/{external_billing_entity_id}",
                external_billing_entity_id=external_billing_entity_id,
            ),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "default_payment_gateway_connection_id": default_payment_gateway_connection_id,
                    "invoice_settings": invoice_settings,
                    "legal_name": legal_name,
                    "name": name,
                    "payment_gateway_connections": payment_gateway_connections,
                    "tax_registrations": tax_registrations,
                },
                billing_entity_update_by_external_id_params.BillingEntityUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingEntity,
        )


class BillingEntitiesWithRawResponse:
    def __init__(self, billing_entities: BillingEntities) -> None:
        self._billing_entities = billing_entities

        self.create = _legacy_response.to_raw_response_wrapper(
            billing_entities.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            billing_entities.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            billing_entities.list,
        )
        self.archive = _legacy_response.to_raw_response_wrapper(
            billing_entities.archive,
        )
        self.archive_by_external_id = _legacy_response.to_raw_response_wrapper(
            billing_entities.archive_by_external_id,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            billing_entities.fetch,
        )
        self.fetch_by_external_id = _legacy_response.to_raw_response_wrapper(
            billing_entities.fetch_by_external_id,
        )
        self.unarchive = _legacy_response.to_raw_response_wrapper(
            billing_entities.unarchive,
        )
        self.unarchive_by_external_id = _legacy_response.to_raw_response_wrapper(
            billing_entities.unarchive_by_external_id,
        )
        self.update_by_external_id = _legacy_response.to_raw_response_wrapper(
            billing_entities.update_by_external_id,
        )


class AsyncBillingEntitiesWithRawResponse:
    def __init__(self, billing_entities: AsyncBillingEntities) -> None:
        self._billing_entities = billing_entities

        self.create = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.list,
        )
        self.archive = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.archive,
        )
        self.archive_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.archive_by_external_id,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.fetch,
        )
        self.fetch_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.fetch_by_external_id,
        )
        self.unarchive = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.unarchive,
        )
        self.unarchive_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.unarchive_by_external_id,
        )
        self.update_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            billing_entities.update_by_external_id,
        )


class BillingEntitiesWithStreamingResponse:
    def __init__(self, billing_entities: BillingEntities) -> None:
        self._billing_entities = billing_entities

        self.create = to_streamed_response_wrapper(
            billing_entities.create,
        )
        self.update = to_streamed_response_wrapper(
            billing_entities.update,
        )
        self.list = to_streamed_response_wrapper(
            billing_entities.list,
        )
        self.archive = to_streamed_response_wrapper(
            billing_entities.archive,
        )
        self.archive_by_external_id = to_streamed_response_wrapper(
            billing_entities.archive_by_external_id,
        )
        self.fetch = to_streamed_response_wrapper(
            billing_entities.fetch,
        )
        self.fetch_by_external_id = to_streamed_response_wrapper(
            billing_entities.fetch_by_external_id,
        )
        self.unarchive = to_streamed_response_wrapper(
            billing_entities.unarchive,
        )
        self.unarchive_by_external_id = to_streamed_response_wrapper(
            billing_entities.unarchive_by_external_id,
        )
        self.update_by_external_id = to_streamed_response_wrapper(
            billing_entities.update_by_external_id,
        )


class AsyncBillingEntitiesWithStreamingResponse:
    def __init__(self, billing_entities: AsyncBillingEntities) -> None:
        self._billing_entities = billing_entities

        self.create = async_to_streamed_response_wrapper(
            billing_entities.create,
        )
        self.update = async_to_streamed_response_wrapper(
            billing_entities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            billing_entities.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            billing_entities.archive,
        )
        self.archive_by_external_id = async_to_streamed_response_wrapper(
            billing_entities.archive_by_external_id,
        )
        self.fetch = async_to_streamed_response_wrapper(
            billing_entities.fetch,
        )
        self.fetch_by_external_id = async_to_streamed_response_wrapper(
            billing_entities.fetch_by_external_id,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            billing_entities.unarchive,
        )
        self.unarchive_by_external_id = async_to_streamed_response_wrapper(
            billing_entities.unarchive_by_external_id,
        )
        self.update_by_external_id = async_to_streamed_response_wrapper(
            billing_entities.update_by_external_id,
        )
