// logger/logger.js
export function info(msg) {
  const ts = new Date().toISOString();
  console.log(`[INFO] ${ts} ${msg}`);
}

// notification/email.js

import { info } from '../logger/logger.js'; // ← относительный путь ОБЯЗАТЕЛЕН

export function sendEmail(to, subject, body) {
  info(`Sending email to ${to}`);
  // ... nodemailer или fetch
}

// core/order.js

import { info } from '../logger/logger.js';

export class Order {
  constructor(id, items) {
    this.id = id;
    this.items = items;
  }
}

export class OrderService {
  placeOrder(items) {
    const order = new Order(1, items);
    info(`Order ${order.id} placed with ${items.length} items`);
    return order;
  }
}

// app/main.js

import { OrderService } from '../core/order.js';
import { sendEmail } from '../notification/email.js';

const service = new OrderService();
const order = service.placeOrder(['book', 'pen']);
sendEmail('user@example.com', 'Order confirmed', `ID: ${order.id}`);
