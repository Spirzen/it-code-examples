// utils.js
export function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export const MAX_ATTEMPTS = 3;

// main.js

import { validateEmail, MAX_ATTEMPTS } from './utils.js';

if (validateEmail('user@example.com')) {
    console.log(`Attempts allowed: ${MAX_ATTEMPTS}`);
}
