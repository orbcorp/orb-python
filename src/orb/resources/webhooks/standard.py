# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import cast

from ..._types import HeadersLike
from ..._models import construct_type
from ..._resource import SyncAPIResource, AsyncAPIResource
from ._payload_style import check_payload_style
from ...types.webhooks.unwrap_standard_webhook_event import UnwrapStandardWebhookEvent

__all__ = ["Standard", "AsyncStandard"]


class Standard(SyncAPIResource):
    def unwrap_standard(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> UnwrapStandardWebhookEvent:
        """Validates that the given payload was sent by Orb and parses the payload, for an endpoint
        configured for standard payloads."""
        self._client.webhooks.verify_signature(payload=payload, headers=headers, secret=secret)
        body = json.loads(payload)
        check_payload_style(body, expected="standard")
        return cast(
            UnwrapStandardWebhookEvent,
            construct_type(
                type_=UnwrapStandardWebhookEvent,
                value=body,
            ),
        )


class AsyncStandard(AsyncAPIResource):
    def unwrap_standard(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> UnwrapStandardWebhookEvent:
        """Validates that the given payload was sent by Orb and parses the payload, for an endpoint
        configured for standard payloads."""
        self._client.webhooks.verify_signature(payload=payload, headers=headers, secret=secret)
        body = json.loads(payload)
        check_payload_style(body, expected="standard")
        return cast(
            UnwrapStandardWebhookEvent,
            construct_type(
                type_=UnwrapStandardWebhookEvent,
                value=body,
            ),
        )
