import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer

class CrearSentiment(BaseEstimator, TransformerMixin):
    #Acepta como parámetro la columna a partir de la cual crear el sentiment (ej: Score o Rating) y el mínimo score para considerar el sentiment como positivo. Al sentiment positivo le asigna 0, al sentiment negativo le asigna 1.
    def __init__(self,columna_a_transformar,minimo):
        self.columna_a_transformar = columna_a_transformar
        self.minimo = minimo

    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        X["Sentiment"]=X[self.columna_a_transformar]>self.minimo
        X["Sentiment"]=X["Sentiment"].apply(lambda x: 0 if x else 1)
        return X



class DropDuplicated(BaseEstimator, TransformerMixin):
    #Acepta como parámetro las columnas a partir de las cuales considerar registros como duplicados.
    def __init__(self,columnas_decision):
        self.columnas_decision = columnas_decision

    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        X=X.drop_duplicates(subset=self.columnas_decision)
        return X


class FillNa(BaseEstimator, TransformerMixin):
    #Acepta como parámetro una columna del dataframe para rellenar, y con qué rellenarla. Se aplica primero.
    def __init__(self,relleno,columna_a_rellenar):
        self.relleno = relleno
        self.columna_a_rellenar=columna_a_rellenar
    
    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        return pd.concat([X[self.columna_a_rellenar].fillna(value=self.relleno),X.drop(self.columna_a_rellenar,axis=1)],axis=1) 

        # X[self.columna_a_rellenar].fillna(value=self.relleno,inplace=True)
        # return X



class UnirColumnas(BaseEstimator, TransformerMixin):
    #Acepta como parámetro las columnas a unir.
    def __init__(self,columna1,columna2):
        self.columna1 = columna1
        self.columna2 = columna2

    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
#        X[self.columna1+' '+self.columna2]=X[self.columna1]+ " " + X[self.columna2]
         X.loc[:,self.columna1+' '+self.columna2]=X[self.columna1]+ " " + X[self.columna2]
         return pd.DataFrame(X)



class FeatureSelection(BaseEstimator, TransformerMixin):
    def __init__(self,selected_features):
        self.selected_features=selected_features

    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        return X[self.selected_features]



def stemfrases(frase):    
    token_words=word_tokenize(frase)
    stem_sentence=[]    
    englishStemmer=SnowballStemmer("english")
    for word in token_words:
        stem_sentence.append(englishStemmer.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)



class Stemmer_English(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        return X.apply(lambda x: stemfrases(x))



