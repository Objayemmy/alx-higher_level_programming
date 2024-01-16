#!/usr/bin/python3
for i in range(0, 10):
    print(", ".join(f"{i}{j}" for j in range(i + 1, 10)), end='\n' if i == 8 else ', ')
