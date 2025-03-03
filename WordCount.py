#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("Cameron's.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0


  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      characters = len(line) +  1 

  print ("Lines:", lineCount)
  print ("Words:", wordCount)
  print ("Characters", characters)
  
  

if __name__ == '__main__':
  main()
