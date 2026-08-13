import secrets
import string
import math
import re

COMMON_PASSWORD = {
    "123456", "password", "12345678" , "qwerty", "abc123",
    "111111", "1234567890", "iloveyou", "admin", "welcome"
}

def generate_password(length = 12, use_upper = True, use_digits = True, use_symbols = True):

    if length < 4:
        raise ValueError("Password Must Be At Least 4 Characters!")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""
    alphabet = lower + upper + digits + symbols
    password_chars = [secrets.choice(lower)]

    if use_upper: password_chars.append(secrets.choice(upper))
    if use_digits: password_chars.append(secrets.choice(digits))
    if use_symbols: password_chars.append(secrets.choice(symbols))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def estimate_entropy(password):

    pool = 0

    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]", password): pool += 32
    if pool == 0: return 0

    return len(password) * math.log2(pool)


def password_score(password):

    feedback = []
    score = 0

    if password.lower() in COMMON_PASSWORD:
        feedback.append("Extremely Common Password!")
        return 0 ,feedback

    entropy = estimate_entropy(password)
    base = min(max((entropy - 10) * 1.4, 0), 70)
    score += base

    if len(password) >= 12: score += 10
    elif len(password) >= 8: score +=5
    else: feedback.append("Too Short - Use At Least 8 Characters!")

    classes = sum(bool(re.search(p, password)) for p in [r"[a-z]", r"[A-Z]", r"[0-9]", r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]"])
    score += {1: 0, 2: 5, 3: 10, 4: 15}.get(classes, 0)

    if re.search(r"(.)\1\1", password):
        score -= 10
        feedback.append("Avoid Repeating Characters!")

    if re.search(r"123|234|345|456|567|678|789|890", password):
        score -= 8
        feedback.append("Avoid Sequential Characters!")

    final = int(max(0, min(score, 100)))
    feedback.insert(0, "Strong Password!" if final >= 60 else "Weak/Moderate Password!")
    feedback.append(f"Entropy: {entropy:.1f} bits. Score: {final}/100.")

    return final, feedback


def interactive_menu():

    while True:
        print("\n==== PG&SC Tool ====")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            length = int(input("Length (default 12): ") or 12)
            pwd = generate_password(length)
            print("\nGenerated Password: ",pwd)
            score, fb = password_score(pwd)
            print("\nAssessment: ")

            for line in fb: print("-", line)

        elif choice == "2":
            pwd = input("Enter Password: ")
            score, fb = password_score(pwd)
            print("\nAssessment: ")

            for line in fb: print("-", line)

        elif choice == "3":
            print("Bye! Stay Secure")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    interactive_menu()