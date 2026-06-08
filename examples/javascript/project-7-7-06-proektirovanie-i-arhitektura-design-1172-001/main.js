
import { createRemoteJWKSet, compactVerify } from 'jose';

const JWKS = createRemoteJWKSet(
  new URL('https://api.payments.example/.well-known/webhook-jwks.json')
);

async function verifyWebhook(rawBody, timestamp, jwsCompact, maxSkewSec = 300) {
  if (Math.abs(Date.now() / 1000 - Number(timestamp)) > maxSkewSec) {
    throw new Error('timestamp skew');
  }
  const signingInput = new TextEncoder().encode(`${timestamp}.${rawBody}`);
  const { payload } = await compactVerify(jwsCompact, JWKS);
  const signed = new TextDecoder().decode(payload);
  if (signed !== new TextDecoder().decode(signingInput)) {
    throw new Error('payload mismatch');
  }
}
