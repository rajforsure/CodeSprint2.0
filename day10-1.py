digits = input().strip()

if not digits:
  print([])
  exit()

keypad = {
  '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl',
  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

combinations = []

def backtrack(index, path):
  if index == len(digits):
    combinations.append(path)
    return
  for letter in keypad.get(digits[index], ''):
    backtrack(index + 1,path + letter)

backtrack(0, "")
print(combinations)

