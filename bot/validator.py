# bot/validator.py

def validate_order_args(args):
    if args.type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT orders require --price")

    if args.qty <= 0:
        raise ValueError("Quantity must be greater than 0")

    if args.price is not None and args.price <= 0:
        raise ValueError("Price must be greater than 0")

    return True
