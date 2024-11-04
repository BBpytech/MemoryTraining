import random
import time
import os


def generate_random_number(digits):
    """გენერირებს შემთხვევით რიცხვს მოცემული რაოდენობის ციფრებით"""
    return random.randint(10 ** (digits - 1), 10 ** digits - 1)


def memory_training():
    digits = 2  # იწყება 2-ნიშნა რიცხვით
    while True:
        random_number = generate_random_number(digits)
        print(f"Remember this number: {random_number}")

        # აჩვენებს რიცხვს 1 წამის განმავლობაში
        time.sleep(6)

        # ეკრანის გასუფთავება
        os.system('cls' if os.name == 'nt' else 'clear')

        # ან ამატებს რამდენიმე ცარიელ ხაზს, რომ რიცხვი აღარ ჩანდეს
        print("\n" * 10)

        # ეკრანზე გამოდის პრომპტი რიცხვის შესაყვანად
        user_input = input(f"Enter the {digits}-digit number: ")

        if user_input == str(random_number):
            print("Correct!")
            digits += 1  # თუ სწორია, გადავდივართ შემდეგ, მეტი ციფრით
        else:
            print(f"Incorrect. The correct number was: {random_number}")
            # არ ვზრდით ციფრების რაოდენობას, იგივე ვარჯიშს ვიმეორებთ
        print()


memory_training()