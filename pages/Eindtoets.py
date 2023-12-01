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

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code
from quiz_data import quiz_data

st.set_page_config(page_title="Eindtoets", page_icon="🧮")
st.markdown("# Eindtoets")
st.sidebar.markdown("**Selecteer je cursus.**")
def show_question():
        question = quiz_data[st.session_state.current_question] 
        st.write(question['question']) # Selects the question within the dictionary being accessed by previous line within the quiz_data list.
        selected_choice = st.radio("Selecteer het juiste antwoord:", question['choices']) 
        submit_button = st.button("Lever in", key = str(question))
        if submit_button:
            check_answer(selected_choice)
            #st.session_state.show_question = False

# Function to check the selected answer and provide feedback
def check_answer(selected_choice):
        question = quiz_data[st.session_state.current_question]
        if selected_choice == question["answer"]:
            st.write("Juist!")
            st.balloons()
            st.session_state.score += 1
        else:
            st.write("Fout!")
            st.write("Het juiste antwoord was:", question["answer"])
        next_question()

    # function to move onto the next question
def next_question():
        current_question = st.session_state.current_question + 1
        if current_question < len(quiz_data): 
            st.session_state.current_question = current_question 
            show_question()
        else:
            st.session_state.show_question = False
            end_score()
            
def end_score():
        end_score = st.session_state.score
        st.success("Klaar met de quiz! Je score is: {}/{}".format(end_score, len(quiz_data)))
        st.write("Ja het heeft zeker iets te maken met je cadeau! Nu je straks veel meer vrije tijd hebt doordat je digitale skills zo erg verbeterd zijn, is het tijd voor een nieuwe hobby! \n Je mag nu je cadeau openen!")
    # Main function - initialising the 3 session state variables.
def main():
        st.write("""
            Je kan nu goed appen en wat ziet de presentatie er mooi uit! \\
            Je vraagt je natuurlijk nu af wat de volgende stap is.\\
            Dat is natuurlijk een leuke quiz!! \\
            Die hopelijk je grote kennis aanduid...
             """)
        st.warning('Helaas is de rijm piet nu een beetje moe, dus de rijmen eindigen "noe"!', icon="⚠️")
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0 
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'show_question' not in st.session_state:
            st.session_state.show_question = True

        if st.session_state.show_question:
             show_question()
        else:
             end_score()

if __name__ == "__main__":
        main()



