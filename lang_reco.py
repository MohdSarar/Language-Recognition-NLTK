import nltk

#importing stop words library (or not library !)

nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk import word_tokenize

#langues reconnues par python stopwords

language = ['turkish', 'tajik', 'swedish', 'spanish', 'slovene', 'russian', 'romanian', 'portuguese', 'norwegian', 'nepali', 'kazakh', 'italian', 'indonesian', 'hungarian', 'greek', 'german', 'french', 'finnish', 'english', 'dutch', 'danish', 'azerbaijani', 'arabic']
potentiel = []
reconnu = []
dico = {}
def reclangue() :
    text = str(input('type here '))
    tokenizedtxt = word_tokenize(text)
    for lang in language : 
        stpwrs = (stopwords.words(lang))
        for word in tokenizedtxt : 
            if word in stpwrs : 
                potentiel.append(lang)
    for lng in potentiel : 
        if lng not in reconnu :
            reconnu.append(lng)
        
    for lng in reconnu : 
        cal = potentiel.count(lng)
        dico[lng] = cal
        dict(sorted(dico.items(), key=lambda item: item[1]))
    
    return print(max(dico, key=dico.get)) 

reclangue()
