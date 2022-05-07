import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from sklearn.metrics import confusion_matrix

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
    # Image for both Spam and ham words
    fig, (ax0,ax1) = plt.subplots(1,2,figsize = (30, 30), facecolor = None)
    ax0.imshow(spam_wordcloud)
    ax0.set_title("Spam Words",fontsize = 50)
    ax0.axis("off")
    ax1.imshow(ham_wordcloud)
    ax1.set_title("Ham Words",fontsize = 50)
    ax1.axis("off")

def plot_dist_classes(data):
    fig, ax = plt.subplots(1,1,figsize=(10,4))
    data.plot(kind='bar')
    ax.set_title("Distribution of Classes", fontsize=20)
    ax.set_ylabel("Frequency",fontsize=16)
    ax.set_xlabel("Classes",fontsize=16)
    
def plot_heatmap(y_valid,y_pred, labels, title):
    crosstab = pd.crosstab(y_valid, y_pred, rownames = ['Actual'], colnames =['Predicted'], margins = False)
    plt.figure() # Push new figure on stack
    htmap = sns.heatmap(crosstab,cbar=False,xticklabels=labels,yticklabels=labels,annot=True,fmt="d",cmap='Blues').set(title=title)
    plt.savefig(title+".png")

def plot_num_words_per_sms(num_words):
    fig, ax = plt.subplots()
    ax.hist(num_words, bins = 80)
    ax.set_title("Distribution of amount of words per SMS", fontsize=16)
    ax.set_ylabel("Words", fontsize=12)
    
def plot_acc(history_dict):
    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']
    epochs = range(1,len(acc)+1)
    plt.plot(epochs, acc, "bo", label="Training Acc")
    plt.plot(epochs, val_acc, "r", label="Validation Acc")
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    
def plot_loss(history_dict):
    val_loss = history_dict['val_loss']
    loss = history_dict['loss']
    epochs = range(1,len(loss)+1)
    plt.plot(epochs, loss, "bo", label="Training Loss")
    plt.plot(epochs, val_loss, "r", label="Validation Loss")
    plt.title("Training and Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()