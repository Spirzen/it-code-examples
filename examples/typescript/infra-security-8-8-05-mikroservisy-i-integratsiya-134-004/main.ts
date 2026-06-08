import https from 'node:https';
import fs from 'node:fs';
import axios from 'axios';

const agent = new https.Agent({
  cert: fs.readFileSync('/secrets/client.crt'),
  key: fs.readFileSync('/secrets/client.key'),
  ca: fs.readFileSync('/secrets/partners-ca.pem'),
});

const client = axios.create({
  baseURL: 'https://api.payments.example',
  httpsAgent: agent,
});
