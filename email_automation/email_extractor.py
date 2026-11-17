import json
import time
from openai import APIConnectionError, APITimeoutError, RateLimitError
from .config import client

def extract_email_info(email_text):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions="""
        Act as a senior customer support manager for a clothing store.

        Your task is to extract information from customer emails.

        Return a JSON object with exactly these keys:
        - customer_name
        - order_number
        - request_type

        The request_type must be one of these five values:

        1. Return:
            The customer wants to return an item because they
            changed their mind or no longer want it.

        2. Complaint:
            The customer reports a damaged, defective, missing,
            or incorrect item.

        3. New order:
            The customer wants to purchase a new item.

        4. Order inquiry:
            The customer asks about the status, delivery date,
            or arrival time of an existing order.

        5. Other:
            General questions about products, delivery policies,
            payment policies, or the store.

        Classification rules:
        - A damaged, defective, missing, or incorrect item
            must always be classified as Complaint.
        - If the customer asks about an existing order's
            delivery status or arrival date, classify it as Order inquiry.
        - If the customer wants to buy a new item, classify it
            as New order.
        - Do not classify general delivery policy questions
            as Order inquiry. Use Other instead.
        - If the customer asks about a payment, payment reminder,
            invoice, or payment confirmation, classify it as Other.
            
        Extraction rules:
        - Extract the customer's name if available.
        - Extract the order number if available.
        - If the customer name or order number is missing,
             return null.
        - Never guess or invent information.
        - Return only the requested JSON object.
""",
        input=email_text,
        text={
        "format": {
            "type": "json_schema",
            "name": "customer_email",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "customer_name": {
                        "type": ["string", "null"]
                    },
                    "order_number": {
                        "type": ["string", "null"]
                    },
                    "request_type": {
                        "type": "string",
                        "enum": [
                            "Return",
                            "Complaint",
                            "New order",
                            "Order inquiry",
                            "Other"
                        ]
                    }
                },
                "required": [
                    "customer_name",
                    "order_number",
                    "request_type"
                ],
                "additionalProperties": False
            }
        }
    }
)

    try:
        result = json.loads(response.output_text)
        return result

    except json.JSONDecodeError:
        print("Invalid JSON response from AI")
        return None

def validate_email_info(email_info):
    if not isinstance(email_info, dict):
        return False

    required_keys = [
        "customer_name",
        "order_number",
        "request_type"
    ]

    for key in required_keys:
        if key not in email_info:
            return False

    allowed_types = [
        "Return",
        "Complaint",
        "New order",
        "Order inquiry",
        "Other"
    ]

    if email_info["request_type"] not in allowed_types:
        return False

    if (
        (email_info["customer_name"] is not None and not isinstance(email_info["customer_name"], str))
        or
        (email_info["order_number"] is not None and not isinstance(email_info["order_number"], str))
    ):
        return False

    return True

def extract_with_retry(email_text):
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            result = extract_email_info(email_text)
            return result

        except (APIConnectionError, RateLimitError, APITimeoutError) as error:
            attempts += 1

            print(f"Attempt {attempts} failed: {error}")

            if attempts < max_attempts:
                time.sleep(2)

    return None