# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np
from PIL import Image

import streamlit as st
from streamlit.hello.utils import show_code



st.set_page_config(page_title="Appje", page_icon="📱")
st.markdown("# HELP, ik moet een appje sturen")
st.sidebar.markdown("**Selecteer je cursus.**")
st.write(
    """"""
)

col1, col2 = st.columns(2)

image = Image.open('./appjenotificatie.png')
with col1:
    st.image(image, width=300)
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write(
    """ 
        \n
        Hallo! De sint is blij om je hier te zien, \\
        Kan je mij helpen met al mijn appjes misschien? \\
        Zoals je kan zien, heb ik er namelijk nogal veel, \\
        Dan ga ik weer door met het lezen van de vele brieven op mijn mail!
    """
    )

st.warning('Je mag absoluut geen hulp krijgen, de pieten kijken mee!!', icon="⚠️")
st.info("Er zijn regels: \n 1. Wees snel. \n 2. Denk niet veel na. \n 3. Het is een appje, en geen mail. Wees kort en bondig.")
image = Image.open('./peer.png')

on = st.toggle('*Stap 1: Activeer als je de sint wilt helpen met de appjes!*', key='2')
if on:
    st.write(""" Vele appjes komen binnen per dag, \\
         Waar jij er nu een paar van beantwoorden mag.\\
         De eerste zal je wel bekend voorkomen, \\
         Laat die creativiteit maar stromen...
         """)
    st.image(image, width=300)
    text_input = st.text_input(
        "Schrijf je antwoord op Peer hier👇",)
on = st.toggle('*Stap 2: Activeer als je je appje hebt gestuurd*', key='1')
if on:
    st.write("""
        Gelukkig was dat niet al te moeilijk\\
        Maar zeker niet toch niet vermoeilijk (?) \\
        De rijm piet wordt nu wel een beetje moe, \\
        Maar we moeten nog wel wat appjes, poeh... 
         """)
    image = Image.open('./werk.png')
    st.image(image, width=300)
    text_input = st.text_input("Schrijf je antwoord op je collega hier👇",)
on = st.toggle('*Stap 3: Activeer als je het tweede appje ook achter de rug hebt*')
if on:
    st.write("""
        Dan misschien nog één appbericht,\\
        Ja, deze is zeker ook verplicht.\\
        Maar de sint is heel erg blij met jouw hulp,\\
        De kruip voor de laatste keer uit jouw *ik kan niet goed appen*-schulp!               
         """)
    image = Image.open('./fam.png')
    st.image(image, width=300)
    text_input = st.text_input("Schrijf je antwoord op ons (aka je fam) hier👇",)
on = st.toggle('*Stap 4: Activeer als je het laatste appje hebt verstuurd*')
if on:
    st.write("""
    Wat knap, ook je laatste appje zit erop!\\
    En wat waren je antwoorden toch top.\\
    Maar nee, nee je bent nog klaar,\\
    Je hebt namelijk nog een toets, dat is zeker waar.
    """
    )
  
    st.info("Ga nu naar de *Eindtoets* pagina")
