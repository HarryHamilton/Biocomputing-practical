import string
import itertools

CHARACTERS = string.ascii_uppercase + " "
TARGET = "CHARLES DARWIN"
best = len(TARGET)


def evaluate(solution):
  return sum(1 for s,t in zip(solution, TARGET) if s != t)

for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
  distance = evaluate(candidate)
  if distance < best:
    best = distance
    print("{0:02} {1}".format(distance, "".join(candidate)))

