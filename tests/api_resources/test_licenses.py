# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    LicenseListResponse,
    LicenseCreateResponse,
    LicenseRetrieveResponse,
    LicenseDeactivateResponse,
    LicenseRetrieveByExternalIDResponse,
)
from orb._utils import parse_date
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLicenses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        license = client.licenses.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        license = client.licenses.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            end_date=parse_date("2026-01-27"),
            start_date=parse_date("2026-01-27"),
        )
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.licenses.with_raw_response.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.licenses.with_streaming_response.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseCreateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        license = client.licenses.retrieve(
            "license_id",
        )
        assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.licenses.with_raw_response.retrieve(
            "license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.licenses.with_streaming_response.retrieve(
            "license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            client.licenses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        license = client.licenses.list(
            subscription_id="subscription_id",
        )
        assert_matches_type(SyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        license = client.licenses.list(
            subscription_id="subscription_id",
            cursor="cursor",
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            limit=1,
            status="active",
        )
        assert_matches_type(SyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.licenses.with_raw_response.list(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(SyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.licenses.with_streaming_response.list(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(SyncPage[LicenseListResponse], license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deactivate(self, client: Orb) -> None:
        license = client.licenses.deactivate(
            license_id="license_id",
        )
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    def test_method_deactivate_with_all_params(self, client: Orb) -> None:
        license = client.licenses.deactivate(
            license_id="license_id",
            end_date=parse_date("2026-01-27"),
        )
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    def test_raw_response_deactivate(self, client: Orb) -> None:
        response = client.licenses.with_raw_response.deactivate(
            license_id="license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    def test_streaming_response_deactivate(self, client: Orb) -> None:
        with client.licenses.with_streaming_response.deactivate(
            license_id="license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            client.licenses.with_raw_response.deactivate(
                license_id="",
            )

    @parametrize
    def test_method_retrieve_by_external_id(self, client: Orb) -> None:
        license = client.licenses.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_external_id(self, client: Orb) -> None:
        response = client.licenses.with_raw_response.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_by_external_id(self, client: Orb) -> None:
        with client.licenses.with_streaming_response.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_license_id` but received ''"):
            client.licenses.with_raw_response.retrieve_by_external_id(
                external_license_id="",
                license_type_id="license_type_id",
                subscription_id="subscription_id",
            )


class TestAsyncLicenses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            end_date=parse_date("2026-01-27"),
            start_date=parse_date("2026-01-27"),
        )
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.with_raw_response.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseCreateResponse, license, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.with_streaming_response.create(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseCreateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.retrieve(
            "license_id",
        )
        assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.with_raw_response.retrieve(
            "license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.with_streaming_response.retrieve(
            "license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseRetrieveResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            await async_client.licenses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.list(
            subscription_id="subscription_id",
        )
        assert_matches_type(AsyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.list(
            subscription_id="subscription_id",
            cursor="cursor",
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            limit=1,
            status="active",
        )
        assert_matches_type(AsyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.with_raw_response.list(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(AsyncPage[LicenseListResponse], license, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.with_streaming_response.list(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(AsyncPage[LicenseListResponse], license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.deactivate(
            license_id="license_id",
        )
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    async def test_method_deactivate_with_all_params(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.deactivate(
            license_id="license_id",
            end_date=parse_date("2026-01-27"),
        )
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.with_raw_response.deactivate(
            license_id="license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.with_streaming_response.deactivate(
            license_id="license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseDeactivateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            await async_client.licenses.with_raw_response.deactivate(
                license_id="",
            )

    @parametrize
    async def test_method_retrieve_by_external_id(self, async_client: AsyncOrb) -> None:
        license = await async_client.licenses.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.with_raw_response.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.with_streaming_response.retrieve_by_external_id(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseRetrieveByExternalIDResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_license_id` but received ''"):
            await async_client.licenses.with_raw_response.retrieve_by_external_id(
                external_license_id="",
                license_type_id="license_type_id",
                subscription_id="subscription_id",
            )
