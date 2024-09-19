# Importing Libraries
# author:@aliicemill
import nltk
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import stylecloud

# Downloading word clusters
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_and_create_stylecloud(file_path, output_name='stylecloud.png', 
                                     icon_name='fas fa-laptop', lang='english'):
    # read file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # represent stopwords
    stop_words = set(stopwords.words(lang))

    # Remove punctuation marks
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Tokenize the text and convert to lowercase
    tokens = word_tokenize(text.lower(), language=lang)

    # Filter out stopwords
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Join filtered tokens
    processed_text = ' '.join(filtered_tokens)

    # Create StyleCloud
    stylecloud.gen_stylecloud(text=processed_text,
                              icon_name=icon_name,
                              output_name=output_name)
    # Show the generated StyleCloud
    im = Image.open(output_name)
    plt.figure(figsize=(10, 10))
    plt.imshow(im)
    plt.axis('off')  # Hide axes
    plt.show()

def create_stylecloud(text, language, icon):
    output_file = "stylecloud.png"
    
    stylecloud.gen_stylecloud(text=text,
                              icon_name=icon,
                              output_name=output_file)
    
    return output_file

st.title("WordCloud Creator")

file = st.file_uploader("Import txt file", type=["txt"])

if file is not None:
    text = file.getvalue().decode("utf-8")
    
    language = st.radio("Language", ["tr", "en","fr","de","es"])
    
    icon_options = ['fa-address-book', 'fa-address-card', 'fa-angry', 'fa-arrow-alt-circle-down', 'fa-arrow-alt-circle-left',
'fa-arrow-alt-circle-right', 'fa-arrow-alt-circle-up', 'fa-bell', 'fa-bell-slash', 'fa-bookmark', 'fa-building',
'fa-calendar', 'fa-calendar-alt', 'fa-calendar-check', 'fa-calendar-minus', 'fa-calendar-plus', 'fa-calendar-times',
'fa-caret-square-down', 'fa-caret-square-left', 'fa-caret-square-right', 'fa-caret-square-up', 'fa-chart-bar',
'fa-check-circle', 'fa-check-square', 'fa-circle', 'fa-clipboard', 'fa-clock', 'fa-clone', 'fa-closed-captioning',
'fa-comment', 'fa-comment-alt', 'fa-comment-dots', 'fa-comments', 'fa-compass', 'fa-copy', 'fa-copyright', 'fa-credit-card',
'fa-dizzy', 'fa-dot-circle', 'fa-edit', 'fa-envelope', 'fa-envelope-open', 'fa-eye', 'fa-eye-slash', 'fa-file',
'fa-file-alt', 'fa-file-archive', 'fa-file-audio', 'fa-file-code', 'fa-file-excel', 'fa-file-image', 'fa-file-pdf',
'fa-file-powerpoint', 'fa-file-video', 'fa-file-word', 'fa-flag', 'fa-flushed', 'fa-folder', 'fa-folder-open', 'fa-frown',
'fa-frown-open', 'fa-futbol', 'fa-gem', 'fa-grimace', 'fa-grin', 'fa-grin-alt', 'fa-grin-beam', 'fa-grin-beam-sweat',
'fa-grin-hearts', 'fa-grin-squint', 'fa-grin-squint-tears', 'fa-grin-stars', 'fa-grin-tears', 'fa-grin-tongue',
'fa-grin-tongue-squint', 'fa-grin-tongue-wink', 'fa-grin-wink', 'fa-hand-lizard', 'fa-hand-paper', 'fa-hand-peace',
'fa-hand-point-down', 'fa-hand-point-left', 'fa-hand-point-right', 'fa-hand-point-up', 'fa-hand-pointer', 'fa-hand-rock',
'fa-hand-scissors', 'fa-hand-spock', 'fa-handshake', 'fa-hdd', 'fa-heart', 'fa-hospital', 'fa-hourglass', 'fa-id-badge',
'fa-id-card', 'fa-image', 'fa-images', 'fa-keyboard', 'fa-kiss', 'fa-kiss-beam', 'fa-kiss-wink-heart', 'fa-laugh',
'fa-laugh-beam', 'fa-laugh-squint', 'fa-laugh-wink', 'fa-lemon', 'fa-life-ring', 'fa-lightbulb', 'fa-list-alt',
'fa-map', 'fa-meh', 'fa-meh-blank', 'fa-meh-rolling-eyes', 'fa-minus-square', 'fa-money-bill-alt', 'fa-moon',
'fa-newspaper', 'fa-object-group', 'fa-object-ungroup', 'fa-paper-plane', 'fa-pause-circle', 'fa-play-circle',
'fa-plus-square', 'fa-question-circle', 'fa-registered', 'fa-sad-cry', 'fa-sad-tear', 'fa-save', 'fa-share-square',
'fa-smile', 'fa-smile-beam', 'fa-smile-wink', 'fa-snowflake', 'fa-square', 'fa-star', 'fa-star-half', 'fa-sticky-note',
'fa-stop-circle', 'fa-sun', 'fa-surprise', 'fa-thumbs-down', 'fa-thumbs-up', 'fa-times-circle', 'fa-tired', 'fa-trash-alt',
'fa-user', 'fa-user-circle', 'fa-window-close', 'fa-window-maximize', 'fa-window-minimize', 'fa-window-restore']
    icon_options = list(map(lambda x : "fas "+x,icon_options))

    icon = st.selectbox("Icon Selection", icon_options, index=1)
    
    if st.button("Create"):
        output_file = create_stylecloud(text, language, icon)
        st.success(f"Here is your file: {output_file}")

        image = Image.open(output_file)
        st.image(image, caption='WordCloud', use_column_width=True)
        
        with open(output_file, "rb") as file:
            btn = st.download_button(
                label="Download WordCloud",
                data=file,
                file_name=output_file,
                mime="image/png"
            )