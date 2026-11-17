import csv
from pathlib import Path

def read_emails():
    with open("customer_emails.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        emails = list(reader)

    return emails

def save_results(results):
    file_exists = Path("processed_emails.csv").exists()

    with open("processed_emails.csv", "a", newline="", encoding="utf-8") as file:
        fieldnames = [
            "email_id",
            "customer_name",
            "order_number",
            "request_type",
            "order_check",
            "action"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(results)

def get_processed_emails_ids():
    processed_ids = set()

    try:
        with open("processed_emails.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                processed_ids.add(row["email_id"])
             
    except FileNotFoundError:
        pass

    return processed_ids

# def get_processed_actions():
#     processed_actions = set()

#     try:
#         with open("processed_emails.csv", "r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)

#             for row in reader:
#                 order_number = row["order_number"]    
#                 action = row["action"]
                 
#                 if order_number and action and action != "Duplicate action - skipped":
#                     processed_actions.add((order_number, action))

#     except FileNotFoundError:
#         pass
    
#     return processed_actions