import pandas as pd
from collections import defaultdict


def get_wine_sorts(file_path):
    excel_data_df = pd.read_excel(file_path, keep_default_na=False)
    wine_sorts = defaultdict(list)

    wine_bottles = excel_data_df.to_dict(orient='records')

    for bottle in wine_bottles:
        temp_dict = defaultdict(str)
        temp_dict["Название"] = bottle["Название"]
        temp_dict["Сорт"] = bottle["Сорт"]
        temp_dict["Цена"] = bottle["Цена"]
        temp_dict["Картинка"] = bottle["Картинка"]
        temp_dict["Акция"] = bottle["Акция"]
        wine_sorts[bottle["Категория"]].append(temp_dict)

    return wine_sorts
