# Queuing System in JS

This project demonstrates how to manage and process jobs using Kue and Redis in Node.js. It includes job creation, processing, tracking, and interacting with Redis for product stock management.

## Project Structure

- **7-job_creator.js**: Script to create notification jobs and track their progress.
- **7-job_processor.js**: Processes the notification jobs, checks if a phone number is blacklisted, and tracks job progress.
- **8-job.js**: Contains the function `createPushNotificationsJobs` to enqueue jobs and log their statuses.
- **8-job.test.js**: Mocha tests for the `createPushNotificationsJobs` function, including validation of job creation.
- **9-stock.js**: Manages product stock using Redis and Express. It includes routes for listing products and reserving stock.
- **Redis**: Used to store and manage reserved stock for products.

## Requirements

- Node.js
- Redis
- Kue
- Mocha for testing

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/alx-backend.git
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start Redis server:

    Ensure that Redis is running locally or configure it to connect to a remote Redis instance.

4. Run the Job Creator:

    ```bash
    npm run dev 7-job_creator.js
    ```

5. Run the Job Processor:

    In a new terminal, run the job processor:

    ```bash
    npm run dev 7-job_processor.js
    ```

6. To interact with the product stock server:

    ```bash
    npm run dev 9-stock.js
    ```

    This will start the Express server on port 1245.

## Routes

- **GET /list_products**: Lists all products with their initial stock.
- **GET /list_products/:itemId**: Fetches product details and current stock.
- **GET /reserve_product/:itemId**: Reserves a product if stock is available.

## Testing

To run the tests for the job creation:

```bash
npm test 8-job.test.js
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
