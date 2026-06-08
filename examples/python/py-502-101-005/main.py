class PaymentProcessor:
    def __init__(self, api_key):
        self._api_key = api_key
        self._session = self._create_session()
    
    def process_payment(self, amount, currency):
        payload = self._prepare_payload(amount, currency)
        response = self._send_request(payload)
        return self._parse_response(response)
    
    def _create_session(self):
        return requests.Session()
    
    def _prepare_payload(self, amount, currency):
        return {
            "amount": amount,
            "currency": currency,
            "timestamp": int(time.time()),
            "signature": self._generate_signature(amount, currency)
        }
    
    def _generate_signature(self, amount, currency):
        data = f"{amount}{currency}{self._api_key}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def _send_request(self, payload):
        return self._session.post("https://api.payment.com/charge", json=payload)
    
    def _parse_response(self, response):
        if response.status_code != 200:
            raise PaymentError(f"Payment failed: {response.text}")
        return response.json()
