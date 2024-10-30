from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transaction_requests_for_filter: list[tuple]) -> None:
    for transaction_request in transaction_requests_for_filter:
        query, state, result = transaction_request

        assert filter_by_state(query, state) == result


def test_sort_by_date(transaction_requests_by_sort: list[tuple]) -> None:
    for transaction_request in transaction_requests_by_sort:
        query, reverse, result = transaction_request

        assert sort_by_date(query, reverse) == result
