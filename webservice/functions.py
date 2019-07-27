# import section

# функция, которая по id, полученным от сервиса Романа, вытаскивает ответы из
# MS SQL и возвращает json структуру, которая будет рендерится на клиенте
def get_final_answer(list_id):
    # TODO Валера
    pass

# функция, которая по строке поиска, полученной с клиента возвращает "чистые" данные,
# которые потом предаются в сервис Романа. На выходе строка.
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
   

