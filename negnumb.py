num1 = 0

while True:
    num2 = float(input("Enter a number ('If you enter a negative number, sum of positive integers will be summed'): "))
    if num2 < 0:
        break
    if num2 > 0:
        num1 += num2
print(num1, "- this is the sum of the positive integers you entered")

        
       

