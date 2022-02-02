print(" *** Min Max Avg ***")
a, b, c = input("Enter 3 numbers : ").split()
a = float(a)
b = float(b)
c = float(c)
if a <= b <= c:
    print(f"min, mid, max == > {a:.1f}, {b:.1f}, {c:.1f}")
elif a <= c <= b:
    print(f"min, mid, max == > {a:.1f}, {c:.1f}, {b:.1f}")
elif b <= a <= c:
    print(f"min, mid, max == > {b:.1f}, {a:.1f}, {c:.1f}")
elif b <= c <= a:
    print(f"min, mid, max == > {b:.1f}, {c:.1f}, {a:.1f}")
elif c <= a <= b:
    print(f"min, mid, max == > {c:.1f}, {a:.1f}, {b:.1f}")
elif c <= b <= a:
    print(f"min, mid, max == > {c:.1f}, {b:.1f}, {a:.1f}")
print(f"Average ==> {(a+b+c)/3:.2f}")
