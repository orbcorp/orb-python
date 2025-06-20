# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers.credits import (
    TopUpListResponse,
    TopUpCreateResponse,
    TopUpListByExternalIDResponse,
    TopUpCreateByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopUps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "memo",
                "require_successful_payment": True,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
            active_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_after=0,
            expires_after_unit="day",
        )
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.create(
                customer_id="",
                amount="amount",
                currency="currency",
                invoice_settings={
                    "auto_collection": True,
                    "net_terms": 0,
                },
                per_unit_cost_basis="per_unit_cost_basis",
                threshold="threshold",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.list(
            customer_id="customer_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(SyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert_matches_type(SyncPage[TopUpListResponse], top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_delete(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        )
        assert top_up is None

    @parametrize
    def test_raw_response_delete(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert top_up is None

    @parametrize
    def test_streaming_response_delete(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert top_up is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.delete(
                top_up_id="top_up_id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `top_up_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.delete(
                top_up_id="",
                customer_id="customer_id",
            )

    @parametrize
    def test_method_create_by_external_id(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    def test_method_create_by_external_id_with_all_params(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "memo",
                "require_successful_payment": True,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
            active_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_after=0,
            expires_after_unit="day",
        )
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    def test_raw_response_create_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    def test_streaming_response_create_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.create_by_external_id(
                external_customer_id="",
                amount="amount",
                currency="currency",
                invoice_settings={
                    "auto_collection": True,
                    "net_terms": 0,
                },
                per_unit_cost_basis="per_unit_cost_basis",
                threshold="threshold",
            )

    @parametrize
    def test_method_delete_by_external_id(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        )
        assert top_up is None

    @parametrize
    def test_raw_response_delete_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert top_up is None

    @parametrize
    def test_streaming_response_delete_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert top_up is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
                top_up_id="top_up_id",
                external_customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `top_up_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
                top_up_id="",
                external_customer_id="external_customer_id",
            )

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(SyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        top_up = client.customers.credits.top_ups.list_by_external_id(
            external_customer_id="external_customer_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.credits.top_ups.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(SyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.credits.top_ups.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = response.parse()
            assert_matches_type(SyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.credits.top_ups.with_raw_response.list_by_external_id(
                external_customer_id="",
            )


class TestAsyncTopUps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "memo",
                "require_successful_payment": True,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
            active_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_after=0,
            expires_after_unit="day",
        )
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.create(
            customer_id="customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert_matches_type(TopUpCreateResponse, top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.create(
                customer_id="",
                amount="amount",
                currency="currency",
                invoice_settings={
                    "auto_collection": True,
                    "net_terms": 0,
                },
                per_unit_cost_basis="per_unit_cost_basis",
                threshold="threshold",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.list(
            customer_id="customer_id",
        )
        assert_matches_type(AsyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.list(
            customer_id="customer_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(AsyncPage[TopUpListResponse], top_up, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert_matches_type(AsyncPage[TopUpListResponse], top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        )
        assert top_up is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert top_up is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.delete(
            top_up_id="top_up_id",
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert top_up is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.delete(
                top_up_id="top_up_id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `top_up_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.delete(
                top_up_id="",
                customer_id="customer_id",
            )

    @parametrize
    async def test_method_create_by_external_id(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    async def test_method_create_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
                "memo": "memo",
                "require_successful_payment": True,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
            active_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_after=0,
            expires_after_unit="day",
        )
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    async def test_raw_response_create_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

    @parametrize
    async def test_streaming_response_create_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.create_by_external_id(
            external_customer_id="external_customer_id",
            amount="amount",
            currency="currency",
            invoice_settings={
                "auto_collection": True,
                "net_terms": 0,
            },
            per_unit_cost_basis="per_unit_cost_basis",
            threshold="threshold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert_matches_type(TopUpCreateByExternalIDResponse, top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.create_by_external_id(
                external_customer_id="",
                amount="amount",
                currency="currency",
                invoice_settings={
                    "auto_collection": True,
                    "net_terms": 0,
                },
                per_unit_cost_basis="per_unit_cost_basis",
                threshold="threshold",
            )

    @parametrize
    async def test_method_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        )
        assert top_up is None

    @parametrize
    async def test_raw_response_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert top_up is None

    @parametrize
    async def test_streaming_response_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.delete_by_external_id(
            top_up_id="top_up_id",
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert top_up is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
                top_up_id="top_up_id",
                external_customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `top_up_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.delete_by_external_id(
                top_up_id="",
                external_customer_id="external_customer_id",
            )

    @parametrize
    async def test_method_list_by_external_id(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(AsyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        top_up = await async_client.customers.credits.top_ups.list_by_external_id(
            external_customer_id="external_customer_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.credits.top_ups.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_up = response.parse()
        assert_matches_type(AsyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.credits.top_ups.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_up = await response.parse()
            assert_matches_type(AsyncPage[TopUpListByExternalIDResponse], top_up, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.credits.top_ups.with_raw_response.list_by_external_id(
                external_customer_id="",
            )
