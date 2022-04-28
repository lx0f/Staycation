from record import Record
from ui import UI
from typing import Callable, Dict, List
from algorithms import (
    bubble_sort_record,
    selection_sort_record,
    insertion_sort_record,
    linear_search_record,
    binary_search_record,
)


class CLI:
    def __init__(self, record_list: List[Record]):
        print("Initializing Staycation Package Deals Inventory CLI...")
        self.actions = {
            1: self.display_all_records,
            2: self.display_from_price_range,
            3: self.sort_by_customer_name,
            4: self.sort_by_package_cost,
            5: self.sort_by_package_name,
            6: self.search_by_customer_name,
            7: self.search_by_package_name,
        }

        print("Importint Records...")
        self.record_list = record_list
        self.record_size = len(record_list)

        self.ui = UI()

    def __sort_by_package_name(self) -> List[Record]:
        sorted_records = selection_sort_record(self.record_list)
        return sorted_records

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

    def display_all_records(self) -> None:
        for record in self.record_list:
            print(record)
        print()

    def display_from_price_range(self) -> None:
        raise NotImplementedError()

    def sort_by_customer_name(self) -> None:
        # use bubble sort
        bubble_sort_record(self.record_list)
        print("Sorted! - via bubble sort")

    def sort_by_package_cost(self) -> None:
        # use insertion sort
        insertion_sort_record(self.record_list)
        print("Sorted! - via isertion sort")

    def sort_by_package_name(self) -> None:
        # use selection sort
        selection_sort_record(self.record_list)
        print("Sorted! - via selection sort")

    def search_by_customer_name(self) -> None:
        customer_name = self.ui.input_str(
            "Please enter the customer name to search: "
        ).lower()
        record = linear_search_record(self.record_list, customer_name)
        print(record)

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
