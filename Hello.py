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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Surprise Mama",
        page_icon="🎁",
    )

    st.write("# Surprise Mama! 🎅🎁")

    st.sidebar.markdown("Selecteer je cursus.")
    st.markdown('''
    Hoi Mama,\n
    Welkom bij de jouw hoog nodige spoedcursus *"Hoe moet ik **zelfstandig** met de computer omgaan?"*

    Deze surprise bestaat uit verschillende delen: \n
    1. Hoe werkt powerpoint? 
    2. Hoe schrijf ik een appje?
    3. Hoe ruim ik mijn mail op?

    Uiteindelijk is de bedoeling dat je zonder de hulp van je lieve dochter (Imme) en je secretaris (Marc) de digitale wereld aan kan. 

    Laten we beginnen met hoeveel je nu over jouw computerskills denkt: ''')
    minimum = 1
    maximum = 10
  
    st.slider("Ik kan zelfstand een mooie powerpoint maken", minimum, maximum, key="pp")
    st.slider("Ik kan zelfstandig een appje sturen", minimum, maximum, key="appje")
    st.slider("Ik heb een opgeruimde mail box", minimum, maximum, key="mail")
    st.slider("Ik heb geen moeite om zelfstandig taken uit te voeren op de computer", minimum, maximum, key="com")               
                

if __name__ == "__main__":
    run()
