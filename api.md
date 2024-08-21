# Shared Types

```python
from orb.types import BillingCycleRelativeDate, Discount, PaginationMetadata
```

# TopLevel

Types:

```python
from orb.types import TopLevelPingResponse
```

Methods:

- <code title="get /ping">client.top_level.<a href="./src/orb/resources/top_level.py">ping</a>() -> <a href="./src/orb/types/top_level_ping_response.py">TopLevelPingResponse</a></code>

# Coupons

Types:

```python
from orb.types import Coupon
```

Methods:

- <code title="post /coupons">client.coupons.<a href="./src/orb/resources/coupons/coupons.py">create</a>(\*\*<a href="src/orb/types/coupon_create_params.py">params</a>) -> <a href="./src/orb/types/coupon.py">Coupon</a></code>
- <code title="get /coupons">client.coupons.<a href="./src/orb/resources/coupons/coupons.py">list</a>(\*\*<a href="src/orb/types/coupon_list_params.py">params</a>) -> <a href="./src/orb/types/coupon.py">SyncPage[Coupon]</a></code>
- <code title="post /coupons/{coupon_id}/archive">client.coupons.<a href="./src/orb/resources/coupons/coupons.py">archive</a>(coupon_id) -> <a href="./src/orb/types/coupon.py">Coupon</a></code>
- <code title="get /coupons/{coupon_id}">client.coupons.<a href="./src/orb/resources/coupons/coupons.py">fetch</a>(coupon_id) -> <a href="./src/orb/types/coupon.py">Coupon</a></code>

## Subscriptions

Methods:

- <code title="get /coupons/{coupon_id}/subscriptions">client.coupons.subscriptions.<a href="./src/orb/resources/coupons/subscriptions.py">list</a>(coupon_id, \*\*<a href="src/orb/types/coupons/subscription_list_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">SyncPage[Subscription]</a></code>

# CreditNotes

Types:

```python
from orb.types import CreditNote
```

Methods:

- <code title="get /credit_notes">client.credit_notes.<a href="./src/orb/resources/credit_notes.py">list</a>(\*\*<a href="src/orb/types/credit_note_list_params.py">params</a>) -> <a href="./src/orb/types/credit_note.py">SyncPage[CreditNote]</a></code>
- <code title="get /credit_notes/{credit_note_id}">client.credit_notes.<a href="./src/orb/resources/credit_notes.py">fetch</a>(credit_note_id) -> <a href="./src/orb/types/credit_note.py">CreditNote</a></code>

# Customers

Types:

```python
from orb.types import Customer
```

Methods:

- <code title="post /customers">client.customers.<a href="./src/orb/resources/customers/customers.py">create</a>(\*\*<a href="src/orb/types/customer_create_params.py">params</a>) -> <a href="./src/orb/types/customer.py">Customer</a></code>
- <code title="put /customers/{customer_id}">client.customers.<a href="./src/orb/resources/customers/customers.py">update</a>(customer_id, \*\*<a href="src/orb/types/customer_update_params.py">params</a>) -> <a href="./src/orb/types/customer.py">Customer</a></code>
- <code title="get /customers">client.customers.<a href="./src/orb/resources/customers/customers.py">list</a>(\*\*<a href="src/orb/types/customer_list_params.py">params</a>) -> <a href="./src/orb/types/customer.py">SyncPage[Customer]</a></code>
- <code title="delete /customers/{customer_id}">client.customers.<a href="./src/orb/resources/customers/customers.py">delete</a>(customer_id) -> None</code>
- <code title="get /customers/{customer_id}">client.customers.<a href="./src/orb/resources/customers/customers.py">fetch</a>(customer_id) -> <a href="./src/orb/types/customer.py">Customer</a></code>
- <code title="get /customers/external_customer_id/{external_customer_id}">client.customers.<a href="./src/orb/resources/customers/customers.py">fetch_by_external_id</a>(external_customer_id) -> <a href="./src/orb/types/customer.py">Customer</a></code>
- <code title="put /customers/external_customer_id/{external_customer_id}">client.customers.<a href="./src/orb/resources/customers/customers.py">update_by_external_id</a>(id, \*\*<a href="src/orb/types/customer_update_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customer.py">Customer</a></code>

## Costs

Types:

```python
from orb.types.customers import CostListResponse, CostListByExternalIDResponse
```

Methods:

- <code title="get /customers/{customer_id}/costs">client.customers.costs.<a href="./src/orb/resources/customers/costs.py">list</a>(customer_id, \*\*<a href="src/orb/types/customers/cost_list_params.py">params</a>) -> <a href="./src/orb/types/customers/cost_list_response.py">CostListResponse</a></code>
- <code title="get /customers/external_customer_id/{external_customer_id}/costs">client.customers.costs.<a href="./src/orb/resources/customers/costs.py">list_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/cost_list_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/cost_list_by_external_id_response.py">CostListByExternalIDResponse</a></code>

## Credits

Types:

```python
from orb.types.customers import CreditListResponse, CreditListByExternalIDResponse
```

Methods:

- <code title="get /customers/{customer_id}/credits">client.customers.credits.<a href="./src/orb/resources/customers/credits/credits.py">list</a>(customer_id, \*\*<a href="src/orb/types/customers/credit_list_params.py">params</a>) -> <a href="./src/orb/types/customers/credit_list_response.py">SyncPage[CreditListResponse]</a></code>
- <code title="get /customers/external_customer_id/{external_customer_id}/credits">client.customers.credits.<a href="./src/orb/resources/customers/credits/credits.py">list_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/credit_list_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/credit_list_by_external_id_response.py">SyncPage[CreditListByExternalIDResponse]</a></code>

### Ledger

Types:

```python
from orb.types.customers.credits import (
    LedgerListResponse,
    LedgerCreateEntryResponse,
    LedgerCreateEntryByExternalIDResponse,
    LedgerListByExternalIDResponse,
)
```

Methods:

- <code title="get /customers/{customer_id}/credits/ledger">client.customers.credits.ledger.<a href="./src/orb/resources/customers/credits/ledger.py">list</a>(customer_id, \*\*<a href="src/orb/types/customers/credits/ledger_list_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/ledger_list_response.py">SyncPage[LedgerListResponse]</a></code>
- <code title="post /customers/{customer_id}/credits/ledger_entry">client.customers.credits.ledger.<a href="./src/orb/resources/customers/credits/ledger.py">create_entry</a>(customer_id, \*\*<a href="src/orb/types/customers/credits/ledger_create_entry_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/ledger_create_entry_response.py">LedgerCreateEntryResponse</a></code>
- <code title="post /customers/external_customer_id/{external_customer_id}/credits/ledger_entry">client.customers.credits.ledger.<a href="./src/orb/resources/customers/credits/ledger.py">create_entry_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/credits/ledger_create_entry_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/ledger_create_entry_by_external_id_response.py">LedgerCreateEntryByExternalIDResponse</a></code>
- <code title="get /customers/external_customer_id/{external_customer_id}/credits/ledger">client.customers.credits.ledger.<a href="./src/orb/resources/customers/credits/ledger.py">list_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/credits/ledger_list_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/ledger_list_by_external_id_response.py">SyncPage[LedgerListByExternalIDResponse]</a></code>

### TopUps

Types:

```python
from orb.types.customers.credits import (
    TopUpCreateResponse,
    TopUpListResponse,
    TopUpCreateByExternalIDResponse,
    TopUpListByExternalIDResponse,
)
```

Methods:

- <code title="post /customers/{customer_id}/credits/top_ups">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">create</a>(customer_id, \*\*<a href="src/orb/types/customers/credits/top_up_create_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/top_up_create_response.py">TopUpCreateResponse</a></code>
- <code title="get /customers/{customer_id}/credits/top_ups">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">list</a>(customer_id, \*\*<a href="src/orb/types/customers/credits/top_up_list_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/top_up_list_response.py">SyncPage[TopUpListResponse]</a></code>
- <code title="delete /customers/{customer_id}/credits/top_ups/{top_up_id}">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">delete</a>(top_up_id, \*, customer_id) -> None</code>
- <code title="post /customers/external_customer_id/{external_customer_id}/credits/top_ups">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">create_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/credits/top_up_create_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/top_up_create_by_external_id_response.py">TopUpCreateByExternalIDResponse</a></code>
- <code title="delete /customers/external_customer_id/{external_customer_id}/credits/top_ups/{top_up_id}">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">delete_by_external_id</a>(top_up_id, \*, external_customer_id) -> None</code>
- <code title="get /customers/external_customer_id/{external_customer_id}/credits/top_ups">client.customers.credits.top_ups.<a href="./src/orb/resources/customers/credits/top_ups.py">list_by_external_id</a>(external_customer_id, \*\*<a href="src/orb/types/customers/credits/top_up_list_by_external_id_params.py">params</a>) -> <a href="./src/orb/types/customers/credits/top_up_list_by_external_id_response.py">SyncPage[TopUpListByExternalIDResponse]</a></code>

## BalanceTransactions

Types:

```python
from orb.types.customers import BalanceTransactionCreateResponse, BalanceTransactionListResponse
```

Methods:

- <code title="post /customers/{customer_id}/balance_transactions">client.customers.balance_transactions.<a href="./src/orb/resources/customers/balance_transactions.py">create</a>(customer_id, \*\*<a href="src/orb/types/customers/balance_transaction_create_params.py">params</a>) -> <a href="./src/orb/types/customers/balance_transaction_create_response.py">BalanceTransactionCreateResponse</a></code>
- <code title="get /customers/{customer_id}/balance_transactions">client.customers.balance_transactions.<a href="./src/orb/resources/customers/balance_transactions.py">list</a>(customer_id, \*\*<a href="src/orb/types/customers/balance_transaction_list_params.py">params</a>) -> <a href="./src/orb/types/customers/balance_transaction_list_response.py">SyncPage[BalanceTransactionListResponse]</a></code>

# Events

Types:

```python
from orb.types import (
    EventUpdateResponse,
    EventDeprecateResponse,
    EventIngestResponse,
    EventSearchResponse,
)
```

Methods:

- <code title="put /events/{event_id}">client.events.<a href="./src/orb/resources/events/events.py">update</a>(event_id, \*\*<a href="src/orb/types/event_update_params.py">params</a>) -> <a href="./src/orb/types/event_update_response.py">EventUpdateResponse</a></code>
- <code title="put /events/{event_id}/deprecate">client.events.<a href="./src/orb/resources/events/events.py">deprecate</a>(event_id) -> <a href="./src/orb/types/event_deprecate_response.py">EventDeprecateResponse</a></code>
- <code title="post /ingest">client.events.<a href="./src/orb/resources/events/events.py">ingest</a>(\*\*<a href="src/orb/types/event_ingest_params.py">params</a>) -> <a href="./src/orb/types/event_ingest_response.py">EventIngestResponse</a></code>
- <code title="post /events/search">client.events.<a href="./src/orb/resources/events/events.py">search</a>(\*\*<a href="src/orb/types/event_search_params.py">params</a>) -> <a href="./src/orb/types/event_search_response.py">EventSearchResponse</a></code>

## Backfills

Types:

```python
from orb.types.events import (
    BackfillCreateResponse,
    BackfillListResponse,
    BackfillCloseResponse,
    BackfillFetchResponse,
    BackfillRevertResponse,
)
```

Methods:

- <code title="post /events/backfills">client.events.backfills.<a href="./src/orb/resources/events/backfills.py">create</a>(\*\*<a href="src/orb/types/events/backfill_create_params.py">params</a>) -> <a href="./src/orb/types/events/backfill_create_response.py">BackfillCreateResponse</a></code>
- <code title="get /events/backfills">client.events.backfills.<a href="./src/orb/resources/events/backfills.py">list</a>(\*\*<a href="src/orb/types/events/backfill_list_params.py">params</a>) -> <a href="./src/orb/types/events/backfill_list_response.py">SyncPage[BackfillListResponse]</a></code>
- <code title="post /events/backfills/{backfill_id}/close">client.events.backfills.<a href="./src/orb/resources/events/backfills.py">close</a>(backfill_id) -> <a href="./src/orb/types/events/backfill_close_response.py">BackfillCloseResponse</a></code>
- <code title="get /events/backfills/{backfill_id}">client.events.backfills.<a href="./src/orb/resources/events/backfills.py">fetch</a>(backfill_id) -> <a href="./src/orb/types/events/backfill_fetch_response.py">BackfillFetchResponse</a></code>
- <code title="post /events/backfills/{backfill_id}/revert">client.events.backfills.<a href="./src/orb/resources/events/backfills.py">revert</a>(backfill_id) -> <a href="./src/orb/types/events/backfill_revert_response.py">BackfillRevertResponse</a></code>

# InvoiceLineItems

Types:

```python
from orb.types import InvoiceLineItemCreateResponse
```

Methods:

- <code title="post /invoice_line_items">client.invoice_line_items.<a href="./src/orb/resources/invoice_line_items.py">create</a>(\*\*<a href="src/orb/types/invoice_line_item_create_params.py">params</a>) -> <a href="./src/orb/types/invoice_line_item_create_response.py">InvoiceLineItemCreateResponse</a></code>

# Invoices

Types:

```python
from orb.types import Invoice, InvoiceFetchUpcomingResponse
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/orb/resources/invoices.py">create</a>(\*\*<a href="src/orb/types/invoice_create_params.py">params</a>) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>
- <code title="put /invoices/{invoice_id}">client.invoices.<a href="./src/orb/resources/invoices.py">update</a>(invoice_id, \*\*<a href="src/orb/types/invoice_update_params.py">params</a>) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/orb/resources/invoices.py">list</a>(\*\*<a href="src/orb/types/invoice_list_params.py">params</a>) -> <a href="./src/orb/types/invoice.py">SyncPage[Invoice]</a></code>
- <code title="get /invoices/{invoice_id}">client.invoices.<a href="./src/orb/resources/invoices.py">fetch</a>(invoice_id) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>
- <code title="get /invoices/upcoming">client.invoices.<a href="./src/orb/resources/invoices.py">fetch_upcoming</a>(\*\*<a href="src/orb/types/invoice_fetch_upcoming_params.py">params</a>) -> <a href="./src/orb/types/invoice_fetch_upcoming_response.py">InvoiceFetchUpcomingResponse</a></code>
- <code title="post /invoices/{invoice_id}/issue">client.invoices.<a href="./src/orb/resources/invoices.py">issue</a>(invoice_id) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>
- <code title="post /invoices/{invoice_id}/mark_paid">client.invoices.<a href="./src/orb/resources/invoices.py">mark_paid</a>(invoice_id, \*\*<a href="src/orb/types/invoice_mark_paid_params.py">params</a>) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>
- <code title="post /invoices/{invoice_id}/void">client.invoices.<a href="./src/orb/resources/invoices.py">void</a>(invoice_id) -> <a href="./src/orb/types/invoice.py">Invoice</a></code>

# Items

Types:

```python
from orb.types import Item
```

Methods:

- <code title="post /items">client.items.<a href="./src/orb/resources/items.py">create</a>(\*\*<a href="src/orb/types/item_create_params.py">params</a>) -> <a href="./src/orb/types/item.py">Item</a></code>
- <code title="put /items/{item_id}">client.items.<a href="./src/orb/resources/items.py">update</a>(item_id, \*\*<a href="src/orb/types/item_update_params.py">params</a>) -> <a href="./src/orb/types/item.py">Item</a></code>
- <code title="get /items">client.items.<a href="./src/orb/resources/items.py">list</a>(\*\*<a href="src/orb/types/item_list_params.py">params</a>) -> <a href="./src/orb/types/item.py">SyncPage[Item]</a></code>
- <code title="get /items/{item_id}">client.items.<a href="./src/orb/resources/items.py">fetch</a>(item_id) -> <a href="./src/orb/types/item.py">Item</a></code>

# Metrics

Types:

```python
from orb.types import BillableMetric
```

Methods:

- <code title="post /metrics">client.metrics.<a href="./src/orb/resources/metrics.py">create</a>(\*\*<a href="src/orb/types/metric_create_params.py">params</a>) -> <a href="./src/orb/types/billable_metric.py">BillableMetric</a></code>
- <code title="put /metrics/{metric_id}">client.metrics.<a href="./src/orb/resources/metrics.py">update</a>(metric_id, \*\*<a href="src/orb/types/metric_update_params.py">params</a>) -> <a href="./src/orb/types/billable_metric.py">BillableMetric</a></code>
- <code title="get /metrics">client.metrics.<a href="./src/orb/resources/metrics.py">list</a>(\*\*<a href="src/orb/types/metric_list_params.py">params</a>) -> <a href="./src/orb/types/billable_metric.py">SyncPage[BillableMetric]</a></code>
- <code title="get /metrics/{metric_id}">client.metrics.<a href="./src/orb/resources/metrics.py">fetch</a>(metric_id) -> <a href="./src/orb/types/billable_metric.py">BillableMetric</a></code>

# Plans

Types:

```python
from orb.types import Plan
```

Methods:

- <code title="post /plans">client.plans.<a href="./src/orb/resources/plans/plans.py">create</a>(\*\*<a href="src/orb/types/plan_create_params.py">params</a>) -> <a href="./src/orb/types/plan.py">Plan</a></code>
- <code title="put /plans/{plan_id}">client.plans.<a href="./src/orb/resources/plans/plans.py">update</a>(plan_id, \*\*<a href="src/orb/types/plan_update_params.py">params</a>) -> <a href="./src/orb/types/plan.py">Plan</a></code>
- <code title="get /plans">client.plans.<a href="./src/orb/resources/plans/plans.py">list</a>(\*\*<a href="src/orb/types/plan_list_params.py">params</a>) -> <a href="./src/orb/types/plan.py">SyncPage[Plan]</a></code>
- <code title="get /plans/{plan_id}">client.plans.<a href="./src/orb/resources/plans/plans.py">fetch</a>(plan_id) -> <a href="./src/orb/types/plan.py">Plan</a></code>

## ExternalPlanID

Methods:

- <code title="put /plans/external_plan_id/{external_plan_id}">client.plans.external_plan_id.<a href="./src/orb/resources/plans/external_plan_id.py">update</a>(other_external_plan_id, \*\*<a href="src/orb/types/plans/external_plan_id_update_params.py">params</a>) -> <a href="./src/orb/types/plan.py">Plan</a></code>
- <code title="get /plans/external_plan_id/{external_plan_id}">client.plans.external_plan_id.<a href="./src/orb/resources/plans/external_plan_id.py">fetch</a>(external_plan_id) -> <a href="./src/orb/types/plan.py">Plan</a></code>

# Prices

Types:

```python
from orb.types import EvaluatePriceGroup, Price, PriceEvaluateResponse
```

Methods:

- <code title="post /prices">client.prices.<a href="./src/orb/resources/prices/prices.py">create</a>(\*\*<a href="src/orb/types/price_create_params.py">params</a>) -> <a href="./src/orb/types/price.py">Price</a></code>
- <code title="put /prices/{price_id}">client.prices.<a href="./src/orb/resources/prices/prices.py">update</a>(price_id, \*\*<a href="src/orb/types/price_update_params.py">params</a>) -> <a href="./src/orb/types/price.py">Price</a></code>
- <code title="get /prices">client.prices.<a href="./src/orb/resources/prices/prices.py">list</a>(\*\*<a href="src/orb/types/price_list_params.py">params</a>) -> <a href="./src/orb/types/price.py">SyncPage[Price]</a></code>
- <code title="post /prices/{price_id}/evaluate">client.prices.<a href="./src/orb/resources/prices/prices.py">evaluate</a>(price_id, \*\*<a href="src/orb/types/price_evaluate_params.py">params</a>) -> <a href="./src/orb/types/price_evaluate_response.py">PriceEvaluateResponse</a></code>
- <code title="get /prices/{price_id}">client.prices.<a href="./src/orb/resources/prices/prices.py">fetch</a>(price_id) -> <a href="./src/orb/types/price.py">Price</a></code>

## ExternalPriceID

Methods:

- <code title="put /prices/external_price_id/{external_price_id}">client.prices.external_price_id.<a href="./src/orb/resources/prices/external_price_id.py">update</a>(external_price_id, \*\*<a href="src/orb/types/prices/external_price_id_update_params.py">params</a>) -> <a href="./src/orb/types/price.py">Price</a></code>
- <code title="get /prices/external_price_id/{external_price_id}">client.prices.external_price_id.<a href="./src/orb/resources/prices/external_price_id.py">fetch</a>(external_price_id) -> <a href="./src/orb/types/price.py">Price</a></code>

# Subscriptions

Types:

```python
from orb.types import (
    Subscription,
    SubscriptionUsage,
    Subscriptions,
    SubscriptionFetchCostsResponse,
    SubscriptionFetchScheduleResponse,
)
```

Methods:

- <code title="post /subscriptions">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">create</a>(\*\*<a href="src/orb/types/subscription_create_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="put /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">update</a>(subscription_id, \*\*<a href="src/orb/types/subscription_update_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">list</a>(\*\*<a href="src/orb/types/subscription_list_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">SyncPage[Subscription]</a></code>
- <code title="post /subscriptions/{subscription_id}/cancel">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">cancel</a>(subscription_id, \*\*<a href="src/orb/types/subscription_cancel_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">fetch</a>(subscription_id) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions/{subscription_id}/costs">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">fetch_costs</a>(subscription_id, \*\*<a href="src/orb/types/subscription_fetch_costs_params.py">params</a>) -> <a href="./src/orb/types/subscription_fetch_costs_response.py">SubscriptionFetchCostsResponse</a></code>
- <code title="get /subscriptions/{subscription_id}/schedule">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">fetch_schedule</a>(subscription_id, \*\*<a href="src/orb/types/subscription_fetch_schedule_params.py">params</a>) -> <a href="./src/orb/types/subscription_fetch_schedule_response.py">SyncPage[SubscriptionFetchScheduleResponse]</a></code>
- <code title="get /subscriptions/{subscription_id}/usage">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">fetch_usage</a>(subscription_id, \*\*<a href="src/orb/types/subscription_fetch_usage_params.py">params</a>) -> <a href="./src/orb/types/subscription_usage.py">SubscriptionUsage</a></code>
- <code title="post /subscriptions/{subscription_id}/price_intervals">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">price_intervals</a>(subscription_id, \*\*<a href="src/orb/types/subscription_price_intervals_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/schedule_plan_change">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">schedule_plan_change</a>(subscription_id, \*\*<a href="src/orb/types/subscription_schedule_plan_change_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/trigger_phase">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">trigger_phase</a>(subscription_id, \*\*<a href="src/orb/types/subscription_trigger_phase_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/unschedule_cancellation">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">unschedule_cancellation</a>(subscription_id) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/unschedule_fixed_fee_quantity_updates">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">unschedule_fixed_fee_quantity_updates</a>(subscription_id, \*\*<a href="src/orb/types/subscription_unschedule_fixed_fee_quantity_updates_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/unschedule_pending_plan_changes">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">unschedule_pending_plan_changes</a>(subscription_id) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>
- <code title="post /subscriptions/{subscription_id}/update_fixed_fee_quantity">client.subscriptions.<a href="./src/orb/resources/subscriptions.py">update_fixed_fee_quantity</a>(subscription_id, \*\*<a href="src/orb/types/subscription_update_fixed_fee_quantity_params.py">params</a>) -> <a href="./src/orb/types/subscription.py">Subscription</a></code>

# Webhooks

Methods:

- <code>client.webhooks.<a href="./src/orb/resources/webhooks.py">unwrap</a>(\*args) -> object</code>
- <code>client.webhooks.<a href="./src/orb/resources/webhooks.py">verify_signature</a>(\*args) -> None</code>

# Alerts

Types:

```python
from orb.types import Alert
```

Methods:

- <code title="get /alerts/{alert_id}">client.alerts.<a href="./src/orb/resources/alerts.py">retrieve</a>(alert_id) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="put /alerts/{alert_configuration_id}">client.alerts.<a href="./src/orb/resources/alerts.py">update</a>(alert_configuration_id, \*\*<a href="src/orb/types/alert_update_params.py">params</a>) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="get /alerts">client.alerts.<a href="./src/orb/resources/alerts.py">list</a>(\*\*<a href="src/orb/types/alert_list_params.py">params</a>) -> <a href="./src/orb/types/alert.py">SyncPage[Alert]</a></code>
- <code title="post /alerts/customer_id/{customer_id}">client.alerts.<a href="./src/orb/resources/alerts.py">create_for_customer</a>(customer_id, \*\*<a href="src/orb/types/alert_create_for_customer_params.py">params</a>) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="post /alerts/external_customer_id/{external_customer_id}">client.alerts.<a href="./src/orb/resources/alerts.py">create_for_external_customer</a>(external_customer_id, \*\*<a href="src/orb/types/alert_create_for_external_customer_params.py">params</a>) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="post /alerts/subscription_id/{subscription_id}">client.alerts.<a href="./src/orb/resources/alerts.py">create_for_subscription</a>(subscription_id, \*\*<a href="src/orb/types/alert_create_for_subscription_params.py">params</a>) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="post /alerts/{alert_configuration_id}/disable">client.alerts.<a href="./src/orb/resources/alerts.py">disable</a>(alert_configuration_id) -> <a href="./src/orb/types/alert.py">Alert</a></code>
- <code title="post /alerts/{alert_configuration_id}/enable">client.alerts.<a href="./src/orb/resources/alerts.py">enable</a>(alert_configuration_id) -> <a href="./src/orb/types/alert.py">Alert</a></code>
