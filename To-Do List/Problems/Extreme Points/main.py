# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
#test_dict = {"a": 43, "b": 1233, "c": 8}
reverse_dict = {value: key for key, value in test_dict.items()}
print('min:', reverse_dict[min(reverse_dict)])
print('max:', reverse_dict[max(reverse_dict)])

# Work with the 'test_dict'