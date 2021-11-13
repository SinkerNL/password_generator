import sys

class PasswordGenerator:
    def __init__(self):
        self.PASSWORD_LENGTH = 5
        self.RETRIES_ASK_FOR_INPUT = 4

    def ask_user_for_input(self) -> tuple():
        """
        Ask the user certain questions needed to create the password.
        """
        answer = str(input(f"Do you want a standard password? (Y) or adjustable password (N)?\n")).lower()
        if answer == "y":
            return (self.PASSWORD_LENGTH)
        elif answer == "n":
            pass
        else:
            print("You didn't provide a valid answer, please try again.")
            self.RETRIES_ASK_FOR_INPUT -= 1
            if self.RETRIES_ASK_FOR_INPUT == 0:
                print("You tried too many times, program is quitting.")
                sys.exit()
            self.ask_user_for_input()
        return (answer)

    def main(self):
        print("Started Password Generator")
        self.ask_user_for_input()


if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.main()
