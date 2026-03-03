from api.user_api import get_user
from database.db_queries import get_user_name


def test_validate_user(base_url, db_connection, test_data):

    user_id = test_data["user_id"]

    # API Call
    response = get_user(base_url, user_id)
    api_data = response.json()
    #print(api_data)

    # DB Call
    db_name = get_user_name(db_connection, user_id)

    # Assertions
    assert response.status_code == 200
    assert api_data["name"] == db_name
