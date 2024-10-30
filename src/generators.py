from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, None, None]:
    """Получает список транзакций и код валюты.
    Возвращает генератор со словарём транзакции или None если такой транзакции больше нет"""

    if isinstance(currency_code, str) and isinstance(transactions, list):
        for transaction in transactions:
            if not isinstance(transaction, dict):
                continue

            operation_amount = transaction.get("operationAmount", {})
            currency = operation_amount.get("currency", {})

            if currency_code == currency["code"]:
                yield transaction

    return None


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Получает список транзакций.
    Возвращает генератор со строкой из транзакции или None."""

    if isinstance(transactions, list):
        for transaction in transactions:
            if not isinstance(transaction, dict):
                continue

            if "description" in transaction:
                yield transaction["description"]

    return None


def card_number_generator(start_number_card: int, end_number_card: int) -> Generator[str, None, None]:
    """Получает стартовый номер > 0 и конечный номер < 10_000_000_000_000_000.
    Возвращает генератор со строкой сгенерированного номера или None."""

    if isinstance(start_number_card, int) and isinstance(end_number_card, int):
        if start_number_card > 0 and end_number_card < 10_000_000_000_000_000:
            for i in range(start_number_card, end_number_card + 1):
                card_number = str(i).rjust(16, "0")

                yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

    return None


if __name__ == "__main__":
    gen = card_number_generator(1, 5)

    while True:
        res = next(gen)
        print(res)

        if res is None:
            break
