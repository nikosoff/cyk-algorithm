import numpy as np
import sys        
        
        
def exploreTree(A, T, rules, sentence, space):
  i = int(rules.split(",")[0])
  j = int(rules.split(",")[1])
  rules = T[i,j]
  coordinates = rules.split("-")
  if "@" not in coordinates[0]:
    xy = coordinates[0].split(",")
    print(space + "  |-" + sentence.split()[int(xy[0])])
    return
  left = coordinates[0].split("@")[0].split(",")
  print(space + " |-" + A[int(left[0]),int(left[1])].split(",")[0])
  if len(coordinates) >= 2:
    A[i,j] = ','.join(A[i,j].split(",")[1:])
    T[i,j] = '-'.join(T[i,j].split("-")[1:])
  exploreTree(A,T,left[0]+","+left[1],sentence,space+" ")
  
  right = coordinates[0].split("@")[1].split(",")
  print(space + " |-" + A[int(right[0]),int(right[1])].split(",")[0])
  exploreTree(A,T,right[0]+","+right[1],sentence,space+" ")
 


def CYKalgorithm(sentence):

  words = sentence.split(" ")
  A = np.chararray([len(words),len(words)+1],unicode=True,itemsize=100)
  T = np.chararray([len(words),len(words)+1],unicode=True,itemsize=100)
  N = A.shape[1]
  A[:] = ""

  for i in range(0,N-1):
    A[i,i+1] = rules[words[i]]
    T[i,i+1] = str(i)+","+str(i+1)

  for k in range(2,N):
    for i in range(0,N-k):
      for j in range(i+1,i+k):
        if A[i,j] != "" and A[j,i+k] != "":
          left_rules = A[i,j].split(",")
          right_rules = A[j,i+k].split(",")
          for lr in left_rules:
            for rr in right_rules:
              candidate_rule = lr + " " + rr
              if candidate_rule in rules:
                if A[i,i+k] != "":
                  A[i,i+k] = A[i,i+k] + "," + rules[candidate_rule]
                  T[i,i+k] = T[i,i+k] + "-" + str(i) + "," + str(j) + "@" + str(j) + "," +str(i+k)
                else:
                  A[i,i+k] = rules[candidate_rule]
                  T[i,i+k] = str(i) + "," + str(j) + "@" + str(j) + "," + str(i+k)
  
  if "S" not in A[0,A.shape[0]]:
    print("The sentence \""+sentence+"\" is not recognized by the grammar")
    return False
  else:
    print("The sentence \""+sentence+"\" is recognized by the grammar")
  
  for i in range(0,len(T[0,N-1].split("-"))):
   print("S")
   exploreTree(A,T,"0,"+str(N-1),sentence,"")
     

  return True
  
def is_input_valid(sentence, rules):
   
    for word in sentence.split(" "):
        if word not in rules.keys():
            return False
    return True


  
arguments = sys.argv  
  
input_file = arguments[1]
sentence = arguments[2]

#Grammar should be in Chomsky Normal Form(CNF)
rules = dict()
with open(input_file, encoding="utf-8") as rules_file:
    for line in rules_file:
        terms = line.rstrip().split("->")
        rules[terms[1]] = terms[0]

        
if is_input_valid(sentence, rules):        
    CYKalgorithm(sentence)
else:
    print("The sentence \""+sentence+"\" is not recognized by the grammar")