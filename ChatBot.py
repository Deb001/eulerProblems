import tensorflow as tf
import numpy as np
import re
import time

# import the dataset
lines = open('/Users/ddas/Downloads/cornell_movie/movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open('/Users/ddas/Downloads/cornell_movie/movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

# create dictionary
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

#create list of all conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversations_ids.append(_conversation.split(','))

#getting separate question and answers
questions = []
answers = []
for conversation in conversations_ids:
    for i in range (len(conversation) -1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])

#clean texts

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am",text)
    text = re.sub(r"don't", "do not",text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"cann't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|,.?]", "", text)
    return text

# cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))

# cleaning answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))

# creating a dictionary that maps each word to its number of occurence
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

# creating 2 dictionaries that map questions words and answer words to an unique integer
threshold = 20
questionswords2int = {}
word_number = 0

for word, count in word2count.items():
    if count >= threshold:
        questionswords2int[word] = word_number
        word_number += 1

answerswords2int = {}
word_number = 0

for word, count in word2count.items():
    if count >= threshold:
        answerswords2int[word] = word_number
        word_number += 1
print(answerswords2int)

# adding last tokens to the dictionaries
tokens = ['<PAD>','<EOS>', '<OUT>','<SOS>']
for token in tokens:
    questionswords2int[token] = len(questionswords2int) + 1
for token in tokens:
    answerswords2int[token] = len(answerswords2int) + 1

# inverse dictionary
answersints2word = {w_i:w for w, w_i in answerswords2int.items()}

#EOS token
for i in range(len(clean_answers)):
    clean_answers[i] += ' <EOS>'
