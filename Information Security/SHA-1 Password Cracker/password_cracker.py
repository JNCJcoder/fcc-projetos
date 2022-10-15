import hashlib

def read_file(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(line.strip())
    return data

passwords = read_file('top-10000-passwords.txt')
salts = read_file('known-salts.txt')

def crack_sha1_hash(hash, use_salts=False):
    for password in passwords:
        if use_salts:
            for salt in salts:
                salted_passwords = [
                    salt + password,
                    salt + password + salt,
                    password + salt
                ]

                for salted_password in salted_passwords:
                    result = hashlib.sha1(salted_password.encode()).hexdigest()
                    if result == hash:
                        return password
        else:
            result = hashlib.sha1(password.encode()).hexdigest()
            if result == hash:
                return password

    return 'PASSWORD NOT IN DATABASE'