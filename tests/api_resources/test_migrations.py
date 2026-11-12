# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    MigrationListResponse,
    MigrationCancelResponse,
    MigrationCreateResponse,
    MigrationRetrieveResponse,
)
from orb._utils import parse_date
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMigrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        migration = client.migrations.create(
            effective_time="immediately",
            target_plan_version_number=0,
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        migration = client.migrations.create(
            effective_time="immediately",
            target_plan_version_number=0,
            allow_invoice_credit_or_void=True,
            can_defer_billing=True,
            effective_date=parse_date("2019-12-27"),
            excluded_subscription_ids=["string"],
            external_plan_id="external_plan_id",
            in_trial=True,
            included_subscription_ids=["string"],
            plan_id="plan_id",
            plan_version_numbers=[0],
            reason="reason",
            statuses=["active"],
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.migrations.with_raw_response.create(
            effective_time="immediately",
            target_plan_version_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.migrations.with_streaming_response.create(
            effective_time="immediately",
            target_plan_version_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationCreateResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        migration = client.migrations.retrieve(
            "migration_id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.migrations.with_raw_response.retrieve(
            "migration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.migrations.with_streaming_response.retrieve(
            "migration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            client.migrations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        migration = client.migrations.list()
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        migration = client.migrations.list(
            cursor="cursor",
            external_plan_id="external_plan_id",
            limit=1,
            plan_id="plan_id",
        )
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.migrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.migrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Orb) -> None:
        migration = client.migrations.cancel(
            "migration_id",
        )
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Orb) -> None:
        response = client.migrations.with_raw_response.cancel(
            "migration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Orb) -> None:
        with client.migrations.with_streaming_response.cancel(
            "migration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationCancelResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            client.migrations.with_raw_response.cancel(
                "",
            )


class TestAsyncMigrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.create(
            effective_time="immediately",
            target_plan_version_number=0,
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.create(
            effective_time="immediately",
            target_plan_version_number=0,
            allow_invoice_credit_or_void=True,
            can_defer_billing=True,
            effective_date=parse_date("2019-12-27"),
            excluded_subscription_ids=["string"],
            external_plan_id="external_plan_id",
            in_trial=True,
            included_subscription_ids=["string"],
            plan_id="plan_id",
            plan_version_numbers=[0],
            reason="reason",
            statuses=["active"],
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.migrations.with_raw_response.create(
            effective_time="immediately",
            target_plan_version_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.migrations.with_streaming_response.create(
            effective_time="immediately",
            target_plan_version_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationCreateResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.retrieve(
            "migration_id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.migrations.with_raw_response.retrieve(
            "migration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.migrations.with_streaming_response.retrieve(
            "migration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            await async_client.migrations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.list()
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.list(
            cursor="cursor",
            external_plan_id="external_plan_id",
            limit=1,
            plan_id="plan_id",
        )
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.migrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.migrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOrb) -> None:
        migration = await async_client.migrations.cancel(
            "migration_id",
        )
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOrb) -> None:
        response = await async_client.migrations.with_raw_response.cancel(
            "migration_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOrb) -> None:
        async with async_client.migrations.with_streaming_response.cancel(
            "migration_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationCancelResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            await async_client.migrations.with_raw_response.cancel(
                "",
            )
