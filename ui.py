from typing import Any, Callable, List


class UI:
    """Luth Andyka's personal "Safe" input class :D"""

    def __init__(self):
        # print("Initializing UI...\n")
        pass

    def input_int(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> int:
        x = input(prompt)
        while not x.isnumeric():
            print(error_message)
            x = input(prompt)
        return int(x)

    def input_str(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> str:
        x = input(prompt)
        while not isinstance(x, str):
            print(error_message)
            x = input(prompt)
        return str(x)

    def input_char(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> str:
        x = input(prompt)
        while len(x) != 1:
            print(error_message)
            x = input(prompt)
        return str(x)

    def input_lambda(
        self,
        validator: Callable[[Any], bool],
        dtype: type,
        prompt: str = "",
        error_message: str = "An error occured",
    ) -> Any:
        x = input(prompt)
        try:
            x = dtype(x)
        except Exception:
            print(f"Input is not of datatype {dtype}")
            x = self.input_lambda(validator, dtype, prompt, error_message)

        if not validator(x):
            print("Your input is not valid.")
            x = self.input_lambda(validator, dtype, prompt, error_message)

        return x

    def input_list_int(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> List[int]:
        x = input(prompt).split()
        while not all([lambda i: i.isnumeric() for _ in x]):
            print(error_message)
            x = input(prompt).split()
        return list(map(int, x))

    def input_list_str(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> List[str]:
        x = input(prompt).split()
        while not all([isinstance(i, str) for i in x]):
            print(error_message)
            x = input(prompt).split()
        return list(map(str, x))

    def input_list_char(
        self, prompt: str = "", error_message: str = "An error occured"
    ) -> List[str]:
        x = input(prompt).split()
        while not all([lambda i: len(i) == 1 for _ in x]):
            print(error_message)
            x = input(prompt).split()
        return list(map(str, x))

    def input_list_lambda(
        self,
        validator: Callable[[Any], bool],
        dtype: type,
        prompt: str = "",
        error_message: str = "An error occured",
    ) -> List[Any]:
        # very dangerous please test thank you!!
        x = input(prompt).split()
        while not all([validator(i) for i in x]):
            print(error_message)
            x = input(prompt).split()
        return list(map(dtype, x))


if __name__ == "__main__":

    # ui = UI()

    # TESTS
    # integer = ui.input_int("Enter an integer: ")
    # print(integer)
    # integer = ui.input_int()
    # print(integer)

    # string = ui.input_str("Enter a string: ")
    # print(string)
    # string = ui.input_str()
    # print(string)

    # char = ui.input_char("Enter a char: ")
    # print(char)
    # char = ui.input_char()
    # print(char)
    pass
