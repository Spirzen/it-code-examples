import crypto from "node:crypto";

const pseudo = Math.random();               // PRNG движка
const secure = crypto.randomBytes(16);      // CSPRNG

console.log(pseudo, secure.toString("hex"));
