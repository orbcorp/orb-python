# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.plans import (
    MigrationListResponse,
    MigrationCancelResponse,
    MigrationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMigrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        migration = client.plans.migrations.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.plans.migrations.with_raw_response.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.plans.migrations.with_streaming_response.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.migrations.with_raw_response.retrieve(
                migration_id="migration_id",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            client.plans.migrations.with_raw_response.retrieve(
                migration_id="",
                plan_id="plan_id",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        migration = client.plans.migrations.list(
            plan_id="plan_id",
        )
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        migration = client.plans.migrations.list(
            plan_id="plan_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.plans.migrations.with_raw_response.list(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.plans.migrations.with_streaming_response.list(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(SyncPage[MigrationListResponse], migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.migrations.with_raw_response.list(
                plan_id="",
            )

    @parametrize
    def test_method_cancel(self, client: Orb) -> None:
        migration = client.plans.migrations.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        )
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Orb) -> None:
        response = client.plans.migrations.with_raw_response.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Orb) -> None:
        with client.plans.migrations.with_streaming_response.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationCancelResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.migrations.with_raw_response.cancel(
                migration_id="migration_id",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            client.plans.migrations.with_raw_response.cancel(
                migration_id="",
                plan_id="plan_id",
            )


class TestAsyncMigrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        migration = await async_client.plans.migrations.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.migrations.with_raw_response.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.migrations.with_streaming_response.retrieve(
            migration_id="migration_id",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.migrations.with_raw_response.retrieve(
                migration_id="migration_id",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            await async_client.plans.migrations.with_raw_response.retrieve(
                migration_id="",
                plan_id="plan_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        migration = await async_client.plans.migrations.list(
            plan_id="plan_id",
        )
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        migration = await async_client.plans.migrations.list(
            plan_id="plan_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.migrations.with_raw_response.list(
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.migrations.with_streaming_response.list(
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(AsyncPage[MigrationListResponse], migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.migrations.with_raw_response.list(
                plan_id="",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOrb) -> None:
        migration = await async_client.plans.migrations.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        )
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.migrations.with_raw_response.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCancelResponse, migration, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.migrations.with_streaming_response.cancel(
            migration_id="migration_id",
            plan_id="plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationCancelResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.migrations.with_raw_response.cancel(
                migration_id="migration_id",
                plan_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `migration_id` but received ''"):
            await async_client.plans.migrations.with_raw_response.cancel(
                migration_id="",
                plan_id="plan_id",
            )
