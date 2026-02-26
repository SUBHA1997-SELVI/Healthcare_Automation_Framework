from utils.db_utils import DatabaseUtils


def test_validate_user_in_database():

    query = "SELECT username FROM users WHERE username='tomsmith';"
    result = DatabaseUtils.execute_query(query)

    assert len(result) > 0
    assert result[0][0] == "tomsmith"