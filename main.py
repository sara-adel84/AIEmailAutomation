from email_automation.email_extractor import (
    extract_with_retry,
    validate_email_info
)

from email_automation.order_manager import (
    check_order,
    get_action
)

from email_automation.csv_manager import (
    read_emails,
    save_results,
    get_processed_emails_ids
)

emails = read_emails()

results = []

processed_ids = get_processed_emails_ids()
# processed_actions = get_processed_actions()

for email in emails:
   
    email_id = str(email["email_id"]).strip() 
    if not email_id:
        print("Missing email ID - skipped")
        continue

    if email_id in processed_ids:
        print("Email already processed - skipped")
        continue

    email_text = email["email_text"].strip()

    if not email_text:
        print("Empty email skipped")
        continue

    email_info = extract_with_retry(email_text)

    if email_info is None:
        print("Email processing failed")
        continue

    if not validate_email_info(email_info):
        print("Invalid AI response - skipped")
        continue

    order_number = email_info["order_number"]
    request_type = email_info["request_type"]

    order_check = check_order(order_number, request_type)
    action = get_action(request_type, order_check)
    # action_key = (str(order_number).strip(), action)

    # if order_number and action_key in processed_actions:
    #     action = "Duplicate action - skipped"
    # elif order_number:
    #     processed_actions.add(action_key)


    result = {
        "email_id": email["email_id"],
        "customer_name": email_info["customer_name"],
        "order_number": order_number,
        "request_type": request_type,
        "order_check": order_check,
        "action": action
    }

    results.append(result)
    processed_ids.add(email_id)

save_results(results)

print("All emails processed and saved successfully!")