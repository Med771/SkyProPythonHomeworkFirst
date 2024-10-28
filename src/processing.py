from time import mktime, strptime, time


def filter_by_state(requests: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает на вход requests типа list[dict], а также state типа str.
    Создаёт filter_transaction_req, а после заносит данные из requests, в которых state равны друг другу.
    Возвращает filter_transaction_req"""

    filter_transaction_req: list[dict] = []

    for request in requests:
        if request.get("state", "") == state:
            filter_transaction_req.append(request)

    return filter_transaction_req


def sort_by_date(requests: list[dict], reverse: bool = True, format_: str = "%Y-%m-%dT%H:%M:%S.%f") -> list[dict]:
    """Принимает на вход requests типа list[dict], а также state типа str.
    Сортирует requests по дате с выбранным значением сортировки.
    Возвращает requests типа list[dict]."""

    def compare(request: dict) -> float:
        if "date" in request:
            time_: str = request["date"]

            return mktime(strptime(time_, format_))

        return time()

    return sorted(requests, reverse=reverse, key=compare)


if __name__ == "__main__":
    transaction_requests = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(*filter_by_state(transaction_requests), sep="\n")
    print()
    print(*filter_by_state(transaction_requests, state="CANCELED"), sep="\n")
    print()
    print(*sort_by_date(transaction_requests), sep="\n")
    print()
    print(*sort_by_date(transaction_requests, reverse=False), sep="\n")
