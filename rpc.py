import random
from os import system

system('cls')

print("""

Welcome to RPC Python

      Here is a list on how to play

      R = Rock
      P = Paper
      S = Sciossors

      The choice is yours

      Can you beat the SYSTEM?
          


""")


main_input = input('RPC> ')

rpc_list = ['r', 'p', 's']

if main_input not in rpc_list:
    print(rpc_list)