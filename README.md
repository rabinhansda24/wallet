
# Wallet App

A simple wallet and transaction application.

## Getting Started

### Prerequisites

Before running the app, make sure to install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. **Environment Variables:** Set up the necessary environment variables:
    - Create a `.env` file in the root directory of the project.
    - Add the required variables as shown below:

```plaintext
JWT_SECRET_KEY='ScuqXHWTSBlzE6Zlp3jE2iExBqrRSTm8KbWw+IbA/oc='
FLASK_ENV='development'
JWT_ACCESS_TOKEN_EXPIRES=5
MINIMUM_BALANCE=20
```

### Running the App

Run the application using the following command:

```bash
flask --app run run
```

## Docker Deployment

### Building the Docker Image

Build the Docker image with the following command:

```bash
docker build -t wallet-app .
```

### Running the Docker Container

Start the Docker container:

```bash
docker run -p 5000:5000 wallet-app
```

## How It Works

- **Registration:** Users must first register in the system.
- **Wallet Creation:** After registration, a wallet is created for the user. Each user can have only one wallet of each type.
- **Transactions:** Users can perform credit or debit transactions, view balances, and see total transactions over a specified period.
- **Thought process behind the Queue:** If we have multiple process trying to write to a wallet transaction, we might have race condition, we might have inaccurate wallet balance. If we have a queue to process the transaction then we can write to transaction table as the request were made. So whenever a transaction request comes credit/debit it is pushed to a queue. `add_transaction_to_queue` function takes a function and other parameters, here `create_transaction` function is being passed. The queue is alawys looking if there is any item present, this is initialized with a background thread started when the app is created and started.

## API Endpoints

- **Register User**
  - **Endpoint:** `/api/v1/users`
  - **Method:** POST
  - **Payload:** `{"phone_number": "9886977544"}`

- **Create Wallet**
  - **Endpoint:** `/api/v1/wallet/create`
  - **Method:** POST
  - **Payload:** `{"user_id": 1, "type": "type1"}`

- **Get Wallet Balance**
  - **Endpoint:** `/api/v1/wallet/get/<user_id>/<type>`
  - **Method:** GET
  - **Example:** `/api/v1/wallet/get/1/type1`

- **Create Transaction**
  - **Endpoint:** `/api/v1/transactions/create`
  - **Method:** POST
  - **Payload:** `{"user_id": 1, "wallet_id": 1, "amount": 20, "is_credit": true}`

- **Get All Transactions for a Wallet**
  - **Endpoint:** `/api/v1/transactions/get/<user_id>/<wallet_id>`
  - **Method:** GET
  - **Example:** `/api/v1/transactions/get/1/1`

- **Get Total Amount Transaction in a Period**
  - **Endpoint:** `/api/v1/transactions/get/total_in_period`
  - **Method:** POST
  - **Payload:** `{"user_id": 1, "wallet_id": 1, "start_date": "2024-04-19T05:27:13", "end_date": "2024-04-19T05:40:00"}`
