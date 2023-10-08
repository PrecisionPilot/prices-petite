from taipy.gui import Gui
import pandas as pd
#import scraping_test

user_query = "Original text"
display_search_results = False
dataframe = pd.DataFrame({"Text":[user_query, 'Other', 'Love'],
                          "Score Pos":[1, 1, 4],
                          "Score Neu":[2, 3, 1],
                          "Score Neg":[1, 2, 0],
                          "Overall":[0, -1, 4]})

page = """

<|layout|columns=1 1|
<|
<|{user_query}|input|>

   
<|Search|button|on_action=on_button_action|>

<|part|render={display_search_results}|
<|{dataframe}|table|>
|>

|>

"""


def on_button_action(state):
    print(state.user_query)
    state.display_search_results = not state.display_search_results



def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.user_query = ""
        return


stylekit = {
  "color_primary": "#9CEAEF",
  "color_secondary": "#746D75",
}
Gui(page).run(stylekit=stylekit)

