import pandas as pd
from collections import defaultdict


def get_wine_sorts(file_path):
    excel_data_df = pd.read_excel(file_path, keep_default_na=False)
    wine_sorts = defaultdict(list)

    wine_bottles = excel_data_df.to_dict(orient='records')

    for bottle in wine_bottles:
        wine_sorts[bottle["Категория"]].append(
            defaultdict(
                str,
                {
                    "Название": bottle["Название"],
                    "Сорт": bottle["Сорт"],
                    "Цена": bottle["Цена"],
                    "Картинка": bottle["Картинка"],
                    "Акция": bottle["Акция"],
                }
            )
        )

    return wine_sorts
