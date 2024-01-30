import string

def main():
  sentence = input('Please enter the sentence to be ciphered: ').strip().lower()
  print(sentence)
  plainToCipherText(sentence)
  cipherToPlainText()

def plainToCipherText(sentence):
  word_to_num = {word:num for num,word in enumerate(string.ascii_lowercase)}
  word_to_num[' '] = 26
  print(word_to_num)
  lst_of_num = []
  new_lst_of_num = []
  brand_new_lst_of_num = []
  for i in sentence:
    if i in word_to_num:
      lst_of_num.append(word_to_num[i])
  print(lst_of_num)
  
  for i in lst_of_num:
    new_lst_of_num.append((i+3)%27)
  print(new_lst_of_num)

def cipherToPlainText():
  pass

main()