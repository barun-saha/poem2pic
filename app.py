import streamlit as st

from config import Config
from diffusion_image import generate_image_from_text
from t5_summary import generate_summary


st.write('''
# Poem2Pic: What picture does your poem paint?

Poetry is food for the soul. An image is worth a thousand words. 

With Poem2Pic, generate an image based on a very short summary of your poem!
''')

footer = """<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 2%;
    width: 100%;
    text-align: center;
    color: #696969;
    padding: 2px;
}
</style>
<div class="footer">
<p><small>Poem2Pic is an experimental project developed for fun. It is not really intended for professional use. 
Generating an image is an expensive process, so the image quality is kept low in the interest of time and cost. 
By using Poem2Pic you agree to fair, responsible, and sensible usage of the solution, platform, 
and the underlying AI models.</small></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

preload_text = ''

try:
    with open('examples/old_pond.txt', 'r', encoding='utf8') as in_file:
        preload_text = in_file.read().strip()
except Exception:
    pass

poem = st.text_area(
    f'''**Type or copy-paste a poem or start off with the following haiku 
    (max. {Config.LLM_MAX_INPUT_LENGTH} characters will be considered):**''',
    preload_text
)

if st.button('Generate image'):
    progress_text = 'Summarizing the poem...give it a moment'
    progress_bar = st.progress(0, text=progress_text)

    poem = poem.strip()
    input_length = len(poem)

    if input_length > 0:
        print(poem)

        target_length = min(input_length, Config.LLM_MAX_INPUT_LENGTH)
        summary = generate_summary(poem[:target_length])

        print(f'Summary: {summary}')
        st.write(f'''Summary: {summary}''')
        progress_bar.progress(10, text='Generating image...need a few more minutes')

        image = generate_image_from_text(summary)
        progress_bar.progress(100, text='Done!')

        st.image(image, caption=summary)
        st.info('Tip: Right-click on the image to save it')
