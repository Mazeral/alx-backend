import kue from 'kue';

const phoneNumber = {
  phoneNumber: '12345',
  message: 'Test',
};

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('phoneNumber1', phoneNumber).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else if (err) {
    console.log('Notification job failed');
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// process the jobs in the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
