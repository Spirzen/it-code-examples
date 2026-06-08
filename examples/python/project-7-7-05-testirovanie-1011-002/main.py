from unittest.mock import Mock, patch
from app.user_service import get_user_data

@patch('app.user_service.DatabaseConnection')
def test_get_user_data_with_mock(mock_db_class):
    mock_instance = Mock()
    mock_instance.fetch_user.return_value = {"id": 1, "name": "Bob"}
    
    mock_db_class.return_value = mock_instance
    
    result = get_user_data(1)
    
    assert result == "Bob"
    mock_instance.fetch_user.assert_called_once_with(1)
