expected_result = input()
actual_result  = input()


if -1 == expected_result.find(actual_result):
    print(f"expected '{expected_result}' to be substring of '{actual_result}'")