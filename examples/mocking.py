import requests
from unittest.mock import patch, MagicMock
import pytest

# Functions
def get_users():
		response = requests.get("https://jsonplaceholder.typicode.com/users")
		if response.status_code == 200:
				return response.json()
		raise requests.HTTPError
	
# Tests

@patch("requests.get")  # Mock the requests.get method
def test_get_users(mock_get):
    # Create a mock response object
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_response.status_code = 200

    # Configure mock_get to return the mock_response
    mock_get.return_value = mock_response

    # Call the function under test
    data = get_users()

    # Verify the output
    assert data == {"id": 1, "name": "John Doe"}

def test_get_users_error():
    with patch("requests.get") as mock_get: # another way to mock a method
        mock_response = MagicMock()
        mock_response.json.status_code = 400
        mock_get.return_value = mock_response
        with pytest.raises(requests.HTTPError):
            get_users()