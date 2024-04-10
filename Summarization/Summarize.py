from transformers import pipeline
import pandas as pd

label2id = [
    'third_party_share_and_collection',
    'user_right_and_control',
    'specific_audiences',
    'data_security',
    'first_party_collection_and_use',
    'policy_change',
    'policy_contact_information',
    'international_data_transfer',
    'cookies_and_similar_technologies',
    'data_retention',
    'policy_introductory']

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

df = pd.read_csv("resultado_pytorch.csv")
    
file = open("Output.txt", "w")

for clase in range (11):
    print(label2id[clase])
    file.write(label2id[clase]+'\n')
    file.write('\n')
    file.write('Resumen : \n')

    texto_by_class = df[(df["class_group"] == clase) & (df["class_risk"] == 1)]['text'].values
    texto = "\n".join(texto_by_class)
    resumen = summarizer(texto, max_length=130, min_length=30, do_sample=False, truncation=True)
    file.write(resumen[0]['summary_text'] + '\n')
    file.write('\n')

# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
