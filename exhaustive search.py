import string
import itertools

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "


for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
  candidate = "".join(candidate)
  print(candidate, end="\r")

  if candidate == TARGET:
    break