num1 = 0
stop = ""

while True:
    num2 = float(input("Enter a number (negative numbers  will not be summed. Type finish to stop): "))
    if num2 < 0:
        break
    if num2 > 0: 
        num1 += num2
    if stop == "finsh":
        break
    print(num2)