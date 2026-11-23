# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.account import (
    BillingEntity,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.create(
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            legal_name="x",
            name="x",
            external_billing_entity_id="x",
            invoice_settings={"memo": "memo"},
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.update(
            billing_entity_id="billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.update(
            billing_entity_id="billing_entity_id",
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            default_payment_gateway_connection_id="default_payment_gateway_connection_id",
            invoice_settings={"memo": "memo"},
            legal_name="x",
            name="x",
            payment_gateway_connections=[
                {
                    "payment_gateway_connection_id": "payment_gateway_connection_id",
                    "payment_provider_type": "stripe",
                }
            ],
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.update(
            billing_entity_id="billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.update(
            billing_entity_id="billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            client.account.billing_entities.with_raw_response.update(
                billing_entity_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.list()
        assert_matches_type(SyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.list(
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(SyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(SyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(SyncPage[BillingEntity], billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.archive(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.archive(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.archive(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            client.account.billing_entities.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_archive_by_external_id(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.archive_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_archive_by_external_id(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.archive_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_archive_by_external_id(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.archive_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive_by_external_id(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            client.account.billing_entities.with_raw_response.archive_by_external_id(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.fetch(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.fetch(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.fetch(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            client.account.billing_entities.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_by_external_id(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.fetch_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_fetch_by_external_id(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.fetch_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_fetch_by_external_id(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.fetch_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_by_external_id(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            client.account.billing_entities.with_raw_response.fetch_by_external_id(
                "",
            )

    @parametrize
    def test_method_unarchive(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.unarchive(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_unarchive(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.unarchive(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_unarchive(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.unarchive(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            client.account.billing_entities.with_raw_response.unarchive(
                "",
            )

    @parametrize
    def test_method_unarchive_by_external_id(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.unarchive_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_unarchive_by_external_id(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.unarchive_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_unarchive_by_external_id(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.unarchive_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive_by_external_id(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            client.account.billing_entities.with_raw_response.unarchive_by_external_id(
                "",
            )

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        billing_entity = client.account.billing_entities.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            default_payment_gateway_connection_id="default_payment_gateway_connection_id",
            invoice_settings={"memo": "memo"},
            legal_name="x",
            name="x",
            payment_gateway_connections=[
                {
                    "payment_gateway_connection_id": "payment_gateway_connection_id",
                    "payment_provider_type": "stripe",
                }
            ],
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.account.billing_entities.with_raw_response.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    def test_streaming_response_update_by_external_id(self, client: Orb) -> None:
        with client.account.billing_entities.with_streaming_response.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_external_id(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            client.account.billing_entities.with_raw_response.update_by_external_id(
                external_billing_entity_id="",
            )


class TestAsyncBillingEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.create(
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            legal_name="x",
            name="x",
            external_billing_entity_id="x",
            invoice_settings={"memo": "memo"},
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.create(
            address={"country": "x"},
            legal_name="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.update(
            billing_entity_id="billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.update(
            billing_entity_id="billing_entity_id",
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            default_payment_gateway_connection_id="default_payment_gateway_connection_id",
            invoice_settings={"memo": "memo"},
            legal_name="x",
            name="x",
            payment_gateway_connections=[
                {
                    "payment_gateway_connection_id": "payment_gateway_connection_id",
                    "payment_provider_type": "stripe",
                }
            ],
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.update(
            billing_entity_id="billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.update(
            billing_entity_id="billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            await async_client.account.billing_entities.with_raw_response.update(
                billing_entity_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.list()
        assert_matches_type(AsyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.list(
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(AsyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(AsyncPage[BillingEntity], billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(AsyncPage[BillingEntity], billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.archive(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.archive(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.archive(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            await async_client.account.billing_entities.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_archive_by_external_id(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.archive_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_archive_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.archive_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.archive_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            await async_client.account.billing_entities.with_raw_response.archive_by_external_id(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.fetch(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.fetch(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.fetch(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            await async_client.account.billing_entities.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.fetch_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.fetch_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.fetch_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            await async_client.account.billing_entities.with_raw_response.fetch_by_external_id(
                "",
            )

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.unarchive(
            "billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.unarchive(
            "billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.unarchive(
            "billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billing_entity_id` but received ''"):
            await async_client.account.billing_entities.with_raw_response.unarchive(
                "",
            )

    @parametrize
    async def test_method_unarchive_by_external_id(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.unarchive_by_external_id(
            "external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_unarchive_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.unarchive_by_external_id(
            "external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_unarchive_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.unarchive_by_external_id(
            "external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            await async_client.account.billing_entities.with_raw_response.unarchive_by_external_id(
                "",
            )

    @parametrize
    async def test_method_update_by_external_id(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        billing_entity = await async_client.account.billing_entities.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
            address={
                "country": "x",
                "city": "city",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            default_payment_gateway_connection_id="default_payment_gateway_connection_id",
            invoice_settings={"memo": "memo"},
            legal_name="x",
            name="x",
            payment_gateway_connections=[
                {
                    "payment_gateway_connection_id": "payment_gateway_connection_id",
                    "payment_provider_type": "stripe",
                }
            ],
            tax_registrations=[
                {
                    "code": "x",
                    "value": "x",
                    "applies_to": "applies_to",
                }
            ],
        )
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.account.billing_entities.with_raw_response.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_entity = response.parse()
        assert_matches_type(BillingEntity, billing_entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.account.billing_entities.with_streaming_response.update_by_external_id(
            external_billing_entity_id="external_billing_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_entity = await response.parse()
            assert_matches_type(BillingEntity, billing_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_billing_entity_id` but received ''"
        ):
            await async_client.account.billing_entities.with_raw_response.update_by_external_id(
                external_billing_entity_id="",
            )
