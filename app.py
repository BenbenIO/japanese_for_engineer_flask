from flask import Flask, render_template, url_for
import pandas as pd
import random

# Global variable
vocabulary = None
name = "Science"
app = Flask(__name__)

def load_vocabulary(wanted_vocabulary='Machine_Learning'):
    """
        Load the vocabulary dataframe into the global variable
        Args:
        - wanted_vocabulary: string of the name of the vocabulary list
    """
    global vocabulary, name
    name = wanted_vocabulary

    vocabulary = pd.read_excel(app.root_path + "/xls_files/" + name +'.xls', index=False)
    vocabulary.index += 1 
    vocabulary.columns = ['kanji', 'hiragana', 'english']
    vocabulary.style.set_properties(**{'text-align': 'center'})
    vocabulary.style.set_table_styles([dict(selector='td', props=[('text-align', 'center')]),])

@app.route('/')
def display_df_home():
    # Load the default dataframe in full answer mode
    global vocabulary, name

    load_vocabulary()
    return render_template('home.html', name = name, dataframe=vocabulary)

## Vocabulary set callback
@app.route('/select_Science')
def select_Science():
    # Selec the Science dataframe
    global vocabulary, name

    load_vocabulary("Science")
    return render_template('home.html', name = name, dataframe=vocabulary)

@app.route('/select_Embedded')
def select_Embedded():
    global vocabulary, name
    load_vocabulary("Embedded_Systems")
    return render_template('home.html', name = name, dataframe=vocabulary)

@app.route('/select_ML')
def select_ML():
    global vocabulary, name
    load_vocabulary("Machine_Learning")
    return render_template('home.html', name = name, dataframe=vocabulary)

@app.route('/select_General')
def select_General():
    global vocabulary, name
    load_vocabulary("General")
    return render_template('home.html', name = name, dataframe=vocabulary)

## Test mode callback
@app.route('/load_answer')
def load_answer():
    # Load the full dataframe
    global vocabulary, name
    modetitle = " (answer)"
    return render_template('home.html', name = name + modetitle, dataframe=vocabulary)

@app.route('/load_kanji')
def load_kanji():
    # Load the kanji test
    global vocabulary, name
    findkanji = vocabulary.copy()
    findkanji.kanji = " "
    print(findkanji.head())
    modetitle = " (kanji test)"
    return render_template('home.html', name = name + modetitle, dataframe=findkanji)

@app.route('/load_hiragana')
def load_hiragana():
    # Load the hiragana test
    global vocabulary, name
    findhiragana = vocabulary.copy()
    findhiragana.hiragana = " "
    modetitle = " (hiragana test)"
    return render_template('home.html', name = name + modetitle, dataframe=findhiragana)

@app.route('/load_english')
def load_english():
    # Load the english test
    global vocabulary, name
    findenglish = vocabulary.copy()
    findenglish.english = " "
    modetitle = " (english test)"
    return render_template('home.html', name = name + modetitle, dataframe=findenglish)

@app.route('/load_random')
def load_random():
    global vocabulary, name
    # Generate a random vector
    replace_vector = []
    dataframe_lenght = vocabulary.shape[0]
    for i in range(dataframe_lenght):
        replace_vector.append(random.randint(0,2))

    findrandom = vocabulary.copy()
    for i in range(dataframe_lenght):
        findrandom.iloc[i,replace_vector[i]] = " "

    modetitle = " (random test)"
    return render_template('home.html', name = 'science' + modetitle, dataframe=findrandom)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

