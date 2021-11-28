import string
import random

class PasswordGenerator:
    def __init__(self):
        self.password_standard_length = int(12)
    
    def create_password(self):
        """
            Sequence of password questions to create password
        """
        ask_password_success = self.ask_for_password_length()
        if ask_password_success == True:
            self.generate_random_password()

    def ask_for_password_length(self):
        """
            Ask for how many characters the password should have
        """
        try:
            print("How many characters should the password be? (type 'exit' to close the program)")
            self.password_length = input("Number of characters: ")
            if self.password_length == "exit":
                self.stop_program()
                return False
            else:
                self.password_length = int(self.password_length)
                return True
        except:
            print("You did not provide an integer, please give an integer")
            self.ask_for_password_length()

    def generate_random_password(self):
        """
            Create password based on the given values
        """
        try:
            self.password = [None for i in range(self.password_length)]
        except:
            print(f"You did not provide a length of password, standard value of {self.password_standard_length} will be used.")
            self.password = [None for i in range(self.password_standard_length)]

        self.password = self.fill_array_with_random_letters(self.password)
        self.password = self.generate_string_from_array(self.password)

        print(self.password)

    def fill_array_with_random_letters(self, empty_array):
        """
            Function that will fill an empty array with random letters
        """
        for i in range(len(empty_array)):
            empty_array[i] = string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)]
        return empty_array
    
    def generate_string_from_array(self, filled_array):
        """
            Function that will generate a string from an array
        """
        full_string = ""
        for i in range(len(filled_array)):
            full_string += filled_array[i]
        return full_string

    def stop_program(self):
        print("Ok, we close the program.")
        return False


if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.create_password()