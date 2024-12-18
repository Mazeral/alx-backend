import kue from 'kue';

const blackList = [
  '4153518780',
  '4153518781',
];

const push_notification_code_2 = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blackList.includes(phoneNumber)) {
	 return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process the jobs in the queue
push_notification_code_2.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Listen for job events
push_notification_code_2.on('job complete', (id) => {
  console.log(`Notification job #${id} completed`);
});

push_notification_code_2.on('job failed', (id, errorMessage) => {
  console.log(`Notification job #${id} failed: ${errorMessage}`);
});
