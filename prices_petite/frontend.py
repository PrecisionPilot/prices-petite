import webbrowser

from taipy.gui import Gui
import pandas as pd
from webscrapper import search_web_prices
from python import capture

user_query = ""
display_search_results = False
data = {"Vendor": [], "Price": [], "Description": [], "Url": []}
dataframe = pd.DataFrame.from_dict(data)
original_dataframe = dataframe
vendor_toggle_options = ["Show All", "Amazon CA", "Etsy", "Walmart", "Ebay", "AliExpress", "Other"]
selected_vendor = vendor_toggle_options[0]
page = """

# Prices Petite

Enter any product:

<|{user_query}|input|>
<|Search|button|on_action=on_button_action|>
<|Open Camera|button|on_action=on_capture_button|>

<|part|render={display_search_results}|
<|{dataframe}|table|>
<|{selected_vendor}|on_change=update_dataframe|toggle|lov={vendor_toggle_options}|>
|>

"""


def on_button_action(state):
    if state.user_query != "":
        new_dataframe = search_web_prices(state.user_query)
        state.dataframe = new_dataframe
        state.original_dataframe = new_dataframe
        state.display_search_results = True

def on_capture_button(state):
    state.user_query = capture()
    on_button_action(state)

def update_dataframe(state):
    state.dataframe = state.original_dataframe
    if state.selected_vendor == state.vendor_toggle_options[len(state.vendor_toggle_options) - 1]:
        for vendor in state.vendor_toggle_options:
            state.dataframe = state.dataframe.drop(state.dataframe[vendor in state.dataframe["Vendor"]].index)
    elif state.selected_vendor != state.vendor_toggle_options[0]:
        state.dataframe = state.dataframe.drop(state.dataframe[~state.dataframe["Vendor"].isin([state.selected_vendor])].index)



def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.user_query = ""
        return

stylekit = {
    "color_primary": "#9CEAEF",
    "color_secondary": "#746D75",
}

Gui(page, css_file="styles.css").run(stylekit=stylekit)