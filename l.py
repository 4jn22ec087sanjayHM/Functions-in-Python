def apply_operation(number,operation):

    return operation(number)

square = lambda x: x ** 2
double = lambda x: x * 2
result1=apply_operation(5, square)
result2=apply_operation(5, double)
print(result1,result2)
