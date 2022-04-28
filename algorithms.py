from typing import List
from record import Record

# use sleep for debugging file loops !
# from time import sleep

"""Algorithms Library!!"""

#######* WORKFLOW *#######
#
# - Make it work with integers first
# - Then duplicate and modify it for Records
#
##########################


def bubble_sort(arr: List[int]) -> List[int]:
    swap = True

    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                swap = True
    return arr


def bubble_sort_record(arr: List[Record]) -> List[Record]:
    swap = True

    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i].customer_name > arr[i + 1].customer_name:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                swap = True
    return arr


def selection_sort(arr: List[int]) -> List[int]:

    for j in range(len(arr)):
        i = arr.index(min(arr[j:]))
        if i == j:
            pass
        else:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
    return arr


def selection_sort_record(arr: List[Record]) -> List[Record]:

    for j in range(len(arr)):
        i = arr.index(min(arr[j:], key=lambda x: x.package_name))
        if i == j:
            pass
        else:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp
            j -= 1
    return arr


def insertion_sort_record(arr: List[Record]) -> List[Record]:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1].cost_per_pax > arr[j].cost_per_pax:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp
            j -= 1
    return arr


def linear_search(arr: List[int], target: int) -> int | None:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return None


def linear_search_record(arr: List[Record], customer_name: str) -> Record | None:
    for i in arr:
        if i.customer_name.lower() == customer_name.lower():
            return i
    return None


def binary_search(arr: List[int], target: int) -> int | None:
    low = 0
    high = len(arr) - 1
    mid = (high - low) // 2

    while target not in [arr[low], arr[mid], arr[high]]:
        if (target < arr[low]) or (target > arr[high]):
            return None

        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        mid = (high - low) // 2 + low

    if target == arr[low]:
        return low
    elif target == arr[mid]:
        return mid
    elif target == arr[high]:
        return high


def binary_search_record(arr: List[Record], target: str) -> Record | None:
    low = 0
    high = len(arr) - 1
    mid = (high - low) // 2

    # for i in range(len(arr)):
    #     print(i, arr[i].package_name)

    target = target.lower()

    while target not in [
        # hey if you're feeling depressed listen to radiohead
        # it'll make you wanna jump faster than a bullet
        arr[low].package_name.lower(),
        arr[mid].package_name.lower(),
        arr[high].package_name.lower(),
    ]:

        # print()
        # print("Low:", low)
        # print("Mid:", mid)
        # print("High:", high)
        # print()

        # all for no case sensitivity ???
        # we live in a horrible society.
        low_val = arr[low].package_name.lower()
        mid_val = arr[mid].package_name.lower()
        high_val = arr[high].package_name.lower()

        if target < low_val or target > high_val:
            return None

        if target < mid_val:
            # print("target is lower than mid")
            high = mid - 1
        elif target > mid_val:
            # print("target is higher than mid")
            low = mid + 1

        # LOL! please remember to adjust the mid index according to the lowest
        # index. debugging this was fun but i don't think ppl will be very
        # impressed LOL
        mid = (high - low) // 2 + low
        # sleep(3)

    # its literally like 1984
    low_val = arr[low].package_name.lower()
    mid_val = arr[mid].package_name.lower()
    high_val = arr[high].package_name.lower()

    # don't ask me to make this shorter
    if target == low_val:
        return arr[low]
    elif target == mid_val:
        return arr[mid]
    elif target == high_val:
        return arr[high]


def breadth_first_search():
    raise NotImplementedError()


def depth_first_search():
    raise NotImplementedError()


if __name__ == "__main__":

    print("Testing", binary_search.__name__)

    test = [2, 3, 1, 8, 5, 7, 10, 6, 4, 9]
    test = insertion_sort(test)
    print(binary_search(test, 100))
