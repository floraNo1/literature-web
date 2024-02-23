from bertopic import BERTopic
from umap import UMAP
from hdbscan import HDBSCAN
from bertopic.vectorizers import ClassTfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from transformers import T5Model
from transformers import AutoConfig
import pandas as pd
import re

config = AutoConfig.from_pretrained("./model/all-MiniLM-L6-v2/config.json")
embedding_model = T5Model.from_pretrained("./model/all-MiniLM-L6-v2", local_files_only=True)

data = pd.read_excel("./data/alldata.xls").astype(str)
dic_file = "./data/dict.txt"
stop_file = "./data/stop_words.txt"


# 数据清洗
def clean_text(mytext):
    stop_list = []
    try:
        with open(stop_file, encoding='utf-8') as stopword_list:
            stop_list = [line.strip() for line in stopword_list]
    except FileNotFoundError:
        print(f"Error: Stop file '{stop_file}' not found.")
    word_list = []
    words = re.findall(r'\b\w+\b', mytext)
    for word in words:
        word = word.lower()
        if word in stop_list or len(word) < 2:
            continue
        word_list.append(word)
    return " ".join(word_list)


umap_model = UMAP(n_neighbors=15, n_components=5,min_dist=0.0,metric='cosine')

hdbscan_model = HDBSCAN(min_cluster_size=10, metric='euclidean', prediction_data=True)

vectorizer_model = CountVectorizer(stop_words="english")
ctfidf_model = ClassTfidfTransformer()


topic_model = BERTopic(
    embedding_model=embedding_model,    # Step 1 - Extract embeddings
    umap_model=umap_model,              # Step 2 - Reduce dimensionality
    hdbscan_model=hdbscan_model,        # Step 3 - Cluster reduced embeddings
    vectorizer_model=vectorizer_model,  # Step 4 - Tokenize topics
    ctfidf_model=ctfidf_model,          # Step 5 - Extract topic words
    nr_topics='auto',
    top_n_words = 10
)

#处理数据
data["processed"] = data.Article_Title.apply(clean_text)
filtered_text = data["processed"].tolist()
topic_model = topic_model.fit(filtered_text)
topic_model.save("my_model")
topics, probabilities = topic_model.fit_transform(filtered_text)


#可视化
# image = topic_model.visualize_hierarchy()
# image = topic_model.visualize_heatmap()
# image = topic_model.visualize_topics()
# topic_model.get_topic_freq()
# topic_0 = topic_model.get_topic(0)
# image = topic_model.visualize_barchart()
# image.show()
