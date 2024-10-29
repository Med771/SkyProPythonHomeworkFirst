from time import strftime, strptime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Принимает информацию о карте типа str в форматах Card Type Number / Account Number.
    В зависимости от ответа, возвращает str в форматах Card Type .... .. **** .... / Account ...."""

    if not isinstance(account_card, str):
        return "Account card type incorrect"

    account_card.strip()

    info_values = account_card.split()

    if len(info_values) > 1:
        number = info_values[-1]

        if len(number) == 16:
            return f"{' '.join(info_values[:-1])} {get_mask_card_number(number)}"
        if len(number) == 20:
            return f"{' '.join(info_values[:-1])} {get_mask_account(number)}"

    return "Account card unknown"


def get_date(date: str) -> str:
    """Принимает дату типа str в формате%Y-%m-%dT%H:%M:%S.%f.
    Возвращает дату типа str в формате %d.%m.%Y."""
    if not isinstance(date, str):
        return "Date type incorrect"

    date.strip()

    try:
        reformatted = strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return "Date format incorrect"

    return strftime("%d.%m.%Y", reformatted)
