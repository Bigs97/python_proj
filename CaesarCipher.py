import string

word_to_num = {word:num for num,word in enumerate(string.ascii_lowercase)}

def main():
  sentence = input('Please enter the sentence to be ciphered: ').strip().lower()
  plainToCipherText(sentence)
  cipherToPlainText()

def plainToCipherText(sentence):
  brand_new_lst_of_num = []
  lst_of_num = [word_to_num[i] for i in sentence if i in word_to_num]
  lst_of_num = [(i+3)%26 for i in lst_of_num]
  # for alpha, nums in word_to_num.items():
  #   if nums in word_to_num.values():
  #     brand_new_lst_of_num.append(alpha)
    
  # print(brand_new_lst_of_num)
  # print(brand_new_lst_of_num)
  # return new_lst_of_num

def cipherToPlainText():
  pass
  # num_to_word = dict([values,keys] for keys, values in word_to_num.items())
  # num_to_word = {values:keys for keys, values in word_to_num.items()}
  
  # print(num_to_word)

main()
