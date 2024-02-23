from flask import Blueprint
from flask import render_template
import pandas as pd
import re
from bertopic import BERTopic


bp = Blueprint("analysis", __name__, url_prefix="/analysis")

data = pd.read_excel("./data/alldata.xls").astype(str)
dic_file = "./data/dict.txt"
stop_file = "./data/stop_words.txt"


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


data["processed"] = data.Article_Title.apply(clean_text)
filtered_text = data["processed"].tolist()

loaded_model = BERTopic.load("my_model")
loaded_model = loaded_model.fit(data["processed"])


@bp.route("/result_freq")
def bertopic_analysis_freq():
    topic_freq = loaded_model.get_topic_freq()
    table_html = topic_freq.to_html(classes='table table-striped', index=False)
    return render_template('bertopic_result.html', table=table_html)



@bp.route("/result_info")
def bertopic_analysis_topic_info():
    topics, probabilities = loaded_model.fit_transform(filtered_text)
    document_info = loaded_model.get_document_info(filtered_text)
    table_html1 = document_info.to_html(classes='table table-striped', index=False)
    return render_template('bertopic_result.html', table=table_html1)





@bp.route("/result_image")
def bertopic_analysis_topic_image():
    return render_template('bertopic_image.html')


