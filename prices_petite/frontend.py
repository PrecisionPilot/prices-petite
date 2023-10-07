from taipy.gui import Gui
import pandas as pd

text = "Original text"
buttonPressed = False
dataframe = ""

searchPage = """
<|{text}|input|>

<|Search|button|on_action=on_button_action|>

<|{dataframe}|table|>

"""

resultPage = """
# Getting started with Taipy GUI

<|{dataframe}|table|>
"""


def on_button_action(state):
    print(state.text)
    state.

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


dataframe = pd.DataFrame({"Text":[text, 'Other', 'Love'],
                          "Score Pos":[1, 1, 4],
                          "Score Neu":[2, 3, 1],
                          "Score Neg":[1, 2, 0],
                          "Overall":[0, -1, 4]})

Gui(searchPage).run(use_reload=True)

