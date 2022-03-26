def print_log(func):
	def wrapper(*args, **kwargs):
		print(f'{func.__name__} была исполнена')
		return func(*args, **kwargs)

	return wrapper


@print_log
def some_func(x, y):
	return x * y


print(some_func(4, 6))
