def is_valid_id(user_id):
    try:
        int(user_id)
        return True
    except ValueError:
        return False
