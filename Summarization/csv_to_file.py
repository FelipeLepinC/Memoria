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

app_name = 'wsp'

df = pd.read_csv(f'/Resultados/resultado_{app_name}.csv')

file = open(f'{app_name}.txt', "a")

for clase in range (11):
    file.write(label2id[clase]+'\n')
    file.write('\n')
    file.write('Riesgo \n')
    text_for_class = df[(df["class_group"] == clase) & (df["class_risk"] == 1)]['text']
    for text in text_for_class.values:
        file.write(text+'\n')
    file.write('\n')
    file.write('Sin riesgo : \n')
    text_for_class = df[(df["class_group"] == clase) & (df["class_risk"] == 0)]['text']
    for text in text_for_class.values:
        file.write(text+'\n')
    file.write('\n')

file.close()