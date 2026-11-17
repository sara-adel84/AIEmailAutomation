orders = {
    "1052": {
        "customer_name": "Sara",
        "payment_status": "paid",
        "product": "jacket",
        "return_allowed": True
    },
    "1053": {
        "customer_name": "Mona",
        "payment_status": "unpaid",
        "product": "dress",
        "return_allowed": True
    },
    "1054": {
        "customer_name": "Omar",
        "payment_status": "paid",
        "product": "sneakers",
        "return_allowed": True
    },
    "1055": {
        "customer_name": "Lina",
        "payment_status": "paid",
        "product": "coat",
        "return_allowed": False
    },
    "1056": {
        "customer_name": "Adam",
        "payment_status": "paid",
        "product": "dress",
        "return_allowed": True
    }
}

def check_order(order_number, request_type):
    order_number = str(order_number).strip()
    order = orders.get(order_number)

    if order is None:
        return "Order not found"

    if order["payment_status"] != "paid":
        return "Payment not completed"

    if request_type == "Return" and not order["return_allowed"]:
        return "Return not allowed"

    return "Order verified"

def get_action(request_type, order_check):
    if request_type == "New order":
        return "Forward new order request"

    if request_type == "Order inquiry":
        if order_check == "Order verified":
            return "Check order delivery status"
        return "Ask customer to verify order number"

    if request_type == "Other":
        if order_check == "Payment not completed":
            return "Contact customer about payment"
        return "Forward general inquiry to customer support"

    if order_check == "Order not found":
        return "Ask customer to verify order number"

    if order_check == "Payment not completed":
        return "Contact customer about payment"

    if request_type == "Return":
        if order_check == "Order verified":
            return "Start return review"

    if request_type == "Complaint":
        if order_check == "Order verified":
            return "Forward complaint to support"

    return "Manual review"