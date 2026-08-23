from langchain_core.tools import tool
from database import get_order


@tool
def track_order(order_id: str) -> str:
    """Get the status and estimated delivery date of an order."""

    order_id = order_id.strip().upper()

    order = get_order(order_id)

    if order is None:
        return f"Order {order_id} was not found."

    order_id, customer_name, product, status, eta = order

    return f"""
Order ID: {order_id}
Customer: {customer_name}
Product: {product}
Status: {status}
Estimated Delivery: {eta}
"""