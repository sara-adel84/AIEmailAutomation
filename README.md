# AI Email Automation

## Project Overview

This project automates customer email processing for a clothing store using Python and OpenAI.

It extracts important information from customer emails, checks order details, and suggests the appropriate action automatically.

## Features

- Extracts customer names, order numbers, and request types using OpenAI.
- Uses structured JSON output for consistent data extraction.
- Validates AI-extracted information.
- Classifies emails into five categories: Return, Complaint, New Order, Order Inquiry, and Other.
- Checks order details, payment status, and return eligibility.
- Determines appropriate actions based on business rules.
- Prevents duplicate email processing using email IDs.
- Reads and saves email data using CSV files.
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

### 1. Clone the repository

```bash
git clone https://github.com/sara-adel84/AIEmailAutomation.git
cd AIEmailAutomation
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `api_key.env` in the project root and add:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

### 5. Run the application

```bash
python main.py
```

## Example Output

The application processes customer emails and generates structured results.

| Email ID | Customer | Request Type | Order Check | Action |
|---|---|---|---|---|
| 1 | Sara | Return | Order verified | Start return review |
| 2 | Mona | Complaint | Payment not completed | Contact customer about payment |
| 4 | Sara | Order inquiry | Order verified | Check order delivery status |
| 7 | Daniel | Complaint | Order verified | Forward complaint to support |

The processed results are saved automatically in `processed_emails.csv`.