# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .customer_payment_gateway_connection import CustomerPaymentGatewayConnection

__all__ = ["PaymentGatewayConnectionListResponse"]


class PaymentGatewayConnectionListResponse(BaseModel):
    customer_id: str

    payment_gateway_connections: List[CustomerPaymentGatewayConnection]
