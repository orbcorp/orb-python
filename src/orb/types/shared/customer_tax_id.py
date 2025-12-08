# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomerTaxID"]


class CustomerTaxID(BaseModel):
    """
    Tax IDs are commonly required to be displayed on customer invoices, which are added to the headers of invoices.


    ### Supported Tax ID Countries and Types


    | Country | Type | Description |
    |---------|------|-------------|
    | Albania | `al_tin` | Albania Tax Identification Number |
    | Andorra | `ad_nrt` | Andorran NRT Number |
    | Angola | `ao_tin` | Angola Tax Identification Number |
    | Argentina | `ar_cuit` | Argentinian Tax ID Number |
    | Armenia | `am_tin` | Armenia Tax Identification Number |
    | Aruba | `aw_tin` | Aruba Tax Identification Number |
    | Australia | `au_abn` | Australian Business Number (AU ABN) |
    | Australia | `au_arn` | Australian Taxation Office Reference Number |
    | Austria | `eu_vat` | European VAT Number |
    | Azerbaijan | `az_tin` | Azerbaijan Tax Identification Number |
    | Bahamas | `bs_tin` | Bahamas Tax Identification Number |
    | Bahrain | `bh_vat` | Bahraini VAT Number |
    | Bangladesh | `bd_bin` | Bangladesh Business Identification Number |
    | Barbados | `bb_tin` | Barbados Tax Identification Number |
    | Belarus | `by_tin` | Belarus TIN Number |
    | Belgium | `eu_vat` | European VAT Number |
    | Benin | `bj_ifu` | Benin Tax Identification Number (Identifiant Fiscal Unique) |
    | Bolivia | `bo_tin` | Bolivian Tax ID |
    | Bosnia and Herzegovina | `ba_tin` | Bosnia and Herzegovina Tax Identification Number |
    | Brazil | `br_cnpj` | Brazilian CNPJ Number |
    | Brazil | `br_cpf` | Brazilian CPF Number |
    | Bulgaria | `bg_uic` | Bulgaria Unified Identification Code |
    | Bulgaria | `eu_vat` | European VAT Number |
    | Burkina Faso | `bf_ifu` | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique) |
    | Cambodia | `kh_tin` | Cambodia Tax Identification Number |
    | Cameroon | `cm_niu` | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique) |
    | Canada | `ca_bn` | Canadian BN |
    | Canada | `ca_gst_hst` | Canadian GST/HST Number |
    | Canada | `ca_pst_bc` | Canadian PST Number (British Columbia) |
    | Canada | `ca_pst_mb` | Canadian PST Number (Manitoba) |
    | Canada | `ca_pst_sk` | Canadian PST Number (Saskatchewan) |
    | Canada | `ca_qst` | Canadian QST Number (Québec) |
    | Cape Verde | `cv_nif` | Cape Verde Tax Identification Number (Número de Identificação Fiscal) |
    | Chile | `cl_tin` | Chilean TIN |
    | China | `cn_tin` | Chinese Tax ID |
    | Colombia | `co_nit` | Colombian NIT Number |
    | Congo-Kinshasa | `cd_nif` | Congo (DR) Tax Identification Number (Número de Identificação Fiscal) |
    | Costa Rica | `cr_tin` | Costa Rican Tax ID |
    | Croatia | `eu_vat` | European VAT Number |
    | Croatia | `hr_oib` | Croatian Personal Identification Number (OIB) |
    | Cyprus | `eu_vat` | European VAT Number |
    | Czech Republic | `eu_vat` | European VAT Number |
    | Denmark | `eu_vat` | European VAT Number |
    | Dominican Republic | `do_rcn` | Dominican RCN Number |
    | Ecuador | `ec_ruc` | Ecuadorian RUC Number |
    | Egypt | `eg_tin` | Egyptian Tax Identification Number |
    | El Salvador | `sv_nit` | El Salvadorian NIT Number |
    | Estonia | `eu_vat` | European VAT Number |
    | Ethiopia | `et_tin` | Ethiopia Tax Identification Number |
    | European Union | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme |
    | Finland | `eu_vat` | European VAT Number |
    | France | `eu_vat` | European VAT Number |
    | Georgia | `ge_vat` | Georgian VAT |
    | Germany | `de_stn` | German Tax Number (Steuernummer) |
    | Germany | `eu_vat` | European VAT Number |
    | Greece | `eu_vat` | European VAT Number |
    | Guinea | `gn_nif` | Guinea Tax Identification Number (Número de Identificação Fiscal) |
    | Hong Kong | `hk_br` | Hong Kong BR Number |
    | Hungary | `eu_vat` | European VAT Number |
    | Hungary | `hu_tin` | Hungary Tax Number (adószám) |
    | Iceland | `is_vat` | Icelandic VAT |
    | India | `in_gst` | Indian GST Number |
    | Indonesia | `id_npwp` | Indonesian NPWP Number |
    | Ireland | `eu_vat` | European VAT Number |
    | Israel | `il_vat` | Israel VAT |
    | Italy | `eu_vat` | European VAT Number |
    | Japan | `jp_cn` | Japanese Corporate Number (*Hōjin Bangō*) |
    | Japan | `jp_rn` | Japanese Registered Foreign Businesses' Registration Number (*Tōroku Kokugai Jigyōsha no Tōroku Bangō*) |
    | Japan | `jp_trn` | Japanese Tax Registration Number (*Tōroku Bangō*) |
    | Kazakhstan | `kz_bin` | Kazakhstani Business Identification Number |
    | Kenya | `ke_pin` | Kenya Revenue Authority Personal Identification Number |
    | Kyrgyzstan | `kg_tin` | Kyrgyzstan Tax Identification Number |
    | Laos | `la_tin` | Laos Tax Identification Number |
    | Latvia | `eu_vat` | European VAT Number |
    | Liechtenstein | `li_uid` | Liechtensteinian UID Number |
    | Liechtenstein | `li_vat` | Liechtenstein VAT Number |
    | Lithuania | `eu_vat` | European VAT Number |
    | Luxembourg | `eu_vat` | European VAT Number |
    | Malaysia | `my_frp` | Malaysian FRP Number |
    | Malaysia | `my_itn` | Malaysian ITN |
    | Malaysia | `my_sst` | Malaysian SST Number |
    | Malta | `eu_vat` | European VAT Number |
    | Mauritania | `mr_nif` | Mauritania Tax Identification Number (Número de Identificação Fiscal) |
    | Mexico | `mx_rfc` | Mexican RFC Number |
    | Moldova | `md_vat` | Moldova VAT Number |
    | Montenegro | `me_pib` | Montenegro PIB Number |
    | Morocco | `ma_vat` | Morocco VAT Number |
    | Nepal | `np_pan` | Nepal PAN Number |
    | Netherlands | `eu_vat` | European VAT Number |
    | New Zealand | `nz_gst` | New Zealand GST Number |
    | Nigeria | `ng_tin` | Nigerian Tax Identification Number |
    | North Macedonia | `mk_vat` | North Macedonia VAT Number |
    | Northern Ireland | `eu_vat` | Northern Ireland VAT Number |
    | Norway | `no_vat` | Norwegian VAT Number |
    | Norway | `no_voec` | Norwegian VAT on e-commerce Number |
    | Oman | `om_vat` | Omani VAT Number |
    | Peru | `pe_ruc` | Peruvian RUC Number |
    | Philippines | `ph_tin` | Philippines Tax Identification Number |
    | Poland | `eu_vat` | European VAT Number |
    | Portugal | `eu_vat` | European VAT Number |
    | Romania | `eu_vat` | European VAT Number |
    | Romania | `ro_tin` | Romanian Tax ID Number |
    | Russia | `ru_inn` | Russian INN |
    | Russia | `ru_kpp` | Russian KPP |
    | Saudi Arabia | `sa_vat` | Saudi Arabia VAT |
    | Senegal | `sn_ninea` | Senegal NINEA Number |
    | Serbia | `rs_pib` | Serbian PIB Number |
    | Singapore | `sg_gst` | Singaporean GST |
    | Singapore | `sg_uen` | Singaporean UEN |
    | Slovakia | `eu_vat` | European VAT Number |
    | Slovenia | `eu_vat` | European VAT Number |
    | Slovenia | `si_tin` | Slovenia Tax Number (davčna številka) |
    | South Africa | `za_vat` | South African VAT Number |
    | South Korea | `kr_brn` | Korean BRN |
    | Spain | `es_cif` | Spanish NIF Number (previously Spanish CIF Number) |
    | Spain | `eu_vat` | European VAT Number |
    | Suriname | `sr_fin` | Suriname FIN Number |
    | Sweden | `eu_vat` | European VAT Number |
    | Switzerland | `ch_uid` | Switzerland UID Number |
    | Switzerland | `ch_vat` | Switzerland VAT Number |
    | Taiwan | `tw_vat` | Taiwanese VAT |
    | Tajikistan | `tj_tin` | Tajikistan Tax Identification Number |
    | Tanzania | `tz_vat` | Tanzania VAT Number |
    | Thailand | `th_vat` | Thai VAT |
    | Turkey | `tr_tin` | Turkish Tax Identification Number |
    | Uganda | `ug_tin` | Uganda Tax Identification Number |
    | Ukraine | `ua_vat` | Ukrainian VAT |
    | United Arab Emirates | `ae_trn` | United Arab Emirates TRN |
    | United Kingdom | `gb_vat` | United Kingdom VAT Number |
    | United States | `us_ein` | United States EIN |
    | Uruguay | `uy_ruc` | Uruguayan RUC Number |
    | Uzbekistan | `uz_tin` | Uzbekistan TIN Number |
    | Uzbekistan | `uz_vat` | Uzbekistan VAT Number |
    | Venezuela | `ve_rif` | Venezuelan RIF Number |
    | Vietnam | `vn_tin` | Vietnamese Tax ID Number |
    | Zambia | `zm_tin` | Zambia Tax Identification Number |
    | Zimbabwe | `zw_tin` | Zimbabwe Tax Identification Number |
    """

    country: Literal[
        "AD",
        "AE",
        "AL",
        "AM",
        "AO",
        "AR",
        "AT",
        "AU",
        "AW",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BJ",
        "BO",
        "BR",
        "BS",
        "BY",
        "CA",
        "CD",
        "CH",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CV",
        "DE",
        "CY",
        "CZ",
        "DK",
        "DO",
        "EC",
        "EE",
        "EG",
        "ES",
        "ET",
        "EU",
        "FI",
        "FR",
        "GB",
        "GE",
        "GN",
        "GR",
        "HK",
        "HR",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IS",
        "IT",
        "JP",
        "KE",
        "KG",
        "KH",
        "KR",
        "KZ",
        "LA",
        "LI",
        "LT",
        "LU",
        "LV",
        "MA",
        "MD",
        "ME",
        "MK",
        "MR",
        "MT",
        "MX",
        "MY",
        "NG",
        "NL",
        "NO",
        "NP",
        "NZ",
        "OM",
        "PE",
        "PH",
        "PL",
        "PT",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "SN",
        "SR",
        "SV",
        "TH",
        "TJ",
        "TR",
        "TW",
        "TZ",
        "UA",
        "UG",
        "US",
        "UY",
        "UZ",
        "VE",
        "VN",
        "ZA",
        "ZM",
        "ZW",
    ]

    type: Literal[
        "ad_nrt",
        "ae_trn",
        "al_tin",
        "am_tin",
        "ao_tin",
        "ar_cuit",
        "eu_vat",
        "au_abn",
        "au_arn",
        "aw_tin",
        "az_tin",
        "ba_tin",
        "bb_tin",
        "bd_bin",
        "bf_ifu",
        "bg_uic",
        "bh_vat",
        "bj_ifu",
        "bo_tin",
        "br_cnpj",
        "br_cpf",
        "bs_tin",
        "by_tin",
        "ca_bn",
        "ca_gst_hst",
        "ca_pst_bc",
        "ca_pst_mb",
        "ca_pst_sk",
        "ca_qst",
        "cd_nif",
        "ch_uid",
        "ch_vat",
        "cl_tin",
        "cm_niu",
        "cn_tin",
        "co_nit",
        "cr_tin",
        "cv_nif",
        "de_stn",
        "do_rcn",
        "ec_ruc",
        "eg_tin",
        "es_cif",
        "et_tin",
        "eu_oss_vat",
        "gb_vat",
        "ge_vat",
        "gn_nif",
        "hk_br",
        "hr_oib",
        "hu_tin",
        "id_npwp",
        "il_vat",
        "in_gst",
        "is_vat",
        "jp_cn",
        "jp_rn",
        "jp_trn",
        "ke_pin",
        "kg_tin",
        "kh_tin",
        "kr_brn",
        "kz_bin",
        "la_tin",
        "li_uid",
        "li_vat",
        "ma_vat",
        "md_vat",
        "me_pib",
        "mk_vat",
        "mr_nif",
        "mx_rfc",
        "my_frp",
        "my_itn",
        "my_sst",
        "ng_tin",
        "no_vat",
        "no_voec",
        "np_pan",
        "nz_gst",
        "om_vat",
        "pe_ruc",
        "ph_tin",
        "ro_tin",
        "rs_pib",
        "ru_inn",
        "ru_kpp",
        "sa_vat",
        "sg_gst",
        "sg_uen",
        "si_tin",
        "sn_ninea",
        "sr_fin",
        "sv_nit",
        "th_vat",
        "tj_tin",
        "tr_tin",
        "tw_vat",
        "tz_vat",
        "ua_vat",
        "ug_tin",
        "us_ein",
        "uy_ruc",
        "uz_tin",
        "uz_vat",
        "ve_rif",
        "vn_tin",
        "za_vat",
        "zm_tin",
        "zw_tin",
    ]

    value: str
