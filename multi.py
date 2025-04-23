"""Module to multiply two numbers."""

def multiply_numbers(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b

if __name__ == "__main__":
    A = 4
    B = 5
    RESULT = multiply_numbers(A, B)
    print(f"The product of {A} and {B} is {RESULT}.")
