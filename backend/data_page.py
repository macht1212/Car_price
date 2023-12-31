import streamlit as st
import pandas as pd
import plotly.express as ple
import plotly.figure_factory as ff

from data_prep.data_prep import open_file, drop_data, replace, fillna_, price, name_sep


def data_part():
    data = open_file('cars_2023-12-19')

    data = drop_data(data)
    data = replace(data)
    data = fillna_(data)
    data = price(data)
    data = name_sep(data)

    st.markdown("""### Общая информация о датасете""")

    if st.toggle('Показать статистические данные датасета'):
        st.dataframe(data.describe())

    st.markdown("""
    Всего было проанализированно 1974 объявления, размещенных на сайте на момент 19 декабря 2023 года.  
    По данным Информационного агентства Фонтанка спрос на подержанные автомобили в 2023 году вырос в основном из-за того, что основные бренды к которым привыкли российские водители приостановили поставки, 
    а переходить на новые автомобили китайского производства пока не все готовы по причине отсутствия понимания логистики запчастей, срока службы автомобилей, а также их ремонтнопригодность.  
    """)
    if st.toggle('Показать датасет'):
        st.dataframe(data)

    st.markdown("""
    Также по данным Аналитического агентства Автостат, В десятку самых популярных вошли марки девяти зарубежных брендов, разорвавших отношения с Россией: Toyota, Kia, Hyundai, Nissan, Volkswagen, Honda, Ford, Chevrolet и Renault. На первой строчке — ожидаемо бренд отечественного автопрома Lada.  
    Что в подтверждается данными полученными с агрегатора объявлений Drom.""")

    count = st.slider('Количество марок', 5, 20, 10)
    top_15_adds = ple.bar(data.name.value_counts().head(count),
                          labels={'index': 'Марка автомобиля', 'value': 'Количнство объявлений, шт'})
    st.plotly_chart(top_15_adds, use_container_width=True)

    st.markdown("""По данным исследований автомобильного рынка "Авито Авто" средняя стоимость подержаных автомобилей составила 640 тыс. руб., при этом согласно распределению стоимости в 1974 объявлениях, размещенных на Drom, 
среднее значение с учетом догорих автомобилей составляет 2 млн. руб. (1 млн. руб. без учета дорогих авто), что в целом с учетом погрешности исследовний - сопоставимые результаты.
Распределение стоимости автомобилей, согласно проведенному тесту Шапиро-Уилка, нормальное, со смещением в левую сторону (в сторону низкой стоимости).""")

    prices_fig = ple.histogram(data.price, labels={'value': 'Стоимость, руб.'})
    st.plotly_chart(prices_fig, use_container_width=True)

    st.markdown("""Среднее значение годового пробега автомобиля, по данным сайта Автокод, составляет от 10 до 30 тыс. км. в год. По данным проанализированных 1974 объявлений, средний пробег составляет от 120 до 130 тыс. км. при среднем возрасте автомобиля в 10 лет.  
Распределение пробега автомобилей также, согласно проведенному тесту Шапиро-Уилка, нормальное, со смещением в левую сторону (в сторону малого пробега). """)

    mileage_fig = ple.histogram(data[data.mileage > 10].mileage, labels={'value': 'Пробег, тыс. км.'})
    st.plotly_chart(mileage_fig, use_container_width=True)

    st.markdown(
        '''Согласно корреляционной матрицы Спирмана, основное влияние числовых признаков на стоимость оказывают Мощность двигателя (0.75) и Год производства автомобиля (0.8).''')
    st.markdown("""| Признак         | Коэффициент корреляции | t-критерий | t-критическое |
|-----------------|------------------------|------------|---------------|
| year            |               0.800623 |  59.337961 | < 1,967       |
| engine_capacity |               0.350579 |  16.623285 |               |
| horse_power     |               0.751340 |  50.559390 |               |
| mileage         |              -0.487011 |  24.761735 |               |

""")

    st.markdown('''
    
    ''')

    if st.toggle('Показать дополнительные графики'):
        st.markdown("""### Варианты коробок передач в объявлениях""")
        st.plotly_chart(ple.bar(data.transmission.value_counts(),
                                labels={'index': 'Тип коробки передач', 'value': 'Количество, шт'}),
                        use_container_width=True)

        st.markdown("""### Распределение объема двигателя""")
        st.plotly_chart(ple.histogram(data.engine_capacity, nbins=15, labels={'value': 'Объем двигателя, л'}),
                        use_container_width=True)

        st.markdown("""### Распределение мощности двигателей л.с.""")
        st.plotly_chart(ple.histogram(data.horse_power, nbins=15, labels={'value': 'Мощность двигателя, л.с.'}),
                        use_container_width=True)

        st.markdown("""### Варианты топлива""")
        st.plotly_chart(
            ple.bar(data.fuel.value_counts(), labels={'index': 'Тип топлива', 'value': 'Количество объявлений, шт'}),
            use_container_width=True)
