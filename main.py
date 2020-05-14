# Core Reference Libraries
from random import randrange
from time import time

# Written Code Libraries
from heap import heapSort
from linear import search
from binary import binarySearch

def main():
  rando = []
  linerarFound = 0
  binaryFound = 0

  for index in range(0, 10000):
    rando.append(randrange(0, 1000000))

  searches = int(input("How many searches will be performed: "))
  searches = searches

  #### Pre-Sorted ####
  print("Linear Start!\n"); linearStart = time()
  for i in range(0, searches):
    k = randrange(0, 1000000)
    # print("Searching for: ", k)
    found = search(rando, k)

    if found != -1:
      linerarFound += 1
  linearEnd = time()

  print("Total time for %d linear searches: %.5f\n" % (searches, linearEnd - linearStart))
  #### Post-Sorted ####

  # Run HeapSort
  print("Binary Start!\n"); binaryStart = time()
  rando = heapSort(rando)

  for i in range(0, searches):
    k = randrange(0, 1000000)
    found = binarySearch(rando, 0, len(rando)-1, k)

    if found != -1:
      binaryFound += 1

  binaryEnd = time()

  print("Total time for %d binary searches: %.5f\n" % (searches, binaryEnd - binaryStart))

  print("--------------------------------------")

  print("Linear Finds: %d\nLinear Time: %.5f\n" % (linerarFound, linearEnd - linearStart))
  print("Binary Finds: %d\nBinary Time: %.5f\n" % (binaryFound, binaryEnd - binaryStart))

main()