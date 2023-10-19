# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers.credits import (
    LedgerListResponse,
    LedgerCreateEntryResponse,
    LedgerListByExternalIDResponse,
    LedgerCreateEntryByExteralIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestLedger:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list(
            "string",
        )
        assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list(
            "string",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="string",
            cursor="string",
            entry_status="committed",
            entry_type="increment",
            limit=0,
            minimum_amount="string",
        )
        assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    def test_method_create_entry_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="increment",
            description="string",
            effective_date=parse_date("2019-12-27"),
            expiry_date=parse_date("2019-12-27"),
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "string",
            },
            metadata={},
            per_unit_cost_basis="string",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="decrement",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="string",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
            description="string",
            metadata={},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_with_all_params_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="increment",
            description="string",
            effective_date=parse_date("2019-12-27"),
            expiry_date=parse_date("2019-12-27"),
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "string",
            },
            metadata={},
            per_unit_cost_basis="string",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_with_all_params_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="decrement",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_with_all_params_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="string",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_with_all_params_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
            description="string",
            metadata={},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_exteral_id_with_all_params_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list_by_external_id(
            "string",
        )
        assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list_by_external_id(
            "string",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="string",
            cursor="string",
            entry_status="committed",
            entry_type="increment",
            limit=0,
            minimum_amount="string",
        )
        assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])


class TestAsyncLedger:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.list(
            "string",
        )
        assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.list(
            "string",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="string",
            cursor="string",
            entry_status="committed",
            entry_type="increment",
            limit=0,
            minimum_amount="string",
        )
        assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_overload_1(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_1(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="increment",
            description="string",
            effective_date=parse_date("2019-12-27"),
            expiry_date=parse_date("2019-12-27"),
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "string",
            },
            metadata={},
            per_unit_cost_basis="string",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_overload_2(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_2(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            entry_type="decrement",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_overload_3(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_3(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="string",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_overload_4(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_4(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
            description="string",
            metadata={},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_overload_5(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_5(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_overload_1(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_with_all_params_overload_1(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="increment",
            description="string",
            effective_date=parse_date("2019-12-27"),
            expiry_date=parse_date("2019-12-27"),
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "string",
            },
            metadata={},
            per_unit_cost_basis="string",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_overload_2(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_with_all_params_overload_2(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            entry_type="decrement",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_overload_3(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_with_all_params_overload_3(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            entry_type="expiration_change",
            expiry_date=parse_date("2019-12-27"),
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="string",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_overload_4(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_with_all_params_overload_4(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="void",
            description="string",
            metadata={},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_overload_5(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_exteral_id_with_all_params_overload_5(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.create_entry_by_exteral_id(
            "string",
            amount=0,
            block_id="string",
            entry_type="amendment",
            description="string",
            metadata={},
        )
        assert_matches_type(LedgerCreateEntryByExteralIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_list_by_external_id(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.list_by_external_id(
            "string",
        )
        assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, client: AsyncOrb) -> None:
        ledger = await client.customers.credits.ledger.list_by_external_id(
            "string",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="string",
            cursor="string",
            entry_status="committed",
            entry_type="increment",
            limit=0,
            minimum_amount="string",
        )
        assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])
