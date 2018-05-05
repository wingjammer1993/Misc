import copy
import sys

listed = []

try:
	while True:
		inp = raw_input()
		if inp != "":
			listed.append(inp)
		else:
			break
except EOFError:
	pass

index = 0
graphs = []
case = 0
while index < len(listed):
	case += 1
	m = listed[index][0]
	n = listed[index][-1]
	keys = []
	values = []
	index += 1
	for j in range(0, int(n)):
		keys.append(listed[index][0])
		values.append(listed[index][-1])
		index += 1
	stack = copy.deepcopy(keys)
	for idx, k in enumerate(keys):
		if values[idx] in keys:
			stack.remove(values[idx])
	if len(stack) == 0:
		sys.stdout.write("Case" + str(case) + ": valid" + "\n")
	else:
		flag = 0
		for idx, _ in enumerate(keys):
			keys_deep = copy.deepcopy(keys)
			values_deep = copy.deepcopy(values)
			temp = keys_deep[idx]
			keys_deep[idx] = values_deep[idx]
			values_deep[idx] = temp
			stack = copy.deepcopy(keys_deep)
			for idxy, ky in enumerate(keys_deep):
				if values_deep[idxy] in keys_deep:
					stack.remove(values_deep[idxy])
			if len(stack) == 0:
				sys.stdout.write("Case" + str(case) + ": " + str(values_deep[idx]) + " " + str(keys_deep[idx] + "\n"))
				flag = 1
				break
		if flag == 0:
			sys.stdout.write("Case" + str(case) + ": invalid" + "\n")





