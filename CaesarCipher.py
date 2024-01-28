import string

def main():
  sentence = input('Please enter the sentence to be ciphered: ').strip().lower().split(sep = ' ')
  print(sentence)
  plainToCipherText(sentence)
  cipherToPlainText()

def plainToCipherText(sentence):
  word_to_num = {word:num for num,word in enumerate(string.ascii_lowercase)}
  lst_of_num = []
  new_lst_of_num = []
  brand_new_lst_of_num = []
  for i in sentence:
    for j in i:
      if j in word_to_num:
        lst_of_num.append(word_to_num[j])
  print(lst_of_num)
  
  for i in lst_of_num:
    new_lst_of_num.append((i+3)%26)
  print(new_lst_of_num)

  for i in new_lst_of_num:
    brand_new_lst_of_num.append(list(word_to_num.keys())[list(word_to_num.values()).index(i)])
  print(brand_new_lst_of_num)

def cipherToPlainText():
  pass

main()