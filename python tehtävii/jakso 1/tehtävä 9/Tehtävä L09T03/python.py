from typing import Any, tuple

def is_this_zero(num: Any) -> bool:
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number.")
    return num == 0

def safe_is_this_zero(num: Any) -> tuple[bool, str | None]:
    try:
        result = is_this_zero(num)
        return (result, None)
    except TypeError as e:
        return (False, str(e))

def verify_is_this_zero(test_cases: list[Any]) -> list[tuple[Any, tuple[bool, str | None]]]:
    results = []
    for case in test_cases:
        result = safe_is_this_zero(case)
        results.append((case, result))
    return results

def main():
    test_results = verify_is_this_zero([0, 5, "5", None])
    for input_value, (result, error_message) in test_results:
        if error_message:
            print(f"Input: {input_value}, Result: Error - {error_message}")
        else:
            print(f"Input: {input_value}, Result: {result}")

if __name__ == "__main__":
    main()
