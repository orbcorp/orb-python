# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["NewTaxConfigurationModel", "NewAvalaraTaxConfiguration", "NewTaxJarConfiguration"]


class NewAvalaraTaxConfiguration(BaseModel):
    tax_exempt: bool

    tax_provider: Literal["avalara"]

    tax_exemption_code: Optional[str] = None


class NewTaxJarConfiguration(BaseModel):
    tax_exempt: bool

    tax_provider: Literal["taxjar"]


NewTaxConfigurationModel: TypeAlias = Annotated[
    Union[NewAvalaraTaxConfiguration, NewTaxJarConfiguration], PropertyInfo(discriminator="tax_provider")
]
