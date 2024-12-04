import { createClient, redis } from 'redis';

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

client.hset('HolbertonSchools', 'Portland', '50', (err, count) => {
  console.log('Reply: 1');
});
client.hset('HolbertonSchools', 'Seattle', '80', (err, count) => {
  console.log('Reply: 1');
});
client.hset('HolbertonSchools', 'New York', '20', (err, count) => {
  console.log('Reply: 1');
});
client.hset('HolbertonSchools', 'Bogota', '20', (err, count) => {
  console.log('Reply: 1');
});
client.hset('HolbertonSchools', 'Cali', '40', (err, count) => {
  console.log('Reply: 1');
});
client.hset('HolbertonSchools', 'Paris', '2', (err, count) => {
  console.log('Reply: 1');
});

// Get all the fields and values in the hash
client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.error(err);
  } else {
    console.log(obj);
  }
});
