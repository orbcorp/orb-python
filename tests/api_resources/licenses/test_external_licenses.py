# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_date
from tests.utils import assert_matches_type
from orb.types.licenses import ExternalLicenseGetUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalLicenses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_usage(self, client: Orb) -> None:
        external_license = client.licenses.external_licenses.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    def test_method_get_usage_with_all_params(self, client: Orb) -> None:
        external_license = client.licenses.external_licenses.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    def test_raw_response_get_usage(self, client: Orb) -> None:
        response = client.licenses.external_licenses.with_raw_response.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_license = response.parse()
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    def test_streaming_response_get_usage(self, client: Orb) -> None:
        with client.licenses.external_licenses.with_streaming_response.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_license = response.parse()
            assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_usage(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_license_id` but received ''"):
            client.licenses.external_licenses.with_raw_response.get_usage(
                external_license_id="",
                license_type_id="license_type_id",
                subscription_id="subscription_id",
            )


class TestAsyncExternalLicenses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_usage(self, async_client: AsyncOrb) -> None:
        external_license = await async_client.licenses.external_licenses.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    async def test_method_get_usage_with_all_params(self, async_client: AsyncOrb) -> None:
        external_license = await async_client.licenses.external_licenses.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.external_licenses.with_raw_response.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_license = response.parse()
        assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.external_licenses.with_streaming_response.get_usage(
            external_license_id="external_license_id",
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_license = await response.parse()
            assert_matches_type(ExternalLicenseGetUsageResponse, external_license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_usage(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_license_id` but received ''"):
            await async_client.licenses.external_licenses.with_raw_response.get_usage(
                external_license_id="",
                license_type_id="license_type_id",
                subscription_id="subscription_id",
            )
