## An R shiny application to analyze Safaricom Mpesa statements in detail
The application can be deployed on AWS EC2 linux instance or shiny sever pro 

### Prerequisites
#### Shiny Dependencies
You must have the following R packages installed on your server instance
library(stringr)
library(pdftools)
library(rebus)
library(dplyr)
library(ggplot2)
library(highcharter)
#### Linux Dependencies
libcurl4-openssl-dev 
libpoppler-cpp-dev

```
ui.R
```
This will implement the graphical user interface what the user interacts with 
```
server.R
```
This will mainly implement the backend activities of the app
