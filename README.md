# scrape-and-plot-covid19
This repository scrapes figures of covid-19 cases in India, records them in a dataframe, and plots the data.

Figures are scraped periodically from the offical website of <a href = "https://www.mohfw.gov.in/">Ministry of Health and Family Welfare | GOI </a>

### Collected Data

The recorded dataframe has the following columns:

* Time
* Total confirmed cases (Indian and Foreign National have now been combined on the website under "Confirmed")
* Cured/Discharged/Migrated
* Number of Deaths
* The total figure (often reported in the news)

### Samples

A sample table, updated as of 29/03/2020 07:30 PM.
(Edit: This has been updated to the new structure of the website where Indian and Foreign National cases have now been combined and reported)


|    | Time                   |   Confirmed |   Cured/Di/M |   Dead |   "Total" |
|---:|:-----------------------|------------:|-------------:|-------:|----------:|
|  0 | 22.03.2020 at 06:30 PM |         357 |           24 |      7 |       388 |
|  1 | 23.03.2020 at 09:00 AM |         388 |           24 |      7 |       419 |
|  2 | 23.03.2020 at 06:00 PM |         432 |           31 |      7 |       470 |
|  3 | 23.03.2020 at 08:15 PM |         433 |           31 |      7 |       471 |
|  4 | 24.03.2020 at 08:45 AM |         492 |           37 |      9 |       538 |
|  5 | 24.03.2020 at 05:45 PM |         519 |           40 |      9 |       568 |
|  6 | 25.03.2020 at 09:15 AM |         562 |           41 |      9 |       612 |
|  7 | 25.03.2020 at 06:45 PM |         606 |           43 |     10 |       659 |
|  8 | 26.03.2020 at 10:15 AM |         649 |           43 |     13 |       705 |
|  9 | 26.03.2020 at 08:00 PM |         694 |           45 |     16 |       755 |
| 10 | 27.03.2020 at 09:15 AM |         724 |           67 |     17 |       808 |
| 11 | 28.03.2020 at 09:30 AM |         873 |           79 |     19 |       971 |
| 12 | 28.03.2020 at 05:45 PM |         909 |           80 |     19 |      1008 |
| 13 | 28.03.2020 at 05:45 PM |         909 |           80 |     19 |      1008 |
| 14 | 29.03.2020 at 10:00 AM |         979 |           87 |     25 |      1091 |
| 15 | 29.03.2020 at 07:30 PM |        1024 |           96 |     27 |      1147 |


### Plotting

A sample plot using the above data:

![alt text](https://github.com/Sahej02/scrape-and-plot-covid19/blob/master/sample.png "Sample Plot")

