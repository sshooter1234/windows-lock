import hashlib

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password

def verify_password(password, hashed_password):
    hashed_input = hash_password(password)
    if hashed_input == hashed_password:
        return True
    else:
        return False
                            #put your sha256 hash below in the ""
stored_hashed_password = ""

while True:
    password = input("logon: ")
    if verify_password(password, stored_hashed_password):
        print("Valid logon")
        break
    else:
        print("Logon invailed")

print("logon")

#run in cmd and put in full screen