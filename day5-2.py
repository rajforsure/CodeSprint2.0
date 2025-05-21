s = input()
freq = {}

for char in s:
  freq[char] = freq.get(char, 0) + 1

values = list(freq.values())
if all(v == values[0] for v in values):
  print("Aashriya smiles: Emotional balance found.")
else:
  print("Aashriya wonder: Thes thoughts were scattered.")