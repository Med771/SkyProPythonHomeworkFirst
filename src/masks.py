from typing import Union


def get_mask_card_number(number: Union[str, int]) -> str:
    """Принимает на вход number (номер карты) типов int | str.
    Возвращает скрытый номер карты типа str в формате .... ..** **** ...."""
    if not (isinstance(number, int) or isinstance(number, str)):
        return "Number type incorrect"

    if isinstance(number, int):
        number = str(number)

    number.strip()

    if not number.isdigit():
        return "Number not is digits"

    if len(number) != 16:
        return "Number incorrect"

    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(number: Union[str, int]) -> str:
    """Принимает на вход number (номер карты) типов int | str.
    Возвращает скрытый номер карты типа str в формате **...."""
    if not (isinstance(number, int) or isinstance(number, str)):
        return "Account type incorrect"

    if isinstance(number, int):
        number = str(number)

    number.strip()

    if not number.isdigit():
        return "Account not is digits"

    if len(number) != 20:
        return "Account incorrect"

    return f"**{number[-4:]}"
