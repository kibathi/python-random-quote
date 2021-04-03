import random
def pri():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  getlast = len(quotes)
  last = len(quotes)-1
  rnd = random.randint(0,last)

  # print(getlast)
  print(quotes[rnd])


if __name__== "__main__":
  pri()
