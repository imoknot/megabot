from .base import ExcludeNone, Location


class Invoice(ExcludeNone):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: str



class ShippingAddress(ExcludeNone):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(ExcludeNone):
    name: str | None = None
    phone_number: str | None = None
    email: str | None = None
    shipping_address: ShippingAddress | None = None


class SuccessfulPayment(ExcludeNone):
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str | None = None
    order_info: OrderInfo | None = None
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
