# Packages - Cowsay

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     # cowsay.cow("Hi, " + sys.argv[1])
#     cowsay.trex("Hello, " + sys.argv[1])

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
