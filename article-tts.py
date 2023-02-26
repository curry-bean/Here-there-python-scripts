'''
Text To Speech
-------------------------------------------------------------
pip install nltk newspaper3k gtts
'''


import nltk
from newspaper import Article
from gtts import gTTS


def text_to_speech(url):
   article = Article(url)
   article.download()
   article.parse()
   nltk.download('punkt')
   article.nlp()
   article_text = article.text
   language = 'en'
   my_obj = gTTS(text=article_text, lang=language, slow=False)
   my_obj.save("read_article.mp3")


if __name__ == '__main__':
   text_to_speech(
       url='https://hackr.io/blog/top-tech-companies-hiring-python-developers'
   )