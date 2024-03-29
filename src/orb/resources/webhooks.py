# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import hmac
import json
import hashlib
from datetime import datetime, timezone, timedelta

from .._types import (
    HeadersLike,
)
from .._utils import (
    get_required_header,
)
from .._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Orb and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Orb.

        An error will be raised if the webhook payload was not sent by Orb.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, ORB_WEBHOOK_SECRET, on the client class, Orb(webhook_secret='123'), or passed to this function"
            )

        msg_timestamp = get_required_header(headers, "X-Orb-Timestamp")

        # validate the timestamp
        webhook_tolerance = timedelta(minutes=5)
        now = datetime.now(tz=timezone.utc)

        try:
            timestamp = datetime.fromisoformat(msg_timestamp).astimezone()
        except Exception as err:
            raise ValueError("Invalid signature headers. Could not convert to timestamp") from err

        # too old
        if timestamp < (now - webhook_tolerance):
            raise ValueError("Webhook timestamp is too old")

        # too new
        if timestamp > (now + webhook_tolerance):
            raise ValueError("Webhook timestamp is too new")

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        to_sign = f"v1:{msg_timestamp}:{body}".encode("utf-8")
        expected_signature = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).hexdigest()

        msg_signature = get_required_header(headers, "X-Orb-Signature")

        # Signature header can contain multiple signatures delimited by spaces
        passed_sigs = msg_signature.split(" ")

        for versioned_sig in passed_sigs:
            values = versioned_sig.split("=")
            if len(values) != 2:
                # signature is not formatted like {version},{signature}
                continue

            (version, signature) = values

            # Only verify prefix v1
            if version != "v1":
                continue

            if hmac.compare_digest(expected_signature, signature):
                # valid!
                return None

        raise ValueError("None of the given webhook signatures match the expected signature")


class AsyncWebhooks(AsyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Orb and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Orb.

        An error will be raised if the webhook payload was not sent by Orb.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, ORB_WEBHOOK_SECRET, on the client class, Orb(webhook_secret='123'), or passed to this function"
            )

        msg_timestamp = get_required_header(headers, "X-Orb-Timestamp")

        # validate the timestamp
        webhook_tolerance = timedelta(minutes=5)
        now = datetime.now(tz=timezone.utc)

        try:
            timestamp = datetime.fromisoformat(msg_timestamp).astimezone()
        except Exception as err:
            raise ValueError("Invalid signature headers. Could not convert to timestamp") from err

        # too old
        if timestamp < (now - webhook_tolerance):
            raise ValueError("Webhook timestamp is too old")

        # too new
        if timestamp > (now + webhook_tolerance):
            raise ValueError("Webhook timestamp is too new")

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        to_sign = f"v1:{msg_timestamp}:{body}".encode("utf-8")
        expected_signature = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).hexdigest()

        msg_signature = get_required_header(headers, "X-Orb-Signature")

        # Signature header can contain multiple signatures delimited by spaces
        passed_sigs = msg_signature.split(" ")

        for versioned_sig in passed_sigs:
            values = versioned_sig.split("=")
            if len(values) != 2:
                # signature is not formatted like {version},{signature}
                continue

            (version, signature) = values

            # Only verify prefix v1
            if version != "v1":
                continue

            if hmac.compare_digest(expected_signature, signature):
                # valid!
                return None

        raise ValueError("None of the given webhook signatures match the expected signature")
