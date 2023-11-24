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

from typing import Any

import numpy as np

import streamlit as st
from PIL import Image



st.set_page_config(page_title="Powerpoint", page_icon="💻")

st.markdown("# Powerpoint maken")
st.write(
    """ Na je welverdiende rust, moet je weer vele powerpoints maken,\\
    Als kunstdocent bruis je natuurlijk met veel creatieve ideeën.\\
    Alleen besteed jij je tijd soms liever aan andere zaken,\\
    Het is daarom fijn dat de *designer* van powerpoint mooie ontwerpen kan displayen.

    Oh nee, helaas deze keer niet. \\
    Maar de tijd tikt helaas wel door... \\
    Teken een mooiere design voor de slide die je hieronder ziet. \\
    Doe dat op papier, je krijgt hier 5 minuten voor.

"""
)
st.sidebar.markdown("**Selecteer je cursus.**")
image = Image.open('./lege_powerpoint.png')
st.image(image)
on = st.toggle('*Stap 2: Activeer alleen als de powerpoint is goedgekeurd*', key='1')

if on:
    st.write("""
            Wat ziet de presentatie er mooi uit! \\
            Je vraagt je natuurlijk nu af wat de volgende stap is.\\
            Nu moet je de powerpoint opslaan voordat je hem sluit. \\
            Hopelijk gaat er nu niks mis...
             """)
    image = Image.open('./powerpoint_2.png')
    st.image(image)
    st.write("""
            Hoe sla je deze powerpoint op? \\
            Schrijf de stappen in de box hieronder. \\
            Hopelijk is je antwoord top! \\
            Je hebt 1 minuut, en met hulp moet je zonder... 
             """)
    text_input = st.text_input(
        "Schrijf je antwoord hier 👇",)
on1 = st.toggle('*Stap 3: Activeer alleen als je je powerpoint hebt opgeslagen*', key='2')
if on1:
    st.write("""
            Hopelijk heb je je powerpoint goed opgeslagen. \\
            Het juiste antwoord was: *Archief > Opslaan als...* \\
            Je hebt het vast goed gedaan, dus we gaan niet klagen. \\
            Maar hopelijk speel je niet vals. 
            
            Maar nu is het tijd voor het echte werk \\
            Want weet je waar je de mooie afbeeldingen kan vinden die je op de powerpoint ziet? \\
            Zoek ze op je computer, zo zijn je skills echt sterk. \\
            Meer dan 3 minuten heb je niet. 
            """)
on2 = st.toggle('*Stap 4: Activeer nadat je hebt laten zien je eigen designer kan zijn*', key='3')
if on2:
    st.write("""
            Nu je powerpoint onder de hand hebt, \\
            Gaan we nu verder naar hoe je appt. \\
            Selecteer nu de volgende cursus in het menu aan de linkerkant, \\
            Dan is er helemaal niks aan de hand. 
             """)

    