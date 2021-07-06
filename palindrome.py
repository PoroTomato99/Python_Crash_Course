message = "abc123"


a = ""
reversed_a = ""
for c in message:
    print(f"this is => {c}")
    a = a + c
    print(f"this is a => {a}")
    reversed_a = c + reversed_a
    print(f"this is reversed_a => {reversed_a}")

print(a)
print(reversed_a)
    