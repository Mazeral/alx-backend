import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const blackList = [
  '4153518780',
  '4153518781',
];

const push_notification_code_2 = kue.createQueue();

jobs.forEach((element) => {
  const job = push_notification_code_2.create('job', element).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
    if (err) {
      console.log(`Notification job ${job.id} failed: ${err}`);
    }
  });
  job.on('complete', () => {
    console.log('Notification job completed');
  });

  job.on('failed', () => {
    console.log('Notification job failed');
  });
  console.log(`Notification job ${job.id} ${(jobs.indexOf(element) + 1) / jobs.length}% complete`);
});

function sendNotification(phoneNumber, message, job, done) {
  console.log(`Notification job ${job.id} 0% complete`);
  if (blackList.find(phoneNumber)) {
    throw new Error(`Phone number ${phoneNumber} is blacklisted`);
  }

  console.log(`Notification job ${job.id} 50% complete`);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  const queue = kue.createQueue();
  queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
  });
  done();
}
