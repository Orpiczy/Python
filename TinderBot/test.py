from random import seed
from random import randint
import messages

seed(1)
for i in range(100):
    combine_message = messages.pickup_lines[randint(0, 3)]
    print(combine_message)
