import os
import requests
import sqlite3
import pandas as pd
#URLs for the datasets (Annual and Quarterly)
datasets = {
    "annual_unemployment": "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=UNRATE&scale=left&cosd=1960-01-01&coed=2023-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-06&revision_date=2024-11-06&nd=1948-01-01",
    "annual_gdp": "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1&scale=left&cosd=1960-01-01&coed=2023-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=sum&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-06&revision_date=2024-11-06&nd=1947-01-01",
    "quarterly_unemployment": "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=UNRATE&scale=left&cosd=2014-07-01&coed=2024-07-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-08&revision_date=2024-11-08&nd=1948-01-01",
    "quarterly_gdp": "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1&scale=left&cosd=2014-07-01&coed=2024-07-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-08&revision_date=2024-11-08&nd=1947-01-01"
}



data = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))



# Downloading each dataset (Annually and Quarterly) in csv format and then converting it to sqlite
for name, url in datasets.items():
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(data, f"{name}.csv")
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloading Complete for: {name}")
        df = pd.read_csv(f'{data}\\{name}.csv')
        sqlite_path = os.path.join(data,f"{name}.sqlite") # for creating seperate sqlite for each csv file
        #sqlite_path = os.path.join(data,"data.sqlite") # to create single sqlite file including all the csv file as table
        conn = sqlite3.connect(sqlite_path)
        df.to_sql(name,conn,if_exists='replace',index=False)
        conn.close()
        print(f"{name}.csv  is converted to {name}.sqlite")
    else:
        print(f"Downloading Failed for: {name} (Status code: {response.status_code})")
        