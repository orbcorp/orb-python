# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from .costs import (
    Costs,
    AsyncCosts,
    CostsWithRawResponse,
    AsyncCostsWithRawResponse,
    CostsWithStreamingResponse,
    AsyncCostsWithStreamingResponse,
)
from ...types import (
    customer_list_params,
    customer_create_params,
    customer_update_params,
    customer_update_by_external_id_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .credits.credits import (
    Credits,
    AsyncCredits,
    CreditsWithRawResponse,
    AsyncCreditsWithRawResponse,
    CreditsWithStreamingResponse,
    AsyncCreditsWithStreamingResponse,
)
from ...types.customer import Customer
from .balance_transactions import (
    BalanceTransactions,
    AsyncBalanceTransactions,
    BalanceTransactionsWithRawResponse,
    AsyncBalanceTransactionsWithRawResponse,
    BalanceTransactionsWithStreamingResponse,
    AsyncBalanceTransactionsWithStreamingResponse,
)
from ...types.address_input_param import AddressInputParam
from ...types.shared_params.customer_tax_id import CustomerTaxID
from ...types.customer_hierarchy_config_param import CustomerHierarchyConfigParam
from ...types.new_reporting_configuration_param import NewReportingConfigurationParam
from ...types.new_accounting_sync_configuration_param import NewAccountingSyncConfigurationParam

__all__ = ["Customers", "AsyncCustomers"]


class Customers(SyncAPIResource):
    @cached_property
    def costs(self) -> Costs:
        return Costs(self._client)

    @cached_property
    def credits(self) -> Credits:
        return Credits(self._client)

    @cached_property
    def balance_transactions(self) -> BalanceTransactions:
        return BalanceTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return CustomersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return CustomersWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        name: str,
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_create_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This operation is used to create an Orb customer, who is party to the core
        billing relationship. See [Customer](/core-concepts##customer) for an overview
        of the customer resource.

        This endpoint is critical in the following Orb functionality:

        - Automated charges can be configured by setting `payment_provider` and
          `payment_provider_id` to automatically issue invoices
        - [Customer ID Aliases](/events-and-metrics/customer-aliases) can be configured
          by setting `external_customer_id`
        - [Timezone localization](/essentials/timezones) can be configured on a
          per-customer basis by setting the `timezone` parameter

        Args:
          email: A valid customer email, to be used for notifications. When Orb triggers payment
              through a payment gateway, this email will be used for any automatically issued
              receipts.

          name: The full name of the customer

          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval. If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          external_customer_id: An optional user-defined ID for this customer resource, used throughout the
              system as an alias for this Customer. Use this field to identify a customer by
              an existing identifier in your system.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

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
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_update_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval.If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          external_customer_id: The external customer ID. This can only be set if the customer has no existing
              external customer ID. Since this action may change usage quantities for all
              existing subscriptions, it is disallowed if the customer has issued invoices
              with usage line items and subject to the same restrictions as backdated
              subscription creation.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._put(
            f"/customers/{customer_id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Customer]:
        """This endpoint returns a list of all customers for an account.

        The list of
        customers is ordered starting from the most recently created customer. This
        endpoint follows Orb's
        [standardized pagination format](/api-reference/pagination).

        See [Customer](/core-concepts##customer) for an overview of the customer model.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This performs a deletion of this customer, its subscriptions, and its invoices,
        provided the customer does not have any issued invoices. Customers with issued
        invoices cannot be deleted. This operation is irreversible. Note that this is a
        _soft_ deletion, but the data will be inaccessible through the API and Orb
        dashboard.

        For a hard-deletion, please reach out to the Orb team directly.

        **Note**: This operation happens asynchronously and can be expected to take a
        few minutes to propagate to related resources. However, querying for the
        customer on subsequent GET requests while deletion is in process will reflect
        its deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """This endpoint is used to fetch customer details given an identifier.

        If the
        `Customer` is in the process of being deleted, only the properties `id` and
        `deleted: true` will be returned.

        See the [Customer resource](/core-concepts#customer) for a full discussion of
        the Customer model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        This endpoint is used to fetch customer details given an `external_customer_id`
        (see [Customer ID Aliases](/events-and-metrics/customer-aliases)).

        Note that the resource and semantics of this endpoint exactly mirror
        [Get Customer](fetch-customer).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get(
            f"/customers/external_customer_id/{external_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def sync_payment_methods_from_gateway(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Sync Orb's payment methods for the customer with their gateway.

        This method can be called before taking an action that may cause the customer to
        be charged, ensuring that the most up-to-date payment method is charged.

        **Note**: This functionality is currently only available for Stripe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/customers/{customer_id}/sync_payment_methods_from_gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def sync_payment_methods_from_gateway_by_external_customer_id(
        self,
        external_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Sync Orb's payment methods for the customer with their gateway.

        This method can be called before taking an action that may cause the customer to
        be charged, ensuring that the most up-to-date payment method is charged.

        **Note**: This functionality is currently only available for Stripe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/customers/external_customer_id/{external_customer_id}/sync_payment_methods_from_gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def update_by_external_id(
        self,
        id: str,
        *,
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_update_by_external_id_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint is used to update customer details given an `external_customer_id`
        (see [Customer ID Aliases](/events-and-metrics/customer-aliases)). Note that the
        resource and semantics of this endpoint exactly mirror
        [Update Customer](update-customer).

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval.If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          external_customer_id: The external customer ID. This can only be set if the customer has no existing
              external customer ID. Since this action may change usage quantities for all
              existing subscriptions, it is disallowed if the customer has issued invoices
              with usage line items and subject to the same restrictions as backdated
              subscription creation.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/customers/external_customer_id/{id}",
            body=maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
    @cached_property
    def costs(self) -> AsyncCosts:
        return AsyncCosts(self._client)

    @cached_property
    def credits(self) -> AsyncCredits:
        return AsyncCredits(self._client)

    @cached_property
    def balance_transactions(self) -> AsyncBalanceTransactions:
        return AsyncBalanceTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncCustomersWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        name: str,
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_create_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This operation is used to create an Orb customer, who is party to the core
        billing relationship. See [Customer](/core-concepts##customer) for an overview
        of the customer resource.

        This endpoint is critical in the following Orb functionality:

        - Automated charges can be configured by setting `payment_provider` and
          `payment_provider_id` to automatically issue invoices
        - [Customer ID Aliases](/events-and-metrics/customer-aliases) can be configured
          by setting `external_customer_id`
        - [Timezone localization](/essentials/timezones) can be configured on a
          per-customer basis by setting the `timezone` parameter

        Args:
          email: A valid customer email, to be used for notifications. When Orb triggers payment
              through a payment gateway, this email will be used for any automatically issued
              receipts.

          name: The full name of the customer

          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval. If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          external_customer_id: An optional user-defined ID for this customer resource, used throughout the
              system as an alias for this Customer. Use this field to identify a customer by
              an existing identifier in your system.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

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
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_update_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval.If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          external_customer_id: The external customer ID. This can only be set if the customer has no existing
              external customer ID. Since this action may change usage quantities for all
              existing subscriptions, it is disallowed if the customer has issued invoices
              with usage line items and subject to the same restrictions as backdated
              subscription creation.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._put(
            f"/customers/{customer_id}",
            body=await async_maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Customer, AsyncPage[Customer]]:
        """This endpoint returns a list of all customers for an account.

        The list of
        customers is ordered starting from the most recently created customer. This
        endpoint follows Orb's
        [standardized pagination format](/api-reference/pagination).

        See [Customer](/core-concepts##customer) for an overview of the customer model.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This performs a deletion of this customer, its subscriptions, and its invoices,
        provided the customer does not have any issued invoices. Customers with issued
        invoices cannot be deleted. This operation is irreversible. Note that this is a
        _soft_ deletion, but the data will be inaccessible through the API and Orb
        dashboard.

        For a hard-deletion, please reach out to the Orb team directly.

        **Note**: This operation happens asynchronously and can be expected to take a
        few minutes to propagate to related resources. However, querying for the
        customer on subsequent GET requests while deletion is in process will reflect
        its deletion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """This endpoint is used to fetch customer details given an identifier.

        If the
        `Customer` is in the process of being deleted, only the properties `id` and
        `deleted: true` will be returned.

        See the [Customer resource](/core-concepts#customer) for a full discussion of
        the Customer model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        This endpoint is used to fetch customer details given an `external_customer_id`
        (see [Customer ID Aliases](/events-and-metrics/customer-aliases)).

        Note that the resource and semantics of this endpoint exactly mirror
        [Get Customer](fetch-customer).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return await self._get(
            f"/customers/external_customer_id/{external_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def sync_payment_methods_from_gateway(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Sync Orb's payment methods for the customer with their gateway.

        This method can be called before taking an action that may cause the customer to
        be charged, ensuring that the most up-to-date payment method is charged.

        **Note**: This functionality is currently only available for Stripe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/customers/{customer_id}/sync_payment_methods_from_gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def sync_payment_methods_from_gateway_by_external_customer_id(
        self,
        external_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Sync Orb's payment methods for the customer with their gateway.

        This method can be called before taking an action that may cause the customer to
        be charged, ensuring that the most up-to-date payment method is charged.

        **Note**: This functionality is currently only available for Stripe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/customers/external_customer_id/{external_customer_id}/sync_payment_methods_from_gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def update_by_external_id(
        self,
        id: str,
        *,
        accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam] | Omit = omit,
        additional_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        auto_issuance: Optional[bool] | Omit = omit,
        billing_address: Optional[AddressInputParam] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        email_delivery: Optional[bool] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        hierarchy: Optional[CustomerHierarchyConfigParam] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
        | Omit = omit,
        payment_provider_id: Optional[str] | Omit = omit,
        reporting_configuration: Optional[NewReportingConfigurationParam] | Omit = omit,
        shipping_address: Optional[AddressInputParam] | Omit = omit,
        tax_configuration: Optional[customer_update_by_external_id_params.TaxConfiguration] | Omit = omit,
        tax_id: Optional[CustomerTaxID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Customer:
        """
        This endpoint is used to update customer details given an `external_customer_id`
        (see [Customer ID Aliases](/events-and-metrics/customer-aliases)). Note that the
        resource and semantics of this endpoint exactly mirror
        [Update Customer](update-customer).

        Args:
          additional_emails: Additional email addresses for this customer. If populated, these email
              addresses will be CC'd for customer communications. The total number of email
              addresses (including the primary email) cannot exceed 50.

          auto_collection: Used to determine if invoices for this customer will automatically attempt to
              charge a saved payment method, if available. This parameter defaults to `True`
              when a payment provider is provided on customer creation.

          auto_issuance: Used to determine if invoices for this customer will be automatically issued. If
              true, invoices will be automatically issued. If false, invoices will require
              manual approval.If `null` is specified, the customer's auto issuance setting
              will be inherited from the account-level setting.

          currency: An ISO 4217 currency string used for the customer's invoices and balance. If not
              set at creation time, will be set at subscription creation time.

          email: A valid customer email, to be used for invoicing and notifications.

          external_customer_id: The external customer ID. This can only be set if the customer has no existing
              external customer ID. Since this action may change usage quantities for all
              existing subscriptions, it is disallowed if the customer has issued invoices
              with usage line items and subject to the same restrictions as backdated
              subscription creation.

          hierarchy: The hierarchical relationships for this customer.

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

              | Country                | Type         | Description                                                                                             |
              | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
              | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
              | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
              | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
              | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
              | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
              | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
              | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
              | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
              | Austria                | `eu_vat`     | European VAT Number                                                                                     |
              | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
              | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
              | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
              | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
              | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
              | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
              | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
              | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
              | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
              | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
              | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
              | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
              | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
              | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
              | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
              | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
              | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
              | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
              | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
              | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
              | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
              | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
              | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
              | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
              | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
              | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
              | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
              | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
              | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
              | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
              | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
              | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
              | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
              | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
              | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
              | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
              | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
              | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
              | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
              | Finland                | `eu_vat`     | European VAT Number                                                                                     |
              | France                 | `eu_vat`     | European VAT Number                                                                                     |
              | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
              | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
              | Germany                | `eu_vat`     | European VAT Number                                                                                     |
              | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
              | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
              | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
              | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
              | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
              | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
              | India                  | `in_gst`     | Indian GST Number                                                                                       |
              | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
              | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
              | Israel                 | `il_vat`     | Israel VAT                                                                                              |
              | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
              | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
              | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
              | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
              | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
              | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
              | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
              | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
              | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
              | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
              | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
              | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
              | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
              | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
              | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
              | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
              | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
              | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
              | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
              | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
              | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
              | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
              | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
              | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
              | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
              | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
              | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
              | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
              | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
              | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
              | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
              | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
              | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
              | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
              | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `eu_vat`     | European VAT Number                                                                                     |
              | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
              | Russia                 | `ru_inn`     | Russian INN                                                                                             |
              | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
              | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
              | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
              | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
              | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
              | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
              | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
              | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
              | South Africa           | `za_vat`     | South African VAT Number                                                                                |
              | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
              | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
              | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
              | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
              | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
              | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
              | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
              | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
              | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
              | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
              | Thailand               | `th_vat`     | Thai VAT                                                                                                |
              | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
              | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
              | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
              | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
              | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
              | United States          | `us_ein`     | United States EIN                                                                                       |
              | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
              | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
              | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
              | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
              | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
              | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
              | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/customers/external_customer_id/{id}",
            body=await async_maybe_transform(
                {
                    "accounting_sync_configuration": accounting_sync_configuration,
                    "additional_emails": additional_emails,
                    "auto_collection": auto_collection,
                    "auto_issuance": auto_issuance,
                    "billing_address": billing_address,
                    "currency": currency,
                    "email": email,
                    "email_delivery": email_delivery,
                    "external_customer_id": external_customer_id,
                    "hierarchy": hierarchy,
                    "metadata": metadata,
                    "name": name,
                    "payment_provider": payment_provider,
                    "payment_provider_id": payment_provider_id,
                    "reporting_configuration": reporting_configuration,
                    "shipping_address": shipping_address,
                    "tax_configuration": tax_configuration,
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
        self._customers = customers

        self.create = _legacy_response.to_raw_response_wrapper(
            customers.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            customers.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            customers.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            customers.delete,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = _legacy_response.to_raw_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.sync_payment_methods_from_gateway = _legacy_response.to_raw_response_wrapper(
            customers.sync_payment_methods_from_gateway,
        )
        self.sync_payment_methods_from_gateway_by_external_customer_id = _legacy_response.to_raw_response_wrapper(
            customers.sync_payment_methods_from_gateway_by_external_customer_id,
        )
        self.update_by_external_id = _legacy_response.to_raw_response_wrapper(
            customers.update_by_external_id,
        )

    @cached_property
    def costs(self) -> CostsWithRawResponse:
        return CostsWithRawResponse(self._customers.costs)

    @cached_property
    def credits(self) -> CreditsWithRawResponse:
        return CreditsWithRawResponse(self._customers.credits)

    @cached_property
    def balance_transactions(self) -> BalanceTransactionsWithRawResponse:
        return BalanceTransactionsWithRawResponse(self._customers.balance_transactions)


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self._customers = customers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            customers.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            customers.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            customers.delete,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.sync_payment_methods_from_gateway = _legacy_response.async_to_raw_response_wrapper(
            customers.sync_payment_methods_from_gateway,
        )
        self.sync_payment_methods_from_gateway_by_external_customer_id = _legacy_response.async_to_raw_response_wrapper(
            customers.sync_payment_methods_from_gateway_by_external_customer_id,
        )
        self.update_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            customers.update_by_external_id,
        )

    @cached_property
    def costs(self) -> AsyncCostsWithRawResponse:
        return AsyncCostsWithRawResponse(self._customers.costs)

    @cached_property
    def credits(self) -> AsyncCreditsWithRawResponse:
        return AsyncCreditsWithRawResponse(self._customers.credits)

    @cached_property
    def balance_transactions(self) -> AsyncBalanceTransactionsWithRawResponse:
        return AsyncBalanceTransactionsWithRawResponse(self._customers.balance_transactions)


class CustomersWithStreamingResponse:
    def __init__(self, customers: Customers) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.delete = to_streamed_response_wrapper(
            customers.delete,
        )
        self.fetch = to_streamed_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = to_streamed_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.sync_payment_methods_from_gateway = to_streamed_response_wrapper(
            customers.sync_payment_methods_from_gateway,
        )
        self.sync_payment_methods_from_gateway_by_external_customer_id = to_streamed_response_wrapper(
            customers.sync_payment_methods_from_gateway_by_external_customer_id,
        )
        self.update_by_external_id = to_streamed_response_wrapper(
            customers.update_by_external_id,
        )

    @cached_property
    def costs(self) -> CostsWithStreamingResponse:
        return CostsWithStreamingResponse(self._customers.costs)

    @cached_property
    def credits(self) -> CreditsWithStreamingResponse:
        return CreditsWithStreamingResponse(self._customers.credits)

    @cached_property
    def balance_transactions(self) -> BalanceTransactionsWithStreamingResponse:
        return BalanceTransactionsWithStreamingResponse(self._customers.balance_transactions)


class AsyncCustomersWithStreamingResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customers.delete,
        )
        self.fetch = async_to_streamed_response_wrapper(
            customers.fetch,
        )
        self.fetch_by_external_id = async_to_streamed_response_wrapper(
            customers.fetch_by_external_id,
        )
        self.sync_payment_methods_from_gateway = async_to_streamed_response_wrapper(
            customers.sync_payment_methods_from_gateway,
        )
        self.sync_payment_methods_from_gateway_by_external_customer_id = async_to_streamed_response_wrapper(
            customers.sync_payment_methods_from_gateway_by_external_customer_id,
        )
        self.update_by_external_id = async_to_streamed_response_wrapper(
            customers.update_by_external_id,
        )

    @cached_property
    def costs(self) -> AsyncCostsWithStreamingResponse:
        return AsyncCostsWithStreamingResponse(self._customers.costs)

    @cached_property
    def credits(self) -> AsyncCreditsWithStreamingResponse:
        return AsyncCreditsWithStreamingResponse(self._customers.credits)

    @cached_property
    def balance_transactions(self) -> AsyncBalanceTransactionsWithStreamingResponse:
        return AsyncBalanceTransactionsWithStreamingResponse(self._customers.balance_transactions)
