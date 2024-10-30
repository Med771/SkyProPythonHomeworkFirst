import pytest


@pytest.fixture(scope="module")
def numbers_cards() -> list[tuple]:
    return [
        (1596837868705199, "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        (8990922113665229, "8990 92** **** 5229"),
        (5999414228426353, "5999 41** **** 6353"),
        ((82783, True), "Number type incorrect"),
        ({3, 2, 1}, "Number type incorrect"),
        ("98392839s", "Number not is digits"),
        ("saiusia67", "Number not is digits"),
        ("599941422842635s", "Number not is digits"),
        ("", "Number not is digits"),
        (20930293, "Number incorrect"),
        (0, "Number incorrect"),
        ("2187281727", "Number incorrect"),
    ]


@pytest.fixture()
def accounts() -> list[tuple]:
    return [
        (64686473678894779589, "**9589"),
        ("35383033474447895560", "**5560"),
        (73654108430135874305, "**4305"),
        ([9301920, 9020], "Account type incorrect"),
        ({}, "Account type incorrect"),
        ("", "Account not is digits"),
        ("kkks", "Account not is digits"),
        ("7365410843013587430d", "Account not is digits"),
        (83728378273, "Account incorrect"),
        ("09997", "Account incorrect"),
        (0, "Account incorrect"),
    ]


@pytest.fixture()
def dates() -> list[tuple]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2014-02-11T02:26:18.671407", "11.02.2014"),
        ("2024-03-15T02:26:18.671407", "15.03.2024"),
        ([1, 2, 3], "Date type incorrect"),
        ({1982912, 817282, 109902}, "Date type incorrect"),
        ([[111, 90], "2024-03-15T02:26:18.671407"], "Date type incorrect"),
        ("", "Date format incorrect"),
        ("2024-0:18.671407", "Date format incorrect"),
        ("2014-02-11", "Date format incorrect"),
        (":26:18.671407", "Date format incorrect"),
    ]


@pytest.fixture()
def accounts_cards() -> list[tuple]:
    return [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ([], "Account card type incorrect"),
        ({1, 2, 3}, "Account card type incorrect"),
        ("Maestro 159683785199", "Account card unknown"),
        ("Счет 9589", "Account card unknown"),
    ]


@pytest.fixture()
def transaction_requests_for_filter() -> list[tuple]:
    filter_answers = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ]

    return filter_answers


@pytest.fixture()
def transaction_requests_by_sort() -> list[tuple]:
    sort_answers = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
    ]

    return sort_answers
