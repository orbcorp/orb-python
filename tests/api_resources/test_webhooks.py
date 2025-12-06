# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast
from datetime import datetime, timezone, timedelta

import pytest
import time_machine

from orb import Orb, AsyncOrb

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "2024-03-27T15:42:29.551"
    # Fix: Ensure fake_now matches how webhook timestamps are now parsed (UTC assumption)
    fake_now_dt = datetime.fromisoformat(timestamp)
    if fake_now_dt.tzinfo is None:
        fake_now_dt = fake_now_dt.replace(tzinfo=timezone.utc)
    fake_now = fake_now_dt.astimezone()

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

    def test_microsecond_precision_issue_fixed(self, client: Orb) -> None:
        """Test that the webhook timestamp parsing issue is fixed for the reported examples."""
        import hmac
        import hashlib

        secret = self.secret

        # Test cases from the reported issue - these should all work now
        test_cases = [
            ("2025-08-08T21:35:11.531998+00:00", "2025-08-08T21:35:11.445"),
            ("2025-08-08T21:32:02.585239+00:00", "2025-08-08T21:32:02.497"),
            ("2025-08-08T21:35:42.810490+00:00", "2025-08-08T21:35:42.660"),
        ]

        for _, (system_time_str, webhook_timestamp) in enumerate(test_cases, 1):
            system_time = datetime.fromisoformat(system_time_str)

            # Generate the correct signature
            to_sign = f"v1:{webhook_timestamp}:{self.payload}".encode("utf-8")
            signature = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).hexdigest()

            with time_machine.travel(system_time):
                # This should now work without raising "Webhook timestamp is too new"
                client.webhooks.verify_signature(
                    payload=self.payload,
                    headers={"X-Orb-Timestamp": webhook_timestamp, "X-Orb-Signature": f"v1={signature}"},
                    secret=secret,
                )

                # Also test the unwrap method
                result = client.webhooks.unwrap(
                    payload=self.payload,
                    headers={"X-Orb-Timestamp": webhook_timestamp, "X-Orb-Signature": f"v1={signature}"},
                    secret=secret,
                )
                assert result is not None

    def test_timezone_aware_timestamps_still_work(self, client: Orb) -> None:
        """Test that webhook timestamps with explicit timezone info still work."""
        import hmac
        import hashlib
        from datetime import timezone

        secret = self.secret

        # Test with explicit UTC timezone
        system_time = datetime(2025, 8, 8, 21, 35, 11, 531998, tzinfo=timezone.utc)
        webhook_timestamp = "2025-08-08T21:35:11.445+00:00"  # Explicit UTC

        to_sign = f"v1:{webhook_timestamp}:{self.payload}".encode("utf-8")
        signature = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).hexdigest()

        with time_machine.travel(system_time):
            client.webhooks.verify_signature(
                payload=self.payload,
                headers={"X-Orb-Timestamp": webhook_timestamp, "X-Orb-Signature": f"v1={signature}"},
                secret=secret,
            )

    def test_webhook_timestamp_actually_too_new(self, client: Orb) -> None:
        """Test that webhooks that are genuinely too new are still rejected."""
        import hmac
        import hashlib
        from datetime import timezone

        secret = self.secret

        # Set system time to be much earlier than webhook timestamp (more than 5 minute tolerance)
        system_time = datetime(2025, 8, 8, 21, 30, 0, 0, tzinfo=timezone.utc)
        webhook_timestamp = "2025-08-08T21:36:00.000"  # 6 minutes later - should be rejected

        to_sign = f"v1:{webhook_timestamp}:{self.payload}".encode("utf-8")
        signature = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).hexdigest()

        with time_machine.travel(system_time):
            with pytest.raises(ValueError, match="Webhook timestamp is too new"):
                client.webhooks.verify_signature(
                    payload=self.payload,
                    headers={"X-Orb-Timestamp": webhook_timestamp, "X-Orb-Signature": f"v1={signature}"},
                    secret=secret,
                )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "2024-03-27T15:42:29.551"
    # Fix: Ensure fake_now matches how webhook timestamps are now parsed (UTC assumption)
    fake_now_dt = datetime.fromisoformat(timestamp)
    if fake_now_dt.tzinfo is None:
        fake_now_dt = fake_now_dt.replace(tzinfo=timezone.utc)
    fake_now = fake_now_dt.astimezone()

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
