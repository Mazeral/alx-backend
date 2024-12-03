import { createClient } from "redis"

const localhost = '127.0.0.1'
import { createClient } from 'redis'
const client = createClient({
	host: localhost,
	port: 6379,
})


client.on('connect', () => {
	console.log('Redis client connected to the server')
})

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`)
})

function setNewSchool(schoolName, value){
	client.set(schoolName, value, (err, reply) => {
		if (err) throw err;
		console.log('Set key response:', reply)
	})
}

function displaySchoolValue(schoolName){
	const value = client.get(schoolName, (err, reply) => {
		if (err) throw err;
		console.log('Set key response:', reply)
	})
	console.log(value)
}

