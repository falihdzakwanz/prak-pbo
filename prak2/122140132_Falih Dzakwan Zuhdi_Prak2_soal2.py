import random

class Game:

    def __init__(self):
        self.__number = random.randint(1, 100)
        self.__tries = 0
        print("Selamat datang di game tebak angka!")
        print("Saya telah memilih sebuah angka antara 1 dan 100.")
        print("Anda memiliki 10 kesempatan untuk menebaknya.")

    def __del__(self):
        print("Terima kasih telah bermain game tebak angka!")

    def limit_tries(func):
        def wrapper(self, *args):
            if self.__tries < 10:
                return func(self, *args)
            else:
                print("Anda telah kehabisan kesempatan. Anda kalah.")
                print(f"Angka yang saya pilih adalah {self.__number}.")
        return wrapper

    def start(self):
        while True:
            guess = input("Masukkan tebakan Anda: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue
            if guess < 1 or guess > 100:
                print("Input tidak valid. Masukkan angka antara 1 dan 100.")
                continue
            
            self.check(guess)
            if self.__tries == 10 or guess == self.__number:
                break

    @limit_tries
    def check(self, guess):
        self.__tries += 1
        if guess == self.__number:
            print(f"Selamat! Anda menebak dengan benar dalam {self.__tries} kali.")
            print("Anda menang!")
        elif guess < self.__number:
            print("Tebakan Anda terlalu kecil.")
            print(f"Anda masih memiliki {10 - self.__tries} kesempatan.")
        else:
            print("Tebakan Anda terlalu besar.")
            print(f"Anda masih memiliki {10 - self.__tries} kesempatan.")

game = Game()

game.start()

del game
