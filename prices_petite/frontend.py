from taipy.gui import Gui
import pandas as pd
import webscrapper

user_query = ""
display_search_results = False
data = {"Vendor": [], "Price": [], "Description": [], "Url": []}
dataframe = pd.DataFrame.from_dict(data)


page = """

# Prices Petite

Enter any product:

<|{user_query}|input|>
<|Search|button|on_action=on_button_action|>

<|part|render={display_search_results}|
<|{dataframe}|table|>
|>

"""


def on_button_action(state):
    if state.user_query != "":
        new_dataframe = webscrapper .search_web_prices(state.user_query)
        state.dataframe = new_dataframe
        state.display_search_results = True

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.user_query = ""
        return

stylekit = {
    "color_primary": "#9CEAEF",
    "color_secondary": "#746D75",
}
Gui(page).run(stylekit=stylekit)

