 #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
##Stop words with NLTK

#nltk packages are imported
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#create an example sentence
example_syntacticUnit = "In this example, I am going to show you how Natural Language Toolkit can filtr stop words."

#define a function to filter out stopwords
def filterOut_stopWords(example_syntacticUnit):

    filtered_stopWords = set(stopwords.words('english'))#create a variable to store set of stopwords in English

    tokened_words = word_tokenize(example_syntacticUnit) #create a variable to store tokenized words of the example above

    filtered_syntacticUnit = [] #create a variable for an empty list to store filtered stop words in English after looped through with the code below

    for lexicalUnit in tokened_words:
        if lexicalUnit not in filtered_stopWords:
            filtered_syntacticUnit.append(lexicalUnit)

#print the result
filtered=filterOut_stopWords(example_syntacticUnit)
print(filtered)
