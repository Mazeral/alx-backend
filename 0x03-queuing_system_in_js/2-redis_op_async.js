import { createClient } from 'redis';
import { promisify } from 'util';

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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) throw err;
    console.log('Set key response:', reply);
  });
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName, (err, reply) => {
    if (err) throw err;
    console.log('Set key response: ', reply);
  });
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
