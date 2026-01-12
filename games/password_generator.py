import random
def play():
    # choose password length
    n = int(input("Enter the length of password you want: "))
    
    # define characters
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    specials = "^!@$%&*"
    
    # pick at least one from each
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specials)
    ]
    
    # fill the rest with random picks from all characters
    all_chars = uppercase + lowercase + digits + specials
    for i in range(n - 4):
        password.append(random.choice(all_chars))
    
    # shuffle so it’s not predictable
    random.shuffle(password)
    
    # join into string
    password = "".join(password)
    
    print("Generated password:", password)
if __name__ == "__main__":
    play()
