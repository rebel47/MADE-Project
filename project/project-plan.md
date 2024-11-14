# Project Plan

## Title
Unemployment Rate and GDP Growth Correlation in the United States

## Main Question

1. Is there a significant relationship between the annual unemployment rate and GDP growth in the United States over time?

## Description

Understanding the link between unemployment rate and economic growth which can reveal key insights into the U.S. economy. In this project I'll explores the relationship between unemployment rates and real GDP growth over both long-term and recent periods. By analyzing annual data from 1960 to 2023 and quarterly data from the last 10 years, we aim to identify patterns, cycles, and short-term variations. Examining how these indicators move together or diverge can provide a clearer understanding of their impact on each other and potentially inform economic policies and forecasts. This dual-level analysis will help us see how changes in employment and economic output align or differ during various economic cycles.


## Datasources

### 1. **Unemployment Rate (U.S.)**

- **Annual Data**:
  - **Metadata URL**: [U.S. Bureau of Labor Statistics - Unemployment Rate](https://fred.stlouisfed.org/series/UNRATE#0)
  - **Data URL**: [Annual Unemployment Rate Data](https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=UNRATE&scale=left&cosd=1960-01-01&coed=2023-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-06&revision_date=2024-11-06&nd=1948-01-01)
  - **Description**: Provides the seasonally adjusted annual average U.S. unemployment rate from 1960 to 2023, allowing for easy year-over-year comparisons.

- **Quarterly Data**:
  - **Metadata URL**: [U.S. Bureau of Labor Statistics - Unemployment Rate](https://fred.stlouisfed.org/series/UNRATE#0)
  - **Data URL**: [Quarterly Unemployment Rate Data](https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=UNRATE&scale=left&cosd=2014-07-01&coed=2024-07-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-08&revision_date=2024-11-08&nd=1948-01-01)
  - **Description**: Contains quarterly unemployment rates from 2014 to 2024, seasonally adjusted to support analysis of recent short-term trends.

### 2. **Real Gross Domestic Product (Real GDP)**

- **Annual Data**:
  - **Metadata URL**: [U.S. Bureau of Economic Analysis - Real GDP](https://fred.stlouisfed.org/series/GDPC1#0)
  - **Data URL**: [Annual Real GDP Data](https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1&scale=left&cosd=1960-01-01&coed=2023-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=sum&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-06&revision_date=2024-11-06&nd=1947-01-01)
  - **Description**: Provides the annual Real GDP of the U.S. (adjusted for inflation) from 1960 to 2023, reflecting overall economic growth and output levels.

- **Quarterly Data**:
  - **Metadata URL**: [U.S. Bureau of Economic Analysis - Real GDP](https://fred.stlouisfed.org/series/GDPC1#0)
  - **Data URL**: [Quarterly Real GDP Data](https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GDPC1&scale=left&cosd=2014-07-01&coed=2024-07-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2024-11-08&revision_date=2024-11-08&nd=1947-01-01)
  - **Description**: Contains quarterly Real GDP values for the U.S. from 2014 to 2024, adjusted for inflation. This data allows a more detailed look at economic growth and short-term variations.


## Work Packages

1. Data Collection [#1][i1]
2. Data Cleaning and Preprocessing [#2][i2]
3. Exploratory Data Analysis (EDA) [#3][i3]
4. Correlation Analysis [#4][i4]
5. Data Visualization [#5][i5]
6. Reporting [#6][i6]

[i1]: https://github.com/rebel47/MADE-Project/issues/1
[i2]: https://github.com/rebel47/MADE-Project/issues/2
[i3]: https://github.com/rebel47/MADE-Project/issues/3
[i4]: https://github.com/rebel47/MADE-Project/issues/4
[i5]: https://github.com/rebel47/MADE-Project/issues/5
[i6]: https://github.com/rebel47/MADE-Project/issues/6
