# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

import httpx

from ...types import Plan
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...types.plans import external_plan_id_update_params
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["ExternalPlanID", "AsyncExternalPlanID"]


class ExternalPlanID(SyncAPIResource):
    with_raw_response: ExternalPlanIDWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = ExternalPlanIDWithRawResponse(self)

    def update(
        self,
        other_external_plan_id: str,
        *,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given an external_plan_id identifier. It returns information about the
        prices included in the plan and their configuration, as well as the product that
        the plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price).

        Args:
          external_plan_id: An optional user-defined ID for this plan resource, used throughout the system
              as an alias for this Plan. Use this field to identify a plan by an existing
              identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._put(
            f"/plans/external_plan_id/{other_external_plan_id}",
            body=maybe_transform(
                {
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                },
                external_plan_id_update_params.ExternalPlanIDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    def fetch(
        self,
        external_plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given an external_plan_id identifier. It returns information about the
        prices included in the plan and their configuration, as well as the product that
        the plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price). "

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/plans/external_plan_id/{external_plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )


class AsyncExternalPlanID(AsyncAPIResource):
    with_raw_response: AsyncExternalPlanIDWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExternalPlanIDWithRawResponse(self)

    async def update(
        self,
        other_external_plan_id: str,
        *,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given an external_plan_id identifier. It returns information about the
        prices included in the plan and their configuration, as well as the product that
        the plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price).

        Args:
          external_plan_id: An optional user-defined ID for this plan resource, used throughout the system
              as an alias for this Plan. Use this field to identify a plan by an existing
              identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._put(
            f"/plans/external_plan_id/{other_external_plan_id}",
            body=maybe_transform(
                {
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                },
                external_plan_id_update_params.ExternalPlanIDUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    async def fetch(
        self,
        external_plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given an external_plan_id identifier. It returns information about the
        prices included in the plan and their configuration, as well as the product that
        the plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price). "

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/plans/external_plan_id/{external_plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )


class ExternalPlanIDWithRawResponse:
    def __init__(self, external_plan_id: ExternalPlanID) -> None:
        self.update = to_raw_response_wrapper(
            external_plan_id.update,
        )
        self.fetch = to_raw_response_wrapper(
            external_plan_id.fetch,
        )


class AsyncExternalPlanIDWithRawResponse:
    def __init__(self, external_plan_id: AsyncExternalPlanID) -> None:
        self.update = async_to_raw_response_wrapper(
            external_plan_id.update,
        )
        self.fetch = async_to_raw_response_wrapper(
            external_plan_id.fetch,
        )
