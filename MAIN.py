
def To_RGB():
    B = str(input("Blue: "))
    G = str(input("Green: "))
    R = str(input("Red: "))

    RGB = "(" + R + ", " + G + ", " + B + ")"
    BGR = "(" + B + ", " + G + ", " + R + ")"

    print("Original: " + BGR)
    print("Converted: " + RGB)

def To_BGR():
    R = str(input("Red: "))
    G = str(input("Green: "))
    B = str(input("Blue: "))

    RGB = "(" + R + ", " + G + ", " + B + ")"
    BGR = "(" + B + ", " + G + ", " + R + ")"

    print("Original: " + RGB)
    print("Converted: " + BGR)

choice = int(input("1 to convert RGB to BGR/2 to convert BGR to RGB: "))
if choice == 1:
    To_BGR()

elif choice== 2:
    To_RGB()
