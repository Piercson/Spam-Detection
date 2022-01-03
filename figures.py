import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def plot_wordclouds(spam_words,ham_words):
    stopwords = set(STOPWORDS)
    spam_wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(spam_words)
    ham_wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(ham_words)
    fig, (ax0,ax1) = plt.subplots(1,2,figsize = (30, 30), facecolor = None)
    ax0.imshow(spam_wordcloud)
    ax0.set_title("Spam Words",fontsize = 50)
    ax0.axis("off")
    ax1.imshow(ham_wordcloud)
    ax1.set_title("Ham Words",fontsize = 50)
    ax1.axis("off")