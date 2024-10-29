def mult(**args):
    if not args:
        a, b = 1, 1
    else:
        a = args.get('a', 1)
        b = args.get('b', 2)
    return a * b
