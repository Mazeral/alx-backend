import kue from 'kue';

const push_notification_code_3 = kue.createQueue();
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((element) => {
    const job = push_notification_code_3.create('job', element).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      } else if (err) {
        console.log(`Notification job ${job.id} failed ${err}`);
      }
    });
		  job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
		  console.log(`Notification job ${job.id} ${(jobs.indexOf(element) + 1) / jobs.length}% complete`);
		  });
  });
}
