def multiply(num):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * num
        return wrapper
    return decorator

@multiply(3)
def sum_nums(num_1, num_2, ):
    return num_1 + num_2

print(sum_nums(1,num_2 =2))