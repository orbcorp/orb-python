# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast
from datetime import datetime, timedelta

import pytest
import time_machine

from orb import Orb, AsyncOrb

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "2024-03-27T15:42:29.551"
    fake_now = datetime.fromisoformat(timestamp).astimezone()

    payload = """{"id": "o4mmewpfNNTnjfZc", "created_at": "2024-03-27T15:42:29+00:00", "type": "resource_event.test", "properties": {"message": "A test webhook from Orb. Happy testing!"}}"""
    signature = "9d25de966891ab0bc18754faf8d83d0980b44ae330fcc130b41a6cf3daf1f391"
    headers = {
        "X-Orb-Timestamp": timestamp,
        "X-Orb-Signature": f"v1={signature}",
    }
    secret = "c-UGKYdnhHh436B_sMouYAPUvXyWpzOdunZBV5dFSD8"

    @time_machine.travel(fake_now)
    def test_unwrap(self, client: Orb) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        client.webhooks.unwrap(payload, headers, secret=secret)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, client: Orb) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret="foo",
            )

        # multiple signatures
        invalid_signature = "my_invalid_signature"
        assert (
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v1={invalid_signature} v1={signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v2={signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v2={signature} v1={signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "2024-03-27T15:42:29.551"
    fake_now = datetime.fromisoformat(timestamp).astimezone()

    payload = """{"id": "o4mmewpfNNTnjfZc", "created_at": "2024-03-27T15:42:29+00:00", "type": "resource_event.test", "properties": {"message": "A test webhook from Orb. Happy testing!"}}"""
    signature = "9d25de966891ab0bc18754faf8d83d0980b44ae330fcc130b41a6cf3daf1f391"
    headers = {
        "X-Orb-Timestamp": timestamp,
        "X-Orb-Signature": f"v1={signature}",
    }
    secret = "c-UGKYdnhHh436B_sMouYAPUvXyWpzOdunZBV5dFSD8"

    @time_machine.travel(fake_now)
    def test_unwrap(self, async_client: AsyncOrb) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        async_client.webhooks.unwrap(payload, headers, secret=secret)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, async_client: Orb) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = async_client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret="foo",
            )

        # multiple signatures
        invalid_signature = "my_invalid_signature"
        assert (
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v1={invalid_signature} v1={signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v2={signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": f"v2={signature} v1={signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "X-Orb-Signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )
