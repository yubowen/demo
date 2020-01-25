# utf-8
import numpy as np
import tensorflow as tf
import sys
import os
import json
import jieba

# save word_vec_mat and word2id
processed_data_dir = "_processed_data\\data\\nyt"
word_vec_name_prefix = "word_vec"
word2id = json.load(open(os.path.join(processed_data_dir, word_vec_name_prefix + '_word2id.json'), 'r'))

UNK = word2id['UNK']
BLANK = word2id['BLANK']

def seg_cut(sentence,head,tail):
    s1 = jieba.cut(sentence)
    jieba.suggest_freq((head,tail), tune=True)
    s = list(s1)
    if head in s and tail in s:
        return s
    h1 = sentence.find(head)
    t1 = sentence.find(tail)
    if t1 > h1:
        seg1 = list(jieba.cut(sentence[:h1]))
        h2 = h1 + len(head)
        seg2 = list(jieba.cut(sentence[h2:t1]))
        t2 = t1 + len(tail)
        seg3 = list(jieba.cut(sentence[t2:]))
        seg1.append(head)
        seg1.extend(seg2)
        seg1.append(tail)
        seg1.extend(seg3)
        return seg1
    else:
        t1 = sentence.find(head)
        h1 = sentence.find(tail)
        seg1 = list(jieba.cut(sentence[:h1]))
        h2 = h1 + len(head)
        seg2 = list(jieba.cut(sentence[h2:t1]))
        t2 = t1 + len(tail)
        seg3 = list(jieba.cut(sentence[t2:]))
        seg1.append(head)
        seg1.extend(seg2)
        seg1.append(tail)
        seg1.extend(seg3)
        return seg1 

def evaluate_line(s,head,tail):
	max_length = 120
	data_word = np.zeros((max_length), dtype=np.int32)
	data_pos1 = np.zeros((max_length), dtype=np.int32)
	data_pos2 = np.zeros((max_length), dtype=np.int32)
	data_mask = np.zeros((max_length), dtype=np.int32)

	sentence = " ".join(seg_cut(s,head,tail))
	words = sentence.split()

	p1 = sentence.find(' ' + head + ' ')
	p2 = sentence.find(' ' + tail + ' ')
	if p1 == -1:
	    if sentence[:len(head) + 1] == head + " ":
	        p1 = 0
	    elif sentence[-len(head) - 1:] == " " + head:
	        p1 = len(sentence) - len(head)
	    else:
	        p1 = 0 # shouldn't happen
	else:
	    p1 += 1
	if p2 == -1:
	    if sentence[:len(tail) + 1] == tail + " ":
	        p2 = 0
	    elif sentence[-len(tail) - 1:] == " " + tail:
	        p2 = len(sentence) - len(tail)
	    else:
	        p2 = 0 # shouldn't happen
	else:
	    p2 += 1

	cur_ref_data_word = data_word  
	cur_pos = 0
	pos1 = -1
	pos2 = -1
	for j, word in enumerate(words):
	    if j < max_length:
	        if word in word2id:
	            cur_ref_data_word[j] = word2id[word]
	        else:
	            cur_ref_data_word[j] = UNK
	    if cur_pos == p1:
	        pos1 = j
	        p1 = -1
	    if cur_pos == p2:
	        pos2 = j
	        p2 = -1
	    cur_pos += len(word) + 1
	for j in range(j + 1, max_length):
	    cur_ref_data_word[j] = BLANK
	data_length = len(words)
	if len(words) > max_length:
	    data_length = max_length
	if pos1 == -1 or pos2 == -1:
	    raise Exception("[ERROR] Position error, index = {}, sentence = {}, head = {}, tail = {}".format(i, sentence, head, tail))
	if pos1 >= max_length:
	    pos1 = max_length - 1
	if pos2 >= max_length:
	    pos2 = max_length - 1
	pos_min = min(pos1, pos2)
	pos_max = max(pos1, pos2)
	for j in range(max_length):
	    data_pos1[j] = j - pos1 + max_length
	    data_pos2[j] = j - pos2 + max_length
	    if j >= data_length:
	        data_mask[j] = 0
	    elif j <= pos_min:
	        data_mask[j] = 1
	    elif j <= pos_max:
	        data_mask[j] = 2
	    else:
	        data_mask[j] = 3

	dic = {}
	dic["word"] = data_word.reshape(1,-1)
	dic["pos1"] = data_pos1.reshape(1,-1)
	dic["pos2"] = data_pos2.reshape(1,-1)
	dic["mask"] = data_mask.reshape(1,-1)
	dic["rel"] = np.array([0])
	dic["ins_rel"] = np.array([0])
	dic["scope"] = np.array([[0,1]])
	dic["length"] = np.array([len(word)])
	if len(word) > max_length:
	    dic["length"] = np.array([max_length])

	return dic