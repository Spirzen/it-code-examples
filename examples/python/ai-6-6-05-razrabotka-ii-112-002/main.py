
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class SyncModelClient:
    def __init__(self, base_url: str, api_key: str):
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
        self.base_url = base_url

    def generate(self, prompt: str, timeout: float = 15.0) -> Dict[str, Any]:
        try:
            response = self.session.post(
                f"{self.base_url}/v1/chat/completions",
                json={
                    "model": "custom-model",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 256
                },
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Model inference exceeded {timeout}s")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Model API error: {e}")
