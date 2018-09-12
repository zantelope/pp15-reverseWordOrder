
def reverseWordOrder(sentence):
  split_sent = sentence.split(" ")

  reverse_sent = ""


  for i in split_sent[::-1]:
    reverse_sent += i + " "
  return (reverse_sent)



sentence = input("Enter a sentence: ")
print(reverseWordOrder(sentence))
