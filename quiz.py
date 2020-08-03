import random

def get_def_and_pop(word_list, word_dict):
    rand = random.randrange(len(word_list))
    word = word_list.pop(rand)
    definition = word_dict.get(word)
    return word, definition

def getWordandDef(rawstring):
    word, definition = rawstring.split(',', 1)
    return word, definition

fh = open("Vocabulary_list.csv", "r")
wd_list = fh.readlines()

wd_list.pop()
wd_set = set(wd_list)
fh = open("Vocabulary_set.csv", "w")
fh.writelines(wd_set)

word_dict = dict()
for rawstring in wd_set:
    word,definition = getWordandDef(rawstring)
    word_dict[word] = definition

while True:
	wd_list = list(word_dict)#will gave us list of keys		f
	choice_list = []#first of all we will create the empty choice_list
	for x in range(4):#we will create 4 choices	
		word, defination = get_def_and_pop(wd_list, word_dict)
		choice_list.append(defination)
	#shuffle the choices
	random.shuffle(choice_list)	#y
	print(word)#gave word and they will chose defination correct
	print("-------------")
	for idx, choice in enumerate(choice_list):
		print(idx+1, choice)
	choice = int(input("Enter 1,2,3,4; 0 to exit"))
	if choice_list[choice-1] == defination:
		print("Correct!\n")
	elif choice == 0:
		exit(0)
	else:
		print("Incorrect\n")


