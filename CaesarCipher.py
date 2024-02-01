import string

word_to_num = {word:num for num,word in enumerate(string.ascii_lowercase)}
print(word_to_num)
# word_to_num[' '] = 26

def main():
  sentence = input('Please enter the sentence to be ciphered: ').strip().lower()
  print(sentence)
  plainToCipherText(sentence)
  cipherToPlainText()

def plainToCipherText(sentence):
  lst_of_num = []
  new_lst_of_num = []
  brand_new_lst_of_num = []
  for i in sentence:
    if i in word_to_num:
      lst_of_num.append(word_to_num[i])
  print(lst_of_num)
  
  for i in lst_of_num:
    new_lst_of_num.append((i+3)%26)
  print(new_lst_of_num)

  for i in new_lst_of_num:
    if i in word_to_num.values():
      brand_new_lst_of_num.append(word_to_num)
  # return new_lst_of_num

def cipherToPlainText():
  pass
  # num_to_word = dict([values,keys] for keys, values in word_to_num.items())
  # num_to_word = {values:keys for keys, values in word_to_num.items()}
  
  # print(num_to_word)

main()
