import kue from 'kue';

const push_notification_code = kue.createQueue();

// Function to send the notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the push_notification_code queue
push_notification_code.process('push_notification', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done(); // Mark the job as completed
});

// Listen for job completion and failure
push_notification_code.on('job complete', (id, result) => {
  console.log(`Job ${id} completed: ${result}`);
});

push_notification_code.on('job failed', (id, errorMessage) => {
  console.log(`Job ${id} failed: ${errorMessage}`);
});