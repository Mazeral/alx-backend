import { createClient } from 'redis';

const localhost = '127.0.0.1';
const client = createClient({
  host: localhost,
  port: 6379,
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

async function publishMessage(message, time) {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  await delay(time);
  console.log(`About to send ${message}`);
  client.publish('holberton school channel', message);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
