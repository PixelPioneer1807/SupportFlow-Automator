# SupportFlow Automator

SupportFlow Automator is an AI-powered tool designed to streamline customer support by automating ticket analysis, classification, and response generation. It integrates with Google Sheets and Gmail to create an efficient workflow for managing and resolving customer inquiries.

## Features

- **AI-Powered Ticket Classification:** Automatically categorizes incoming support tickets by sentiment (Positive, Negative, Neutral) and issue type (Billing, Technical, Login, General, Other).
- **Automated Reply Generation:** Leverages AI to craft empathetic and helpful responses to customer issues.
- **Google Sheets Integration:** Fetches new tickets from a Google Sheet and updates it with the AI-generated sentiment, issue type, and reply.
- **Automated Email Replies:** Sends the generated responses directly to customers via Gmail SMTP.
- **Web Interface:** Includes a Streamlit application for both submitting and managing support tickets.

## How It Works

1.  **Ticket Submission:** Customers can submit support tickets through a dedicated Streamlit form. New tickets are added as rows to a Google Sheet.
2.  **Ticket Fetching:** The AI Ticket Manager fetches new, unprocessed tickets from the Google Sheet.
3.  **AI Analysis:** For each new ticket, the system uses an AI model to:
    * Classify the ticket's sentiment and issue type.
    * Generate a relevant and contextual reply.
4.  **Sheet Update & Logging:** The original ticket in the Google Sheet is updated with the classification and reply. A record of the processed ticket is also saved to a separate "ProcessedTickets" sheet for logging purposes.
5.  **Email Notification:** An email containing the AI-generated reply is automatically sent to the customer.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- A Google Cloud Platform project with the Google Sheets API and Google Drive API enabled.
- A Gmail account with an App Password for sending emails.
- An API key from EURI.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pixelpioneer1807/supportflow-automator.git](https://github.com/pixelpioneer1807/supportflow-automator.git)
    cd supportflow-automator
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```
    EURI_API_KEY="your_euri_api_key"
    EMAIL_ADDRESS="your_gmail_address"
    EMAIL_APP_PASSWORD="your_gmail_app_password"
    ```

4.  **Configure Google Credentials:**
    Place your Google Cloud service account credentials file in the root directory and name it `google_creds.json`.

## Usage

### Submit a New Ticket

Run the ticket registration form:

```bash
streamlit run register_ticket.py
```
Process and Manage Tickets
Launch the AI Ticket Manager dashboard:
```
streamlit run main.py
```