import bcrypt

def hashear_password(password: str) -> str:
    password_bites = password.encode('utf-8')
    hash_password = bcrypt.hashpw(password_bites, bcrypt.gensalt())
    return hash_password.decode('utf-8')

def verificar_password(password: str, hashed_password: str) -> bool:
    password_bites = password.encode('utf-8')
    hashed_password_bites = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bites, hashed_password_bites)