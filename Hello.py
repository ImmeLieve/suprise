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

    st.write("# Een brief van de hulp pieten 🎅🎁")

    st.sidebar.markdown("**Selecteer je cursus.**")
    st.markdown('''
    *Lieve Hanneke,*

    De hulp piet hoorde dat je de laatste tijd veel rust neemt, \\
    Dat vonden de sint en zijn pieten wel wat vreemd. \\
    Je staat namelijk niet bekend als een zen persoon. \\
    Hun baasje druk bezig zien zijn vonden Jut en Aug inmiddels wel gewoon.

    Nu is er altijd wel iemand thuis om hun aandacht te geven,\\
    Ze hebben inmiddels al gedag gezegd tegen hun rustige leven.\\
    Om het het nog erger te maken voor hen,\\
    wordt het huis nu ook verbouwd… daar gaat hun zen…

    Gelukkig helpen ze graag met de keuzes die gemaakt moeten worden \\
    Ze maken van jouw creatieve chaos een orde.\\
    Wat ze helaas iets te ver gaat,\\
    Is het geven van digitale raad.

    Whatsappjes, mailen en belletjes vinden ze maar raar,\\
    Waarom maken baasjes hun leven vrijwillig zo zwaar?\\
    Daarom hebben ze de pieten ingelicht,\\
    want elke keer als je begint over een appje klappen ze dicht.

    De pieten hebben lang naar het probleem gekeken,\\
    Maar ze snapte er ook helemaal niks van en zijn toen bij de IT piet staan smeken.\\
    Die keek naar het probleem, maar zag er geen…\\
    Maar blijkbaar was hij daarin alleen.

    De IT piet ging daarom dus aan de slag,\\
    Want hij heeft maar zo veel uren in de dag.\\
    Een digitale tool lijkt de uitkomst,\\
    Die gebruikt kan worden door iemand zonder digitale afkomst.

    De digitale wereld moet namelijk je leven makkelijker maken,\\
    Zodat jij meer tijd hebt voor stressen over het huis, nieuwe relaties en dekens haken.\\
    Dus laten we beginnen met het leren,\\
    En jij deze onnodige IT stress kan peren.
                
    **Dus....**

    Welkom bij de jouw hoog nodige spoedcursus *"Hoe moet ik **zelfstandig** met de computer omgaan?"*!
    
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
