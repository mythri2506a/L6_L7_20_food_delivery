import math


def parse_order(items_csv):
    """Parse 'name:qty,name:qty' into a dict. Invalid items are skipped."""
    if not isinstance(items_csv, str):
        return {}
    order = {}
    for item in items_csv.split(','):
        parts = item.split(':')
        if len(parts) != 2:          # missing ':' or too many ':'
            continue
        name, qty = parts[0].strip(), parts[1].strip()
        if not name:
            continue
        try:
            qty = int(qty)
        except ValueError:           # qty not a number
            continue
        if qty <= 0:                 # zero / negative quantity
            continue
        order[name] = order.get(name, 0) + qty   # duplicates add up
    return order


def delivery_eta(distance_km):
    """ETA in minutes, or None if the distance is invalid."""
    if distance_km is None or isinstance(distance_km, bool):
        return None
    try:
        distance = float(distance_km)
    except (TypeError, ValueError):  # not a number
        return None
    if not math.isfinite(distance) or distance <= 0:   # nan, inf, 0, negative
        return None
    return int(15 + distance * 4)


def coupon_discount(code):
    """Discount from a 'SAVE<number>' code, or 0 if the code is invalid."""
    if not isinstance(code, str):
        return 0
    code = code.strip().upper()
    if not code.startswith("SAVE"):
        return 0
    amount = code[4:]
    if not (amount.isascii() and amount.isdigit()):   # empty, letters, unicode digits
        return 0
    return int(amount)


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result if result else "No valid items entered")

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result if result is not None else "Invalid distance")

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result if result else "Invalid coupon")


if __name__ == "__main__":
    main()
