import createClient from 'redis'
import promisify from 'util'
import kue from 'kue'
import express from 'express'

const localhost = '127.0.0.1';
const client = createClient({
  host: localhost,
  port: 6379,
});
const app = express()

client.set('available_seats', 10)
const reservationEnabled = true;

const setAsync = promisify(client.set).bind(client)
const getAsync = promisify(client.get).bind(client)


function reserveSeat(number){
	client.set('available_seats', number)	
}

async function getCurrentAvailableSeats(){
	const availableSeats = await getAsync('available_seats')
	return availableSeats > 0 ? availableSeats : 0;
}

const queue = kue.createQueue()

app.get('/available_seats', (req, res) => {
	const seats = getCurrentAvailableSeats()
	res.json({"numberOfAvailableSeats": seats})
})

app.get('/reserve_seat', (req, res) => {
	if (reservationEnabled === false){
		res.json({ "status": "Reservation are blocked" })
	}
	const job = queue.create('reserve_seat').save((err) => {
		if (!err){
			res.json({ "status": "Reservation in process" })
		}
		else if (err){
			res.json({ "status": "Reservation failed" })
		}
	})

	job.on('complete', ()=>{
		console.log(`Seat reservation job ${job.id} completed`)
	})
	job.on('failed', ()=>{
		console.log(`Seat reservation job ${job.id} failed: ${err.message}`)
	})

})

app.get('/process', async (req, res) => {
	const seats = parseInt(await getCurrentAvailableSeats(), 10)
	try {
		const newSeats = seats - 1;
		if (newSeats < 0){
			throw Error("Not enough seats available")
		}
		if (newSeats === 0) reservationEnabled = false;
		res.json({ "status": "Queue processing" })
		
	} catch (error) {
		res.json({"status":"Reservation are blocked"})	
	}
})

app.listen(1245);
