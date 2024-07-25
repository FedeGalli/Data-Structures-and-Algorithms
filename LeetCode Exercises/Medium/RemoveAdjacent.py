def adjacentRem(s : str, k) -> str:
	stack = []

	for char in s:
		if len(stack) and char == stack[-1][0]:
			if stack[-1][1] == k - 1:
				for _ in range(1, k):
					stack.pop()
			else:
				stack.append([char, stack[-1][1] + 1])
		else:
			stack.append([char, 1])
			
	
	return_string = [elem[0] for elem in stack]
	return ''.join(return_string)
	

print(adjacentRem("deeedbbcccbdaa", 3))
