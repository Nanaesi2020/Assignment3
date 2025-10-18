"""
Square Area Calculator
A simple Python application that calculates the area of a square.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square given the side length.
    
    Args:
        side_length (float): The length of one side of the square
        
    Returns:
        float: The area of the square (side_length squared)
        
    Raises:
        ValueError: If side_length is negative
        TypeError: If side_length is not a number
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number")
    
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    
    return side_length ** 2


def main():
    """Main function to run the square area calculator interactively."""
    print("Square Area Calculator")
    print("=" * 40)
    
    try:
        side = float(input("Enter the side length of the square: "))
        area = calculate_square_area(side)
        print(f"\nThe area of a square with side length {side} is: {area}")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
