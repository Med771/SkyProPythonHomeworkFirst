from typing import Union


def get_mask_card_number(number: Union[str, int]) -> str:
    number = str(number)

    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(number: Union[str, int]) -> str:
    number = str(number)

    return f"**{number[-4:]}"


if __name__ == "__main__":
    number_card = 7000792289606361

    print(get_mask_card_number(number=number_card))
    print(get_mask_account(number=number_card))
