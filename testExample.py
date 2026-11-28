from unittest.mock import Mock
import pytest
# Code being tested

def get_user_email(user_id, api_client):
    user = api_client.get_user(user_id)
    if user is None:
        raise ValueError(f"User {user_id} not found")
    return user["email"]

# Tests

def test_get_user_email_returns_email():    # Arrange: create a mock dependency with a pretend response         
    api_client = Mock()    
    api_client.get_user.return_value = {"id": 42,"email": "ava@example.com",}
    # Act    
    result = get_user_email(42, api_client)
    # Assert: check the result and how the dependency was called    
    assert result == "ava@example.com"    
    api_client.get_user.assert_called_once_with(42)

def test_get_user_email_raises_if_user_is_missing():    
    api_client = Mock()    
    api_client.get_user.return_value = None
    with pytest.raises(ValueError, match="User 42 not found"):        
        get_user_email(42, api_client)
    api_client.get_user.assert_called_once_with(42)

def test_get_user_email_propagates_api_error():    
    api_client = Mock()    
    api_client.get_user.side_effect = TimeoutError("API timed out")
    with pytest.raises(TimeoutError, match="API timed out"):       
        get_user_email(42, api_client)
    api_client.get_user.assert_called_once_with(42)
