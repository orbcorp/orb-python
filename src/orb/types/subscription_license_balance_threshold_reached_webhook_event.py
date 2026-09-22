# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.customer_minified import CustomerMinified
from .shared.subscription_minified import SubscriptionMinified

__all__ = [
    "SubscriptionLicenseBalanceThresholdReachedWebhookEvent",
    "Properties",
    "PropertiesAlertConfiguration",
    "PropertiesAlertConfigurationMetric",
    "PropertiesAlertConfigurationPlan",
    "PropertiesAlertConfigurationThreshold",
    "PropertiesAlertConfigurationBalanceAlertStatus",
    "PropertiesAlertConfigurationLicenseType",
    "PropertiesAlertConfigurationPriceFilter",
    "PropertiesAlertConfigurationThresholdOverride",
    "PropertiesAlertConfigurationThresholdOverrideThreshold",
    "PropertiesLicense",
    "Subscription",
    "SubscriptionPlan",
]


class PropertiesAlertConfigurationMetric(BaseModel):
    """The metric the alert applies to."""

    id: str


class PropertiesAlertConfigurationPlan(BaseModel):
    """The plan the alert applies to."""

    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None

    plan_version: str


class PropertiesAlertConfigurationThreshold(BaseModel):
    """
    Thresholds are used to define the conditions under which an alert will be triggered.
    """

    value: str
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """


class PropertiesAlertConfigurationBalanceAlertStatus(BaseModel):
    """Alert status is used to determine if an alert is currently in-alert or not."""

    in_alert: bool
    """Whether the alert is currently in-alert or not."""

    threshold_value: str
    """The value of the threshold that defines the alert status."""


class PropertiesAlertConfigurationLicenseType(BaseModel):
    """Minified license type for alert serialization."""

    id: str


class PropertiesAlertConfigurationPriceFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PropertiesAlertConfigurationThresholdOverrideThreshold(BaseModel):
    """
    Thresholds are used to define the conditions under which an alert will be triggered.
    """

    value: str
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """


class PropertiesAlertConfigurationThresholdOverride(BaseModel):
    """A per-group threshold override on a grouped cost alert.

    An empty `thresholds` list means the group is silenced (never fires).
    A non-empty list fully replaces the default thresholds for that group.
    """

    group_values: List[str]
    """
    The values identifying this group, ordered to match group_keys when set and the
    alert's grouping_keys otherwise.
    """

    thresholds: List[PropertiesAlertConfigurationThresholdOverrideThreshold]
    """The thresholds applied to this group.

    An empty list means the group is silenced.
    """

    group_keys: Optional[List[str]] = None
    """The subset of the alert's grouping_keys this override binds.

    Null when the override targets one exact group across every grouping key.
    """


class PropertiesAlertConfiguration(BaseModel):
    """
    [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
    usage, or credit balance and trigger webhooks when a threshold is exceeded.

    Alerts created through the API can be scoped to either customers or subscriptions.
    """

    id: str
    """Also referred to as alert_id in this documentation."""

    created_at: datetime
    """The creation time of the resource in Orb."""

    currency: Optional[str] = None
    """The name of the currency the credit balance or invoice cost is denominated in."""

    customer: Optional[CustomerMinified] = None
    """The customer the alert applies to."""

    enabled: bool
    """Whether the alert is enabled or disabled."""

    metric: Optional[PropertiesAlertConfigurationMetric] = None
    """The metric the alert applies to."""

    plan: Optional[PropertiesAlertConfigurationPlan] = None
    """The plan the alert applies to."""

    subscription: Optional[SubscriptionMinified] = None
    """The subscription the alert applies to."""

    thresholds: Optional[List[PropertiesAlertConfigurationThreshold]] = None
    """
    The thresholds that define the conditions under which the alert will be
    triggered.
    """

    type: Literal[
        "credit_balance_depleted",
        "credit_balance_dropped",
        "credit_balance_recovered",
        "usage_exceeded",
        "cost_exceeded",
        "spend_exceeded",
        "license_balance_threshold_reached",
    ]
    """The type of alert. This must be a valid alert type."""

    balance_alert_status: Optional[List[PropertiesAlertConfigurationBalanceAlertStatus]] = None
    """The current status of the alert.

    This field is only present for credit balance alerts.
    """

    grouping_keys: Optional[List[str]] = None
    """The property keys to group cost alerts by.

    Only present for cost alerts with grouping enabled.
    """

    license_type: Optional[PropertiesAlertConfigurationLicenseType] = None
    """Minified license type for alert serialization."""

    price_filters: Optional[List[PropertiesAlertConfigurationPriceFilter]] = None
    """
    Filters scoping which prices are included in spend and grouped cost alert
    evaluation. Alerts use the price_id, item_id, and price_type fields only; the
    alert's pricing unit is reported by currency.
    """

    threshold_overrides: Optional[List[PropertiesAlertConfigurationThresholdOverride]] = None
    """Per-group threshold overrides.

    Each override maps a specific combination of grouping_keys values to a
    replacement threshold list. Only present for grouped cost alerts that have at
    least one override.
    """


class PropertiesLicense(BaseModel):
    external_license_id: str

    license_type_id: str

    threshold_percentage: str


class Properties(BaseModel):
    """
    Every license that crossed a threshold for one alert, batched into a single message. For
    account-wide alerts the licenses may span several license types.
    """

    alert_configuration: PropertiesAlertConfiguration
    """
    [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
    usage, or credit balance and trigger webhooks when a threshold is exceeded.

    Alerts created through the API can be scoped to either customers or
    subscriptions.
    """

    licenses: List[PropertiesLicense]

    timeframe_end: datetime

    timeframe_start: datetime


class SubscriptionPlan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class Subscription(BaseModel):
    """A lightweight subscription representation for webhook payloads.

    This avoids the expensive to_subscription_params() call required for full serialization.
    """

    id: str

    customer: CustomerMinified

    end_date: Optional[datetime] = None

    plan: Optional[SubscriptionPlan] = None

    start_date: datetime

    status: Literal["active", "ended", "upcoming"]


class SubscriptionLicenseBalanceThresholdReachedWebhookEvent(BaseModel):
    """Issued when a license balance threshold is reached."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties
    """
    Every license that crossed a threshold for one alert, batched into a single
    message. For account-wide alerts the licenses may span several license types.
    """

    subscription: Subscription
    """A lightweight subscription representation for webhook payloads.

    This avoids the expensive to_subscription_params() call required for full
    serialization.
    """

    type: Literal["subscription.license_balance_threshold_reached"]
    """The event this payload describes."""
