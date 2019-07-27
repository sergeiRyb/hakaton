from nltk.corpus import stopwords
import re
import nltk
import pymorphy2

def preprocessing_data(string):
    stop_words = set(stopwords.words("russian"))
    
    # Change notwords on spaces
        
    pattern = r"[^\w]"
    string1=re.sub(pattern, " ", string).lower()
    
    # Delite stop words
    
    words = nltk.word_tokenize(string1)
    without_stop_words = [word for word in words if not word in stop_words]
    
    # Normalize to sting
    
    morph = pymorphy2.MorphAnalyzer()
    n_s = ''
    for word in without_stop_words:
        
        normal = morph.parse(word)[0].normal_form
        n_s = n_s + " " + normal
        # Delite first space
        normal_string = n_s[1:]
    return normal_string
