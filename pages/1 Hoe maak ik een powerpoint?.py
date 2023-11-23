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
    Doe dat op papier, je krijgt hier 2 minuten voor.

"""
)
st.sidebar.markdown("**Selecteer je cursus.**")
image = Image.open('/workspaces/suprise/lege_powerpoint.png')
st.image(image)
on = st.toggle('*Activeer alleen als de powerpoint is goedgekeurd*')

if on:
    
    st.write("""
            Wat ziet de presentatie er mooi uit! \\
            Je vraagt je natuurlijk nu af wat de volgende stap is.\\
            Dat is natuurlijk een leuke quiz!! \\
            Die hopelijk je grote kennis aanduid...
             """)


    