import sys

def fib_memo(n, memo):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif memo[n] > 0:
		return memo[n]
	else:
		memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
		print(memo)
		return memo[n]

def all_fib(user_no):
	size = user_no + 1
	memo = [-1] * size
	for n in range(user_no, 0 , -1):
		print("%s: %s" % (n, fib_memo(n, memo)))

def main():
	user_no = input("which fib: ")
	try:
		all_fib(int(user_no))
	except Exception as e:
		print("Invalid input")
		sys.exit(1)


def test():
	assert fib_memo(1) == 1
	assert fib_memo("ab") == "Invalid input"


if __name__ == "__main__":
	main()
else:
	test()