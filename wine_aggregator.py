import pandas as pd
from collections import defaultdict


def get_wine_dict():
    excel_data_df = pd.read_excel('wine3.xlsx', keep_default_na=False)
    wine_data = defaultdict(list)

    wine_dicts = excel_data_df.to_dict(orient='records')

    for item in wine_dicts:
        temp_dict = defaultdict(str)
        temp_dict["Название"] = item["Название"]
        temp_dict["Сорт"] = item["Сорт"]
        temp_dict["Цена"] = item["Цена"]
        temp_dict["Картинка"] = item["Картинка"]
        temp_dict["Акция"] = item["Акция"]
        wine_data[item["Категория"]].append(temp_dict)

    return wine_data
