"""
Unit tests for the square area calculator application.
Uses pytest framework for testing.
"""

import pytest
from square_area import calculate_square_area


class TestSquareArea:
    """Test suite for square area calculations."""
    
    def test_positive_integer(self):
        """Test with a positive integer."""
        assert calculate_square_area(5) == 25
    
    def test_positive_float(self):
        """Test with a positive floating-point number."""
        assert calculate_square_area(3.5) == 12.25
    
    def test_zero(self):
        """Test with zero."""
        assert calculate_square_area(0) == 0
    
    def test_negative_number(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError):
            calculate_square_area(-5)
    
    def test_invalid_type_string(self):
        """Test that string input raises TypeError."""
        with pytest.raises(TypeError):
            calculate_square_area("10")
    
    def test_invalid_type_none(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError):
            calculate_square_area(None)
    
    def test_large_number(self):
        """Test with a large number."""
        assert calculate_square_area(100) == 10000
    
    def test_student_id_custom(self):
        """
        Custom test using last two digits of student ID.
        Student ID: 100957828
        Last two digits: 28
        Expected area: 28 * 28 = 900
        """
        # Test that a square with side length 30 has area 900
        assert calculate_square_area(28) == 900
        # assert calculate_square_area(21) == 800  # Intentionally wrong to demonstrate failure