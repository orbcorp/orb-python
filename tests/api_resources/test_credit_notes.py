# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import CreditNote
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCreditNotes:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        credit_note = client.credit_notes.list()
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        credit_note = client.credit_notes.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        credit_note = client.credit_notes.fetch(
            "string",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])


class TestAsyncCreditNotes:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        credit_note = await client.credit_notes.list()
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        credit_note = await client.credit_notes.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[CreditNote], credit_note, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        credit_note = await client.credit_notes.fetch(
            "string",
        )
        assert_matches_type(CreditNote, credit_note, path=["response"])
