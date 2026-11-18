# AI Email Automation

## Project Overview

This project automates customer email processing for a clothing store using Python and OpenAI.

It extracts important information from customer emails, checks order details, and suggests the appropriate action automatically.

## Features

- Extracts customer names, order numbers, and request types using AI.
- Validates extracted information.
- Checks order details and payment status.
- Identifies return requests and complaints.
- Prevents duplicate actions for the same order.
- Saves processed emails and results in CSV files.
- Handles API errors with retry logic.

## Technologies Used

- Python 3.12
- OpenAI API
- CSV
- JSON
- python-dotenv
- Exception Handling

## Project Structure
```text
AIEmailAutomation/
├── email_automation/
│   ├── __init__.py
│   ├── config.py
│   ├── csv_manager.py
│   ├── email_extractor.py
│   └── order_manager.py
├── customer_emails.csv
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```


## How to Run

1. Clone the repository.
2. Create a virtual environment.
3. Install the required libraries:

   pip install openai python-dotenv

4. Create an `api_key.env` file in the project root.
5. Add your OpenAI API key to the environment file.
6. Run the application:

   python main.py