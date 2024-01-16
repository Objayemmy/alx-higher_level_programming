#!/usr/bin/python3
[200~import random

        number = random.randint(-10, 10)

        result = "negative" if number < 0 else "zero" if number == 0 else "positive"
        print(f"{number} is {result}")
