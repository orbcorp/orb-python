# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import cast

__all__ = ["check_payload_style"]


def check_payload_style(body: object, *, expected: str) -> None:
    """Raises when a payload was rendered in a style the calling method doesn't parse, rather than
    letting it parse into a type whose fields it doesn't carry. Payloads from before payload
    styles existed carry no `payload_style` and are expanded."""
    style = cast("dict[str, object]", body).get("payload_style", "expanded") if isinstance(body, dict) else None
    if style == expected:
        return
    method = "webhooks.standard.unwrap_standard" if style == "standard" else "webhooks.unwrap"
    raise ValueError(
        f"This webhook payload has payload_style {style!r}, but this method parses {expected!r} payloads. "
        f"Use `{method}` for an endpoint configured for {style!r} payloads."
    )
