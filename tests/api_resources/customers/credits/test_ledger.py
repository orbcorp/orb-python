# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_date, parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers.credits import (
    LedgerListResponse,
    LedgerCreateEntryResponse,
    LedgerListByExternalIDResponse,
    LedgerCreateEntryByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedger:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list(
            customer_id="customer_id",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            cursor="cursor",
            entry_status="committed",
            entry_type="increment",
            limit=1,
            minimum_amount="minimum_amount",
        )
        assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(SyncPage[LedgerListResponse], ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_create_entry_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
            currency="currency",
            description="description",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "item_id",
                    "operator": "includes",
                    "values": ["string"],
                }
            ],
            invoice_settings={
                "auto_collection": True,
                "custom_due_date": parse_date("2019-12-27"),
                "invoice_date": parse_date("2019-12-27"),
                "item_id": "item_id",
                "memo": "memo",
                "net_terms": 0,
                "require_successful_payment": True,
            },
            metadata={"foo": "string"},
            per_unit_cost_basis="per_unit_cost_basis",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_overload_1(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_overload_1(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_overload_1(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                entry_type="increment",
            )

    @parametrize
    def test_method_create_entry_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_overload_2(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_overload_2(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_overload_2(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                entry_type="decrement",
            )

    @parametrize
    def test_method_create_entry_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="block_id",
            currency="currency",
            description="description",
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_overload_3(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_overload_3(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_overload_3(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                entry_type="expiration_change",
                target_expiry_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_create_entry_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_overload_4(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_overload_4(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_overload_4(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="void",
            )

    @parametrize
    def test_method_create_entry_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_with_all_params_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_overload_5(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_overload_5(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_overload_5(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="amendment",
            )

    @parametrize
    def test_method_create_entry_by_external_id_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_external_id_with_all_params_overload_1(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
            currency="currency",
            description="description",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "item_id",
                    "operator": "includes",
                    "values": ["string"],
                }
            ],
            invoice_settings={
                "auto_collection": True,
                "custom_due_date": parse_date("2019-12-27"),
                "invoice_date": parse_date("2019-12-27"),
                "item_id": "item_id",
                "memo": "memo",
                "net_terms": 0,
                "require_successful_payment": True,
            },
            metadata={"foo": "string"},
            per_unit_cost_basis="per_unit_cost_basis",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_by_external_id_overload_1(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_by_external_id_overload_1(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_by_external_id_overload_1(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                entry_type="increment",
            )

    @parametrize
    def test_method_create_entry_by_external_id_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_external_id_with_all_params_overload_2(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_by_external_id_overload_2(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_by_external_id_overload_2(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_by_external_id_overload_2(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                entry_type="decrement",
            )

    @parametrize
    def test_method_create_entry_by_external_id_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_external_id_with_all_params_overload_3(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="block_id",
            currency="currency",
            description="description",
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_by_external_id_overload_3(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_by_external_id_overload_3(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_by_external_id_overload_3(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                entry_type="expiration_change",
                target_expiry_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_create_entry_by_external_id_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_external_id_with_all_params_overload_4(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_by_external_id_overload_4(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_by_external_id_overload_4(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_by_external_id_overload_4(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="void",
            )

    @parametrize
    def test_method_create_entry_by_external_id_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_method_create_entry_by_external_id_with_all_params_overload_5(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_raw_response_create_entry_by_external_id_overload_5(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    def test_streaming_response_create_entry_by_external_id_overload_5(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_entry_by_external_id_overload_5(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="amendment",
            )

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        ledger = client.customers.credits.ledger.list_by_external_id(
            external_customer_id="external_customer_id",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            cursor="cursor",
            entry_status="committed",
            entry_type="increment",
            limit=1,
            minimum_amount="minimum_amount",
        )
        assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.ledger.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.ledger.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = response.parse()
            assert_matches_type(SyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.ledger.with_raw_response.list_by_external_id(
                external_customer_id="",
            )


class TestAsyncLedger:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.list(
            customer_id="customer_id",
        )
        assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.list(
            customer_id="customer_id",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            cursor="cursor",
            entry_status="committed",
            entry_type="increment",
            limit=1,
            minimum_amount="minimum_amount",
        )
        assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(AsyncPage[LedgerListResponse], ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_create_entry_overload_1(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_1(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
            currency="currency",
            description="description",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "item_id",
                    "operator": "includes",
                    "values": ["string"],
                }
            ],
            invoice_settings={
                "auto_collection": True,
                "custom_due_date": parse_date("2019-12-27"),
                "invoice_date": parse_date("2019-12-27"),
                "item_id": "item_id",
                "memo": "memo",
                "net_terms": 0,
                "require_successful_payment": True,
            },
            metadata={"foo": "string"},
            per_unit_cost_basis="per_unit_cost_basis",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_overload_1(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_overload_1(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_overload_1(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                entry_type="increment",
            )

    @parametrize
    async def test_method_create_entry_overload_2(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_2(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_overload_2(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_overload_2(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            entry_type="decrement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_overload_2(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                entry_type="decrement",
            )

    @parametrize
    async def test_method_create_entry_overload_3(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_3(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="block_id",
            currency="currency",
            description="description",
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_overload_3(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_overload_3(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_overload_3(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                entry_type="expiration_change",
                target_expiry_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_create_entry_overload_4(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_4(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_overload_4(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_overload_4(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_overload_4(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="void",
            )

    @parametrize
    async def test_method_create_entry_overload_5(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_with_all_params_overload_5(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_overload_5(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_overload_5(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry(
            customer_id="customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_overload_5(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry(
                customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="amendment",
            )

    @parametrize
    async def test_method_create_entry_by_external_id_overload_1(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_external_id_with_all_params_overload_1(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
            currency="currency",
            description="description",
            effective_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "item_id",
                    "operator": "includes",
                    "values": ["string"],
                }
            ],
            invoice_settings={
                "auto_collection": True,
                "custom_due_date": parse_date("2019-12-27"),
                "invoice_date": parse_date("2019-12-27"),
                "item_id": "item_id",
                "memo": "memo",
                "net_terms": 0,
                "require_successful_payment": True,
            },
            metadata={"foo": "string"},
            per_unit_cost_basis="per_unit_cost_basis",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_by_external_id_overload_1(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_by_external_id_overload_1(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_by_external_id_overload_1(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                entry_type="increment",
            )

    @parametrize
    async def test_method_create_entry_by_external_id_overload_2(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_external_id_with_all_params_overload_2(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_by_external_id_overload_2(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_by_external_id_overload_2(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            entry_type="decrement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_by_external_id_overload_2(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                entry_type="decrement",
            )

    @parametrize
    async def test_method_create_entry_by_external_id_overload_3(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_external_id_with_all_params_overload_3(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
            amount=0,
            block_id="block_id",
            currency="currency",
            description="description",
            expiry_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_by_external_id_overload_3(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_by_external_id_overload_3(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            entry_type="expiration_change",
            target_expiry_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_by_external_id_overload_3(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                entry_type="expiration_change",
                target_expiry_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_create_entry_by_external_id_overload_4(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_external_id_with_all_params_overload_4(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
            void_reason="refund",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_by_external_id_overload_4(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_by_external_id_overload_4(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="void",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_by_external_id_overload_4(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="void",
            )

    @parametrize
    async def test_method_create_entry_by_external_id_overload_5(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_method_create_entry_by_external_id_with_all_params_overload_5(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
            currency="currency",
            description="description",
            metadata={"foo": "string"},
        )
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_raw_response_create_entry_by_external_id_overload_5(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

    @parametrize
    async def test_streaming_response_create_entry_by_external_id_overload_5(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.create_entry_by_external_id(
            external_customer_id="external_customer_id",
            amount=0,
            block_id="block_id",
            entry_type="amendment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(LedgerCreateEntryByExternalIDResponse, ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_entry_by_external_id_overload_5(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.create_entry_by_external_id(
                external_customer_id="",
                amount=0,
                block_id="block_id",
                entry_type="amendment",
            )

    @parametrize
    async def test_method_list_by_external_id(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        ledger = await async_client.customers.credits.ledger.list_by_external_id(
            external_customer_id="external_customer_id",
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="currency",
            cursor="cursor",
            entry_status="committed",
            entry_type="increment",
            limit=1,
            minimum_amount="minimum_amount",
        )
        assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.ledger.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger = response.parse()
        assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.ledger.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger = await response.parse()
            assert_matches_type(AsyncPage[LedgerListByExternalIDResponse], ledger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.ledger.with_raw_response.list_by_external_id(
                external_customer_id="",
            )
