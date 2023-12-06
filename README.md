# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка зависимостей

```
pip install -r requirements.txt
```

## Подготовка данных

Нужна таблица с информацей по винам, названием 
```
wine.xlsx
```
и следующим форматом:

| Категория    | Название            | Сорт            | Цена | Картинка                 | Акция                |
|--------------|---------------------|-----------------|------|--------------------------|----------------------|
| Белые вина   | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки      | Коньяк классический |                 | 350  | konyak_klassicheskyi.png |                      |
| Красные вина | Черный лекарь       | Качич           | 399  | chernyi_lekar.png        |                      |
| Красные вина | Хванчкара           | Александраули   | 550  | hvanchkara.png           |                      |
| Напитки      | Чача                |                 | 299  | chacha.png               | Выгодное предложение |
| Напитки      | Коньяк кизиловый    |                 | 350  | konyak_kizilovyi.png     |                      |

Пропуски игнорируются, сортировка данных в таблице не нужна.

## Запуск

- Скачайте код
- Запустите сайт командой 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
