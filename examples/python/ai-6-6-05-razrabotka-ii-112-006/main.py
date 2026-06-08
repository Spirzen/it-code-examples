
import pytest

from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_model_adapter_success():
    mock_response = {
        "choices": [{"message": {"content": "Тестовый ответ"}}],
        "usage": {"total_tokens": 42},
        "model": "test-model"
    }
    
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_post.return_value = AsyncMock(
            status_code=200,
            json=lambda: mock_response,
            elapsed=type("obj", (), {"total_seconds": lambda: 0.123})()
        )
        
        adapter = OpenAICompatibleAdapter(
            base_url="http://test", 
            api_key="test", 
            model_name="test-model"
        )
        result = await adapter.generate("Тестовый промпт")
        
        assert result.text == "Тестовый ответ"
        assert result.tokens_used == 42
