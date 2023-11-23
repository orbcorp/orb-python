# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .costs import Costs, AsyncCosts, CostsWithRawResponse, AsyncCostsWithRawResponse
from .usage import Usage, AsyncUsage, UsageWithRawResponse, AsyncUsageWithRawResponse
from ...types import (
    Customer,
    customer_list_params,
    customer_create_params,
    customer_update_params,
    customer_update_by_external_id_params,
)
from .credits import (
    Credits,
    AsyncCredits,
    CreditsWithRawResponse,
    AsyncCreditsWithRawResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .balance_transactions import (
    BalanceTransactions,
    AsyncBalanceTransactions,
    BalanceTransactionsWithRawResponse,
    AsyncBalanceTransactionsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Customers", "AsyncCustomers"]


class Customers(SyncAPIResource):
    costs: Costs
    usage: Usage
    credits: Credits
    balance_transactions: BalanceTransactions
    with_raw_response: CustomersWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.costs = Costs(client)
        self.usage = Usage(client)
        self.credits = Credits(client)
        self.balance_transactions = BalanceTransactions(client)
        self.with_raw_response = CustomersWithRawResponse(self)

    def create(
        self,
        *,
        email: str,
        name: str,
        accounting_sync_configuration: Optional[customer_create_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_create_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_create_params.ReportingConfiguration] | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_create_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_create_params.TaxID] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This operation is used to create an Orb customer, who is party to the core
        billing relationship. See [Customer](../guides/concepts#customer) for an
        overview of the customer resource.

        This endpoint is critical in the following Orb functionality:

        - Automated charges can be configured by setting `payment_provider` and
          `payment_provider_id` to automatically issue invoices
        - [Customer ID Aliases](../guides/events-and-metrics/customer-aliases) can be
          configured by setting `external_customer_id`
        - [Timezone localization](../guides/product-catalog/timezones.md) can be
          configured on a per-customer basis by setting the `timezone` parameter

        Args:
          email: A valid customer email, to be used for notifications. When Orb triggers payment
              through a payment gateway, this email will be used for any automatically issued
              receipts.

          name: The full name of the customer

          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          external_customer_id: An optional user-defined ID for this customer resource, used throughout the
              system as an alias for this Customer. Use this field to identify a customer by
              an existing identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode, the connection must first be configured in the Orb
              webapp.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          timezone: A timezone identifier from the IANA timezone database, such as
              `"America/Los_Angeles"`. This defaults to your account's timezone if not set.
              This cannot be changed after customer creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/customers",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "metadata": metadata,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                    "timezone": timezone,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )

    def update(
        self,
        customer_id: str,
        *,
        accounting_sync_configuration: Optional[customer_update_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_update_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_update_params.ReportingConfiguration] | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_update_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_update_params.TaxID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint can be used to update the `payment_provider`,
        `payment_provider_id`, `name`, `email`, `email_delivery`, `tax_id`,
        `auto_collection`, `metadata`, `shipping_address`, `billing_address`, and
        `additional_emails` of an existing customer. Other fields on a customer are
        currently immutable.

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The full name of the customer

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode:

              - the connection must first be configured in the Orb webapp.
              - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`,
                `bill.com`, `netsuite`), any product mappings must first be configured with
                the Orb team.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._put(
            f"/customers/{customer_id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Customer]:
        """This endpoint returns a list of all customers for an account.

        The list of
        customers is ordered starting from the most recently created customer. This
        endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        See [Customer](../guides/concepts#customer) for an overview of the customer
        model.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=SyncPage[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )

    def delete(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This performs a deletion of this customer, its subscriptions, and its invoices.
        This operation is irreversible. Note that this is a _soft_ deletion, but the
        data will be inaccessible through the API and Orb dashboard. For hard-deletion,
        please reach out to the Orb team directly.

        **Note**: This operation happens asynchronously and can be expected to take a
        few minutes to propagate to related resources. However, querying for the
        customer on subsequent GET requests while deletion is in process will reflect
        its deletion with a `deleted: true` property. Once the customer deletion has
        been fully processed, the customer will not be returned in the API.

        On successful processing, this returns an empty dictionary (`{}`) in the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def fetch(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """This endpoint is used to fetch customer details given an identifier.

        If the
        `Customer` is in the process of being deleted, only the properties `id` and
        `deleted: true` will be returned.

        See the [Customer resource](../guides/core-concepts.mdx#customer) for a full
        discussion of the Customer model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def fetch_by_external_id(
        self,
        external_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        This endpoint is used to fetch customer details given an `external_customer_id`
        (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)).

        Note that the resource and semantics of this endpoint exactly mirror
        [Get Customer](fetch-customer).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/customers/external_customer_id/{external_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def update_by_external_id(
        self,
        id: str,
        *,
        accounting_sync_configuration: Optional[customer_update_by_external_id_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_update_by_external_id_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_update_by_external_id_params.ReportingConfiguration]
        | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_update_by_external_id_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_update_by_external_id_params.TaxID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint is used to update customer details given an `external_customer_id`
        (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)). Note
        that the resource and semantics of this endpoint exactly mirror
        [Update Customer](update-customer).

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The full name of the customer

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode:

              - the connection must first be configured in the Orb webapp.
              - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`,
                `bill.com`, `netsuite`), any product mappings must first be configured with
                the Orb team.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._put(
            f"/customers/external_customer_id/{id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                },
                customer_update_by_external_id_params.CustomerUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )


class AsyncCustomers(AsyncAPIResource):
    costs: AsyncCosts
    usage: AsyncUsage
    credits: AsyncCredits
    balance_transactions: AsyncBalanceTransactions
    with_raw_response: AsyncCustomersWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.costs = AsyncCosts(client)
        self.usage = AsyncUsage(client)
        self.credits = AsyncCredits(client)
        self.balance_transactions = AsyncBalanceTransactions(client)
        self.with_raw_response = AsyncCustomersWithRawResponse(self)

    async def create(
        self,
        *,
        email: str,
        name: str,
        accounting_sync_configuration: Optional[customer_create_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_create_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_create_params.ReportingConfiguration] | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_create_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_create_params.TaxID] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This operation is used to create an Orb customer, who is party to the core
        billing relationship. See [Customer](../guides/concepts#customer) for an
        overview of the customer resource.

        This endpoint is critical in the following Orb functionality:

        - Automated charges can be configured by setting `payment_provider` and
          `payment_provider_id` to automatically issue invoices
        - [Customer ID Aliases](../guides/events-and-metrics/customer-aliases) can be
          configured by setting `external_customer_id`
        - [Timezone localization](../guides/product-catalog/timezones.md) can be
          configured on a per-customer basis by setting the `timezone` parameter

        Args:
          email: A valid customer email, to be used for notifications. When Orb triggers payment
              through a payment gateway, this email will be used for any automatically issued
              receipts.

          name: The full name of the customer

          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          external_customer_id: An optional user-defined ID for this customer resource, used throughout the
              system as an alias for this Customer. Use this field to identify a customer by
              an existing identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode, the connection must first be configured in the Orb
              webapp.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          timezone: A timezone identifier from the IANA timezone database, such as
              `"America/Los_Angeles"`. This defaults to your account's timezone if not set.
              This cannot be changed after customer creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/customers",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "metadata": metadata,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                    "timezone": timezone,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )

    async def update(
        self,
        customer_id: str,
        *,
        accounting_sync_configuration: Optional[customer_update_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_update_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_update_params.ReportingConfiguration] | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_update_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_update_params.TaxID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint can be used to update the `payment_provider`,
        `payment_provider_id`, `name`, `email`, `email_delivery`, `tax_id`,
        `auto_collection`, `metadata`, `shipping_address`, `billing_address`, and
        `additional_emails` of an existing customer. Other fields on a customer are
        currently immutable.

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The full name of the customer

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode:

              - the connection must first be configured in the Orb webapp.
              - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`,
                `bill.com`, `netsuite`), any product mappings must first be configured with
                the Orb team.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._put(
            f"/customers/{customer_id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Customer, AsyncPage[Customer]]:
        """This endpoint returns a list of all customers for an account.

        The list of
        customers is ordered starting from the most recently created customer. This
        endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        See [Customer](../guides/concepts#customer) for an overview of the customer
        model.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=AsyncPage[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )

    async def delete(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This performs a deletion of this customer, its subscriptions, and its invoices.
        This operation is irreversible. Note that this is a _soft_ deletion, but the
        data will be inaccessible through the API and Orb dashboard. For hard-deletion,
        please reach out to the Orb team directly.

        **Note**: This operation happens asynchronously and can be expected to take a
        few minutes to propagate to related resources. However, querying for the
        customer on subsequent GET requests while deletion is in process will reflect
        its deletion with a `deleted: true` property. Once the customer deletion has
        been fully processed, the customer will not be returned in the API.

        On successful processing, this returns an empty dictionary (`{}`) in the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def fetch(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """This endpoint is used to fetch customer details given an identifier.

        If the
        `Customer` is in the process of being deleted, only the properties `id` and
        `deleted: true` will be returned.

        See the [Customer resource](../guides/core-concepts.mdx#customer) for a full
        discussion of the Customer model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def fetch_by_external_id(
        self,
        external_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Customer:
        """
        This endpoint is used to fetch customer details given an `external_customer_id`
        (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)).

        Note that the resource and semantics of this endpoint exactly mirror
        [Get Customer](fetch-customer).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/customers/external_customer_id/{external_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def update_by_external_id(
        self,
        id: str,
        *,
        accounting_sync_configuration: Optional[customer_update_by_external_id_params.AccountingSyncConfiguration]
        | NotGiven = NOT_GIVEN,
        additional_emails: Optional[List[str]] | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_address: Optional[customer_update_by_external_id_params.BillingAddress] | NotGiven = NOT_GIVEN,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        email_delivery: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | NotGiven = NOT_GIVEN,
        payment_provider_id: Optional[str] | NotGiven = NOT_GIVEN,
        reporting_configuration: Optional[customer_update_by_external_id_params.ReportingConfiguration]
        | NotGiven = NOT_GIVEN,
        shipping_address: Optional[customer_update_by_external_id_params.ShippingAddress] | NotGiven = NOT_GIVEN,
        tax_id: Optional[customer_update_by_external_id_params.TaxID] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint is used to update customer details given an `external_customer_id`
        (see [Customer ID Aliases](../guides/events-and-metrics/customer-aliases)). Note
        that the resource and semantics of this endpoint exactly mirror
        [Update Customer](update-customer).

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The full name of the customer

          payment_provider: This is used for creating charges or invoices in an external system via Orb.
              When not in test mode:

              - the connection must first be configured in the Orb webapp.
              - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`,
                `bill.com`, `netsuite`), any product mappings must first be configured with
                the Orb team.

          payment_provider_id: The ID of this customer in an external payments solution, such as Stripe. This
              is used for creating charges or invoices in the external system via Orb.

          tax_id: Tax IDs are commonly required to be displayed on customer invoices, which are
              added to the headers of invoices.

              ### Supported Tax ID Countries and Types

              | Country              | Type         | Description                                                                                             |
              | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria              | `eu_vat`     | European VAT number                                                                                     |
              | Belgium              | `eu_vat`     | European VAT number                                                                                     |
              | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
              | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
              | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
              | Canada               | `ca_bn`      | Canadian BN                                                                                             |
              | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
              | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
              | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
              | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
              | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
              | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
              | Croatia              | `eu_vat`     | European VAT number                                                                                     |
              | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
              | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
              | Denmark              | `eu_vat`     | European VAT number                                                                                     |
              | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | Estonia              | `eu_vat`     | European VAT number                                                                                     |
              | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
              | Finland              | `eu_vat`     | European VAT number                                                                                     |
              | France               | `eu_vat`     | European VAT number                                                                                     |
              | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany              | `eu_vat`     | European VAT number                                                                                     |
              | Greece               | `eu_vat`     | European VAT number                                                                                     |
              | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
              | Hungary              | `eu_vat`     | European VAT number                                                                                     |
              | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
              | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
              | India                | `in_gst`     | Indian GST number                                                                                       |
              | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
              | Ireland              | `eu_vat`     | European VAT number                                                                                     |
              | Israel               | `il_vat`     | Israel VAT                                                                                              |
              | Italy                | `eu_vat`     | European VAT number                                                                                     |
              | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Latvia               | `eu_vat`     | European VAT number                                                                                     |
              | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
              | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
              | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
              | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
              | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
              | Malta                | `eu_vat `    | European VAT number                                                                                     |
              | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
              | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
              | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
              | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
              | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
              | Poland               | `eu_vat`     | European VAT number                                                                                     |
              | Portugal             | `eu_vat`     | European VAT number                                                                                     |
              | Romania              | `eu_vat`     | European VAT number                                                                                     |
              | Russia               | `ru_inn`     | Russian INN                                                                                             |
              | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
              | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
              | South Africa         | `za_vat`     | South African VAT number                                                                                |
              | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
              | Spain                | `eu_vat`     | European VAT number                                                                                     |
              | Sweden               | `eu_vat`     | European VAT number                                                                                     |
              | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
              | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Thailand             | `th_vat`     | Thai VAT                                                                                                |
              | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
              | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
              | United States        | `us_ein`     | United States EIN                                                                                       |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._put(
            f"/customers/external_customer_id/{id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_id": tax_id,
                },
                customer_update_by_external_id_params.CustomerUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Customer,
        )


class CustomersWithRawResponse:
    def __init__(self, customers: Customers) -> None:
        self.costs = CostsWithRawResponse(customers.costs)
        self.usage = UsageWithRawResponse(customers.usage)
        self.credits = CreditsWithRawResponse(customers.credits)
        self.balance_transactions = BalanceTransactionsWithRawResponse(customers.balance_transactions)

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.delete = to_raw_response_wrapper(
            customers.delete,
        )
        self.fetch = to_raw_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = to_raw_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.update_by_external_id = to_raw_response_wrapper(
            customers.update_by_external_id,
        )


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self.costs = AsyncCostsWithRawResponse(customers.costs)
        self.usage = AsyncUsageWithRawResponse(customers.usage)
        self.credits = AsyncCreditsWithRawResponse(customers.credits)
        self.balance_transactions = AsyncBalanceTransactionsWithRawResponse(customers.balance_transactions)

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customers.delete,
        )
        self.fetch = async_to_raw_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = async_to_raw_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.update_by_external_id = async_to_raw_response_wrapper(
            customers.update_by_external_id,
        )
