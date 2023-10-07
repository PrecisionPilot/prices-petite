from taipy.gui import Gui
import pandas as pd

text = "Original text"

# Definition of the page
page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|Search|button|on_action=on_button_action|>

<|{dataframe}|table|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>


"""

def on_button_action(state):
    print(state.text)

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


dataframe = pd.DataFrame({"Text":[text, 'Other', 'Love'],
                          "Score Pos":[1, 1, 4],
                          "Score Neu":[2, 3, 1],
                          "Score Neg":[1, 2, 0],
                          "Overall":[0, -1, 4]})

Gui(page).run(use_reload=True)