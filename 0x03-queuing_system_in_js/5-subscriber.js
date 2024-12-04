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

client.subscribe('holberton school channel', (msg) => {
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  } else console.log(msg);
});
