from taipy.gui import Gui
import pandas as pd
import scraping_test

user_query = ""
display_search_results = False
#data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
data = {"url_list": [], "price_list": [], "product_name_list": []}
#data2 = {'col_1': [24, 26, 331, 460], 'col_2': ['thtfgf', 'dfdgfhfh', 'sdsdsd', 'cvghytdf']}
dataframe = pd.DataFrame.from_dict(data)


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
    new_dataframe = scraping_test.search_web_prices("broom stick")
    print(new_dataframe)
    print(new_dataframe.dtypes)
    state.dataframe = new_dataframe
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

