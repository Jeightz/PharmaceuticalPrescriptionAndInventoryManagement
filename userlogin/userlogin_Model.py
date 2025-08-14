def checkDataInputed(username, password):
    if not username  or not password or username.strip() == "" or password.strip() == "" or username == "username" or password == "password":
        return False
    return True