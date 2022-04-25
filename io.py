"""Luth Andyka's personal "Safe" input library :D"""

from typing import Any, Callable, List


def input_int() -> int:
    raise NotImplementedError()


def input_str() -> str:
    raise NotImplementedError()


def input_char() -> str:
    raise NotImplementedError()


def input_lambda(func: Callable[[str], bool]) -> Any:
    raise NotImplementedError()


def input_list_int() -> List[int]:
    raise NotImplementedError()


def input_list_str() -> List[str]:
    raise NotImplementedError()


def input_list_char() -> List[str]:
    raise NotImplementedError()


def input_list_lambda(func: Callable[[str], bool]) -> List[Any]:
    raise NotImplementedError()
