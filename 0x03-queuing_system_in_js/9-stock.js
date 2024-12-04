import express from 'express';
import { createClient } from 'redis';
import promisify from 'util';

const localhost = '127.0.0.1';
const client = createClient({
  host: localhost,
  port: 6379,
});

const app = express();
const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

app.get('/list_products', (req, res) => {
	 const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  // Get current reserved stock from Redis
  const reservedStock = getCurrentReservedStockById(itemId);

  // Calculate the current quantity
  const currentQuantity = product.stock - reservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = reserveStockById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  if (product) {
    if (parseInt(product.stock, 10) <= 0) {
      return res.json({ status: 'Not enough stock available', itemId: product.id });
    }

    res.json({ status: 'Reservation confirmed', itemId: product.id });
  }
});

app.listen(1245);
