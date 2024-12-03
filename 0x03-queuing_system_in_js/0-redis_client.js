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
