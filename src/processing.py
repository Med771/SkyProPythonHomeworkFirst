from time import mktime, strptime, time


def filter_by_state(requests: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает на вход requests типа list[dict], а также state типа str.
    Создаёт filter_transaction_req, а после заносит данные из requests, в которых state равны друг другу.
    Возвращает filter_transaction_req"""

    if not isinstance(requests, list):
        return []

    filter_transaction_req: list[dict] = []

    for request in requests:
        if not isinstance(request, dict):
            continue

        if request.get("state", "") == state:
            filter_transaction_req.append(request)

    return filter_transaction_req


def sort_by_date(requests: list[dict], reverse: bool = True, format_: str = "%Y-%m-%dT%H:%M:%S.%f") -> list[dict]:
    """Принимает на вход requests типа list[dict], а также state типа str.
    Сортирует requests по дате с выбранным значением сортировки.
    Возвращает requests типа list[dict]."""

    if not isinstance(requests, list):
        return []

    def compare(request: dict) -> float:
        if not isinstance(request, dict):
            return time()

        if "date" in request:
            time_: str = request["date"]

            if not isinstance(time_, str):
                return time()

            try:
                return mktime(strptime(time_, format_))
            except ValueError:
                return time()

        return time()

    return sorted(requests, reverse=reverse, key=compare)
