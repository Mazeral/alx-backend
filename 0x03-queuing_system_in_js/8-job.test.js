import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    sinon.stub(queue, 'create').returns({
      save: sinon.stub().yields(null),
      on: sinon.stub(),
    });
  });

  afterEach(() => {
    sinon.restore();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create jobs in the queue for each job in the array', () => {
    const jobs = [
      { phoneNumber: '123-456-7890', message: 'Job 1' },
      { phoneNumber: '987-654-3210', message: 'Job 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.create.callCount).to.equal(jobs.length);

    jobs.forEach((job, index) => {
      expect(queue.create.getCall(index).args[0]).to.equal('job');
      expect(queue.create.getCall(index).args[1]).to.deep.equal(job);
    });
  });

  it('should log job completion percentage for each job', () => {
    const jobs = [
      { phoneNumber: '123-456-7890', message: 'Job 1' },
      { phoneNumber: '987-654-3210', message: 'Job 2' },
    ];

    const consoleLogStub = sinon.stub(console, 'log');

    createPushNotificationsJobs(jobs, queue);

    const job = queue.create.returnValues[0];
    const jobCompleteCallback = job.on.getCall(0).args[1];
    jobCompleteCallback();

    expect(consoleLogStub.calledWith('Notification job 1 completed')).to.be.true;
    expect(consoleLogStub.calledWith('Notification job 1 50% complete')).to.be
      .true;

    consoleLogStub.restore();
  });
});
