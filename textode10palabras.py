juan = input("Enter a string: ")

if len(juan) > 10:
    juan = juan[:10] + "..."

print("Resultado: " + juan)