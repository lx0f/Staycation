from types import NoneType
from record import Record
from ui import UI
from typing import List
from algorithms import (
    bubble_sort_record,
    selection_sort_record,
    insertion_sort_record,
    linear_search_record,
    binary_search_record,
)

# 3 часа ночи, и я начинаю слышать и видеть вещи, которых нет. Я действительно
# не должен был вздремнуть в тот вечер.

# aw yea level up time
def needs_records(func):
    """use this decorator for functions that require record data"""

    def wrapped(self, *args, **kwargs):
        if self.record_list is not None:
            return func(self, *args, **kwargs)
        else:
            print("To run that action, you will need records")
            print("Please consider adding records")

    wrapped.__name__ = func.__name__
    return wrapped


class CLI:
    def __init__(self, record_list: List[Record] | None = None):
        self.actions = {
            1: self.display_all_records,
            2: self.display_from_price_range,
            3: self.sort_by_customer_name,
            4: self.sort_by_package_cost,
            5: self.sort_by_package_name,
            6: self.search_by_customer_name,
            7: self.search_by_package_name,
            8: self.exit,
        }

        self.record_list = record_list
        self.record_size = len(record_list) if record_list else None

        self.ui = UI()
        self.run = True

    def import_records(self, record_list: List[Record]) -> None:
        self.record_list = record_list

    def is_valid_action(self, x: int) -> bool:
        return x in self.actions

    def run_action(self, x: int) -> None:
        return self.actions[x]()

    def display_actions(self) -> None:

        for k, v in self.actions.items():
            print(f"{k}:", v.__name__)
        print()

    def exit(self) -> None:
        print("Have a wonderful day!")
        print("Bye bye!!")
        self.run = False

    @needs_records
    def __sort_by_package_name(self) -> List[Record]:
        sorted_records = selection_sort_record(self.record_list)
        return sorted_records

    @needs_records
    def display_all_records(self) -> None:
        for record in self.record_list:
            print(record)
        print()

    @needs_records
    def display_from_price_range(self) -> None:
        # TODO: support float values
        min = self.ui.input_int("Enter minimum price: ")
        max = self.ui.input_int("Enter maximum price: ")

        insertion_sort_record(self.record_list)

        for record in self.record_list:
            if record.cost_per_pax >= min and record.cost_per_pax <= max:
                print(record)
        print()

    @needs_records
    def sort_by_customer_name(self) -> None:
        # use bubble sort
        bubble_sort_record(self.record_list)
        print("Sorted! - via bubble sort")

    @needs_records
    def sort_by_package_cost(self) -> None:
        # use insertion sort
        insertion_sort_record(self.record_list)
        print("Sorted! - via isertion sort")

    @needs_records
    def sort_by_package_name(self) -> None:
        # use selection sort
        selection_sort_record(self.record_list)
        print("Sorted! - via selection sort")

    @needs_records
    def search_by_customer_name(self) -> None:
        customer_name = self.ui.input_str(
            "Please enter the customer name to search: "
        ).lower()
        record = linear_search_record(self.record_list, customer_name)
        print(record)

    @needs_records
    def search_by_package_name(self) -> None:
        # use binary search
        customer_name = self.ui.input_str(
            "Please enter the package name to search: "
        ).lower()
        sorted_records = self.__sort_by_package_name()
        record = binary_search_record(sorted_records, customer_name)
        print(record)


if __name__ == "__main__":
    # ui = UI()
    # cli = CLI()
    pass
