library(highcharter)
library(dplyr)
load(file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")

highchart() %>%
  hc_add_series_df(data = weekly_level_001, 
                   type = "line", 
                   x=level_date, 
                   y=count,
                   group=level) %>%
  hc_xAxis(title= list(text="Week"),type='datetime', labels=list(format='{value:%Y-%m-%d}'))  %>%             
  hc_yAxis(title = list(text = "Writers Count"))%>% 
  hc_legend(enabled = TRUE) %>%
  hc_title(text= paste("<b>", "Weekly Writer Levels", "</b>", sep = "")) %>%
  hc_add_theme(hc_theme_google()) %>%
  hc_exporting(enabled = TRUE)    


