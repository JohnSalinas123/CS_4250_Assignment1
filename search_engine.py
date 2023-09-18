#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])
            


#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

for i in range(len(documents)):
  word_list = documents[i].split()
  for word in word_list:
    word_low = word.lower()
    for stop in stopWords:
      stop_low = stop.lower()
      if word_low == stop_low:
        word_list.remove(word)
  documents[i] = " ".join(word_list)
  

        


#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}

for i in range(len(documents)):
  word_list = documents[i].split()
  for w in range(len(word_list)):
    word_low = word_list[w].lower()
    if word_low in steeming:
      word_list[w] = steeming[word_low]
  documents[i] = " ".join(word_list)
  
print("Documents",documents)

  

#Identify the index terms.
#--> add your Python code here
terms = []
for i in range(len(documents)):
  word_list = documents[i].split()
  for w in range(len(word_list)):
    world_low = word_list[w].lower()
    if world_low not in terms:
      terms.append(world_low)

#Build the if-idf term weights matrix.
#--> add your Python code here
docMatrix = []

word_count = {}
for i in range(len(documents)):
  word_list = documents[i].split()
  for w in range(len(word_list)):
    world_low = word_list[w]
    if world_low in word_count:
      word_count[world_low] += 1
    else:
      word_count[world_low] = 1

doc_count = {}
for i in range(len(documents)):
  word_list = documents[i].split()
  for key in word_count:
    if key in word_list and key in doc_count:
      doc_count[key] += 1
    elif key in word_list and key not in doc_count:
      doc_count[key] = 1

def calcTF(doc_index, word):
  temp = documents[doc_index].split()
  doc_len = len(temp)
  freq = temp.count(word)
  return freq/doc_len

def calcIDF(word):
  return math.log10(len(documents)/doc_count[word])

for i in range(len(documents)):
  new_row = [0 for i in range(len(terms))]
  docMatrix.append(new_row)
  
#print(docMatrix)


for i in range(len(documents)):
  word = terms[i]
  col_idf = calcIDF(word)
  #print(col_idf)
  for j in range(len(terms)):
    row_tf = calcTF(j,word)
    #print(row_tf)
    docMatrix[j][i] = round(col_idf * row_tf,4)
    
print(docMatrix)
  
  


#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []
query = "cats and dogs"

#query stopping
query_words = query.split()
left = 0
while left < len(query_words):
  query_low1 = query_words[left].lower()
  for stop in stopWords:
    stop_low = stop.lower()
    if query_low1 == stop_low:
      query_words.remove(stop_low)
  left += 1

print("Stopped:",query_words)

# query stemming
for i in range(len(query_words)):
  query_low2 = query_words[i].lower()
  if query_low2 in steeming:
    query_words[i] = steeming[query_low2]

print("Final Query", query_words)

query_binary = []


for i in range(len(terms)):
  if terms[i] in query_words:
    query_binary.append(1)
  else:
    query_binary.append(0)

print(query_binary)




#Calculate the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here