class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value) -> str or None:
        is_valid_length = len(value) >= 8
        has_digit = len([c for c in value if c.isdigit()]) > 0
        has_uppercase = len([c for c in value if c.isupper()]) > 0

        if not (is_valid_length and has_digit and has_uppercase):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return (f'You have a profile with username: '
                f'"{self.username}" and password: '
                f'{"*" * len(self.__password)}')


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
