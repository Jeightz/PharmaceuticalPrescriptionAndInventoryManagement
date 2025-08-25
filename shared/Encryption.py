import bcrypt


class PasswordHashed:
    
    def _hash_password(self, password: str) -> str:
        if not password:
            raise ValueError("Password is required")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            self.hashed_password.encode('utf-8')
    )