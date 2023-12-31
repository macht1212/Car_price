# Анализ объявлений о продаже автомобилей с сайта drom.ru с целью построения регрессионной модели для предсказания стоимости автомобиля  

## Введение

Идея создания модели появилась в процессе изучения курса машинного обучения для тренировки навыков, полеченных в процессе обучения.  
Часто при продаже автомобиля, многие автовладельцы ставят стоимость своего автомобиля не совсем корректно, то есть либо выше рынка, либо ниже.
Использование модели регрессии, которая была предобучена на достаточно большом датасете, который позволяет собрать сайт (примерно 2000 объявлений), 
должно помочь с пониманием средней стоимости автомобиля.

## Получение данных
Данные были получены из открытых источников, а именно с сайта drom.ru при помощи написанного самолично парсера с использованием библиотек requests и beautifulsoup4.
Данные сохранялись в файл с расширением .csv и названием, включающим в себя дату парсинга. Парсились данные легковых автомобилей.  

## Описание датасета

Датасет состоит из 11 признаков:  
1. name - Марка и модель автомобиля
2. year - Год выпуска автомобиля
3. engine_capacity - Объем двигателя (л)
4. horse_power - Мощность двигателя (л. с.)
5. fuel - Тип топлива
6. transmission - Каробка передач
7. drive_unit - Привод
8. mileage - Пробег (км)
9. location - Место продажи
10. price - Стоимость автомобиля

В последствии при подготовке данных для модели регрессии признак name был разделен на два: name (Марка автомобиля) и model (Модель автомобиля)

## Анализ данных

### Общая информация о датасете
Всего было проанализированно 1974 объявления, размещенных на сайте на момент 19 декабря 2023 года.  
По данным Информационного агентства Фонтанка спрос на подержанные автомобили в 2023 году вырос в основном из-за того, что основные бренды к которым привыкли российские водители приостановили поставки, 
а переходить на новые автомобили китайского производства пока не все готовы по причине отсутствия понимания логистики запчастей, срока службы автомобилей, а также их ремонтнопригодность.  

Также по данным Аналитического агентства Автостат, В десятку самых популярных вошли марки девяти зарубежных брендов, разорвавших отношения с Россией: Toyota, Kia, Hyundai, Nissan, Volkswagen, Honda, Ford, Chevrolet и Renault. На первой строчке — ожидаемо бренд отечественного автопрома Lada.  
Что в подтверждается данными полученными с агрегатора объявлений Drom.

![bar-plot-top-15](/img/ТОП-15%20самых%20продаваемых%20марок%20автомобилей.png)

### Дополнительная информация

По данным исследований автомобильного рынка "Авито Авто" средняя стоимость подержаных автомобилей составила 640 тыс. руб., при этом согласно распределению стоимости в 1974 объявлениях, размещенных на Drom, 
среднее значение с учетом догорих автомобилей составляет 2 млн. руб. (1 млн. руб. без учета дорогих авто), что в целом с учетом погрешности исследовний - сопоставимые результаты.
Распределение стоимости автомобилей, согласно проведенному тесту Шапиро-Уилка, нормальное, со смещением в левую сторону (в сторону низкой стоимости).  
![hist-plot-price](/img/Распределение%20цен%20автомобилей.png)

Среднее значение годового пробега автомобиля, по данным сайта Автокод, составляет от 10 до 30 тыс. км. в год. По данным проанализированных 1974 объявлений, средний пробег составляет от 120 до 130 тыс. км. при среднем возрасте автомобиля в 10 лет.  
Распределение пробега автомобилей также, согласно проведенному тесту Шапиро-Уилка, нормальное, со смещением в левую сторону (в сторону малого пробега). 
![hist-plot-mileage](/img/Распределение%20пробега%20автомобилей.png) 

Согласно корреляционной матрицы Спирмана, основное влияние числовых признаков на стоимость оказывают Мощность двигателя (0.75) и Год производства автомобиля (0.8).  
 
| Признак         | Коэффициент корреляции | t-критерий | t-критическое |
|-----------------|------------------------|------------|---------------|
| year            |               0.800623 |  59.337961 | 1,967         |
| engine_capacity |               0.350579 |  16.623285 |               |
| horse_power     |               0.751340 |  50.559390 |               |
| mileage         |              -0.487011 |  24.761735 |               |

Наиболее статистически значимые признаки: Мощность двигателя и Год производства.

## Подготовка датасета для обучения модели

1. Обработка выбросов
2. Перевод категориальных значений в числовые (Count Encoder или Label Encoder)
3. Разделение данных на тренировочную и тестовую выборки (sklearn: train_test_split). Размер тестовой выборки составил 20%.  
4. Выбор модели регрессии (RandomForestRegressor из библиотеки sklearn или XGBRegressor из библиотеки xgboost)
5. Обучение и тестирование модели  
6. Сохранение предобученной модели

## Результаты

Наилучший результат показала модель регрессии XGBRegressor с модифицировнными категориальными признаками через Count Encoder:  
* Accuracy тренировочной выборки: 0.99078
* Accuracy тестовой выборки: 0.94262

## Использование модели

Для использования модели создано приложение на основе streamlit.  (https://carpricemodel2023.streamlit.app)


