# TopicClouds.py

############ Configuration ##########################
input_file_path = "C://Users/Scott/Documents/GitHub/d3-cloud/examples/topicCloud"
input_file = "word-topic-counts.txt"
num_top_words = 10
#####################################################
import numpy as np
import os
input_path = os.path.join(input_file_path, input_file)
num_topics = 100
mallet_vocab = []
word_topic_counts = []

with open(input_path) as f:
    for line in f:
        values = line.rstrip().split(' ')
        s = values[0]
        word =values[1]
        values[0:2] = []
        topic_count_pairs = [pair.split(':') for pair in values]
        mallet_vocab.append(word)
        counts = np.zeros(num_topics)
        for topic, count in topic_count_pairs:
            counts[int(topic)] = int(count)
        word_topic_counts.append(counts)
 
word_topic = np.array(word_topic_counts)

word_topic = word_topic / np.sum(word_topic, axis=0)

mallet_vocab = np.array(mallet_vocab)  # convert vocab from a list to an array so we can use NumPy operations on it

output_file = os.path.join(input_file_path, "dataset.js")
f = open(output_file,"w")
f.write("")
f.close()
f = open(output_file,"a")
f.write("var dataSet = [\n")
i = 1
for t in range(num_topics):
    top_words_idx = np.argsort(word_topic[:,t])[::-1]  # descending order
    top_words_idx = top_words_idx[:num_top_words]
    top_words = mallet_vocab[top_words_idx]
    top_words_shares = word_topic[top_words_idx, t]
    title = '{name: "topic'+str(t)+'",\n children: ['
    print(title)
    f.write(title+"\n")
    j = 1
    for word, share in zip(top_words, top_words_shares):
        if j == num_top_words:
            wordData = '\t{text: "' + word + '", size: ' + str(np.round(share, 3)) + '}'
        else:
            wordData = '\t{text: "' + word + '", size: ' + str(np.round(share, 3)) + '},'
        print(wordData)
        f.write(wordData+"\n")
        j = j+ 1
    if i == num_topics:
        close = " ]\n}"
    else:
        close =" ]\n},"
    print(close)
    f.write(close+"\n")
    i = i + 1
f.write("];")
f.close()