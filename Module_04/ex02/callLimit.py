from typing import Any


def callLimit(limit: int):
    """
    This function blocks his execution above a limite.
    When we call @callLimit(n), it will call callLimiter()
    with our function and it will call limit_function to
    check if we can execute is or not."""
    def callLimiter(function):
        def limit_function(*args: Any, **kwargs: Any):
            if limit_function.counter < limit:
                limit_function.counter += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
                return None
        limit_function.counter = 0
        return limit_function
    return callLimiter
