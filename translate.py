import pandas as pd
from langdetect import detect
from deep_translator import GoogleTranslator

translate_count = 0

#simple function to detect and translate text 
def detect_and_translate(text,target_lang):
    try: 
        result_lang = detect(text)
    except:
        return text
        
    if result_lang == target_lang:
        return text 
    
    else:
        translate_text = GoogleTranslator(source='auto', target=target_lang).translate(text)

        global translate_count
        translate_count = translate_count + 1
        print('translate_count: ', translate_count)
        return translate_text 

data = pd.read_csv('../reviews.csv')
data.fillna('none', inplace=True)

for index, row in data['comments'].iteritems():
    res = detect_and_translate(row, 'en')
    data.loc[index, 'translated_comment'] = res
    print(index+1, " / 243184 completed")

data.to_csv('reviews_with_translations.csv')