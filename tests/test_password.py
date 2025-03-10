import unittest
from password_strength_checker import check_password_strength

def test_strong_password():
    score, feedback = check_password_strength("StrongPass123!")
    assert score == 4

def test_weak_password():
    score, feedback = check_password_strength("weak")
    assert score < 4

def test_missing_special_character():
    score, feedback = check_password_strength("Password123")
    assert "Include at least one special character" in feedback
