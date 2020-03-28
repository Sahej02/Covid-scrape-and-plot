# scrape-and-plot-covid19
This repository scrapes figures of covid-19 cases in India, records them in a dataframe, and plots the data.

Figures are scraped periodically from the offical website of <a href = "https://www.mohfw.gov.in/">Ministry of Health and Family Welfare | GOI </a>

### Collected Data

The recorded dataframe has the following columns:

* Time
* Total confirmed Indian National cases (IN)
* Total confirmed Foreign National cases (FN)
* Cured/Discharged/Migrated
* Number of Deaths
* The total figure (often reported in the news)

### Samples

A sample table, updated as of 28/03/2020 05:45 PM.


|    | Time                   |   IN |   FN |   Cured/Discharged/Migrated |   Dead |   "Total" |
|---:|:-----------------------|-----:|-----:|-------------:|-------:|----------:|
|  0 | 22.03.2020 at 06:30 PM |  319 |   38 |           24 |      7 |       388 |
|  1 | 23.03.2020 at 09:00 AM |  349 |   39 |           24 |      7 |       419 |
|  2 | 23.03.2020 at 06:00 PM |  393 |   39 |           31 |      7 |       470 |
|  3 | 23.03.2020 at 08:15 PM |  394 |   39 |           31 |      7 |       471 |
|  4 | 24.03.2020 at 08:45 AM |  451 |   41 |           37 |      9 |       538 |
|  5 | 24.03.2020 at 05:45 PM |  476 |   43 |           40 |      9 |       568 |
|  6 | 25.03.2020 at 09:15 AM |  519 |   43 |           41 |      9 |       612 |
|  7 | 25.03.2020 at 06:45 PM |  563 |   43 |           43 |     10 |       659 |
|  8 | 26.03.2020 at 10:15 AM |  602 |   47 |           43 |     13 |       705 |
|  9 | 26.03.2020 at 08:00 PM |  647 |   47 |           45 |     16 |       755 |
| 10 | 27.03.2020 at 09:15 AM |  677 |   47 |           67 |     17 |       808 |
| 11 | 28.03.2020 at 09:30 AM |  826 |   47 |           79 |     19 |       971 |
| 12 | 28.03.2020 at 05:45 PM |  862 |   47 |           80 |     19 |      1008 |


### Plotting

A sample plot using the above data:

![alt text](https://github.com/Sahej02/scrape-and-plot-covid19/blob/master/sample.png "Sample Plot")

