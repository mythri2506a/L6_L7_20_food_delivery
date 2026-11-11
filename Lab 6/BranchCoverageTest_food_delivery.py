import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# ---------- delivery_charge ----------
def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_out_of_range_raises():
    with pytest.raises(ValueError):
        delivery_charge(20, 200, False)

def test_free_delivery_big_order():
    assert delivery_charge(5, 600, False) == 0

def test_mid_distance():
    assert delivery_charge(5, 200, False) == 40

def test_far_distance_raining():
    assert delivery_charge(10, 200, True) == 90


# ---------- apply_coupon ----------
def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

def test_invalid_coupon():
    with pytest.raises(ValueError):
        apply_coupon(300, "FAKE", False)

def test_welcome_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)

def test_small_order_no_discount():
    assert apply_coupon(150, "SAVE50", False) == 150

def test_valid_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


# ---------- estimated_time ----------
def test_peak_and_busy():
    assert estimated_time(5, True, True) == 15 + 20 + 10 + 15 + 5


# ---------- extra tests for branch coverage ----------
def test_zero_distance_raises():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)

def test_boundary_3km():
    assert delivery_charge(3, 200, False) == 20

def test_boundary_8km():
    assert delivery_charge(8, 200, False) == 40

def test_boundary_15km():
    assert delivery_charge(15, 200, False) == 60

def test_order_exactly_500_raining():
    assert delivery_charge(2, 500, True) == 30

def test_welcome_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200

def test_order_exactly_200():
    assert apply_coupon(200, "SAVE50", False) == 150

def test_no_peak_no_busy():
    assert estimated_time(5, False, False) == 35

def test_peak_only():
    assert estimated_time(5, True, False) == 45

def test_busy_only():
    assert estimated_time(5, False, True) == 50
