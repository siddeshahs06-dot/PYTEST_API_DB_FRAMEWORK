def get_user_name(connection, user_id):

    cursor = connection.cursor()
    query = "SELECT name FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))

    result = cursor.fetchone()
    return result[0] if result else None
