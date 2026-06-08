const crypto = require("crypto");
const express = require("express");

const app = express();
const SECRET = process.env.WEBHOOK_SECRET;

app.post("/webhook/github", express.raw({ type: "application/json" }), (req, res) => {
  const signature = req.headers["x-hub-signature-256"];
  const expected = "sha256=" + crypto
    .createHmac("sha256", SECRET)
    .update(req.body)
    .digest("hex");

  if (signature !== expected) {
    return res.status(401).send("Invalid signature");
  }

  const event = JSON.parse(req.body.toString());
  const eventId = req.headers["x-github-delivery"];

  // Идемпотентность: если eventId уже обработан — вернуть 200 без действий
  if (alreadyProcessed(eventId)) {
    return res.status(200).send("Already handled");
  }

  if (event.action === "opened" && req.headers["x-github-event"] === "pull_request") {
    queueCiJob(event.pull_request.number);
  }

  markProcessed(eventId);
  res.status(200).send("OK");
});
