from gensim.models import Word2Vec, KeyedVectors
import pandas as pd
import nltk
import csv


csv_file = 'C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\dataset\\LSMDC - short\\LSMDC16_annos_training.csv'
df = pd.read_csv(csv_file, delimiter = '\t', usecols = [5])

txt_file = open("video_caption.txt","w+")

with open(csv_file, "r", ) as csvfile:
    bookings = csv.reader(csvfile, delimiter='\t')
    for row in bookings:
        txt_file.write(row[5] + '\n')

txt_file.close()

video_caption_txt = 'C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\cv38\\densevid_eval-master\\video_caption.txt'

file_content = open(video_caption_txt).read()
video_caption = nltk.word_tokenize(file_content)
model = Word2Vec(video_caption, min_count = 2, size = 150)
print(model.most_similar('he'))

