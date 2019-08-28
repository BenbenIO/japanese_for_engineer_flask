from flask import Flask, render_template, url_for, send_file, abort, after_this_request
import pandas as pd
from weasyprint import HTML
import os, random

# Global variable
vocabulary = None
vocabulary_temp = None
name = "Science"
name_full = ""
app = Flask(__name__)

def load_vocabulary(wanted_vocabulary='Machine_Learning'):
    """
        Load the vocabulary dataframe into the global variable
        Args:
        - wanted_vocabulary: string of the name of the vocabulary list
    """
    global vocabulary, vocabulary_temp, name, name_full
    name = wanted_vocabulary
    name_full = ""

    vocabulary = pd.read_excel(app.root_path + "/xls_files/" + name +'.xls', index=False)
    vocabulary.index += 1 
    vocabulary.columns = ['kanji', 'hiragana', 'english']
    vocabulary.style.set_properties(**{'text-align': 'center'})
    vocabulary.style.set_table_styles([dict(selector='td', props=[('text-align', 'center')]),])
    vocabulary_temp = vocabulary

def render_name(name):
    """
        Render the name by deleting the _ between the name
        Args:
        - name string to render
    """
    title = ""
    words = name.split("_")
    for w in words:
        title = title + w + " "
    
    return(title.strip())

@app.route('/')
def display_df_home():
    # Load the default dataframe in full answer mode
    global vocabulary, name
    load_vocabulary()
    return render_template('home.html', name = render_name(name), dataframe=vocabulary)

## Vocabulary set callback
@app.route('/select_Science')
def select_Science():
    # Selec the Science dataframe
    global vocabulary, name
    load_vocabulary("Science")
    return render_template('home.html', name = render_name(name), dataframe=vocabulary)

@app.route('/select_Embedded')
def select_Embedded():
    # Selec the System_embedded dataframe
    global vocabulary, name
    load_vocabulary("Embedded_Systems")
    return render_template('home.html', name = render_name(name), dataframe=vocabulary)

@app.route('/select_ML')
def select_ML():
    # Selec the Machine Learning dataframe
    global vocabulary, name
    load_vocabulary("Machine_Learning")
    return render_template('home.html', name = render_name(name), dataframe=vocabulary)

@app.route('/select_General')
def select_General():
    # Selec the General dataframe
    global vocabulary, name
    load_vocabulary("General")
    return render_template('home.html', name = render_name(name), dataframe=vocabulary)

## Test mode callback
@app.route('/load_answer')
def load_answer():
    # Load the full dataframe
    global vocabulary, vocabulary_temp, name, name_full
    modetitle = " - answer"
    name_full = render_name(name) + modetitle
    vocabulary_temp = vocabulary
    return render_template('home.html', name = name_full, dataframe=vocabulary)

@app.route('/load_kanji')
def load_kanji():
    # Load the kanji test
    global vocabulary, vocabulary_temp, name, name_full
    findkanji = vocabulary.copy()
    findkanji.kanji = " "
    modetitle = " - kanji test"
    name_full = render_name(name) + modetitle
    vocabulary_temp = findkanji
    return render_template('home.html', name = name_full, dataframe=vocabulary_temp)

@app.route('/load_hiragana')
def load_hiragana():
    # Load the hiragana test
    global vocabulary, vocabulary_temp, name, name_full
    findhiragana = vocabulary.copy()
    findhiragana.hiragana = " "
    modetitle = " - reading test"
    name_full = render_name(name) + modetitle
    vocabulary_temp = findhiragana
    return render_template('home.html', name = name_full, dataframe=vocabulary_temp)

@app.route('/load_english')
def load_english():
    # Load the english test
    global vocabulary, vocabulary_temp, name, name_full
    findenglish = vocabulary.copy()
    findenglish.english = " "
    modetitle = " - english test"
    name_full = render_name(name) + modetitle
    vocabulary_temp = findenglish
    return render_template('home.html', name = name_full, dataframe=vocabulary_temp)

@app.route('/load_random')
def load_random():
    global vocabulary, vocabulary_temp, name, name_full
    # Generate a random vector
    replace_vector = []
    dataframe_lenght = vocabulary.shape[0]
    for i in range(dataframe_lenght):
        replace_vector.append(random.randint(0,2))

    findrandom = vocabulary.copy()
    for i in range(dataframe_lenght):
        findrandom.iloc[i,replace_vector[i]] = " "

    modetitle = " - random test"
    name_full = render_name(name) + modetitle
    vocabulary_temp = findrandom
    return render_template('home.html', name = name_full, dataframe=vocabulary_temp)

@app.route('/pdf_download')
def pdf_download():
    global vocabulary, vocabulary_temp, name, name_full
    print("DOWNLOAD")
    gen_html = render_template('pdf_template.html', name = name_full, dataframe=vocabulary_temp)
    temp_name = "temp_" + str(random.randint(0, 150)) + ".pdf"
    HTML(string=gen_html).write_pdf(temp_name)

    @after_this_request
    def delete_pdf(response):
        """
            Delete the generated zip file after download
        """
        if os.path.exists(temp_name):
            print("deleting {}".format(temp_name))
            os.remove(temp_name)
            print("DELETED")
        else:
            print("The file does not exist: {}".format(temp_name))
        return response

    try:
        response = send_file(temp_name, attachment_filename= name + "_test.pdf", as_attachment=True, cache_timeout=0)
        return response

    except FileNotFoundError:
        print("error")
        abort(404)


@app.route('/about')
def about():
    # Return the about - add vocabulary page
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
