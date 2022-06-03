# Weekly writer levels miner
# loading the necessary packages and conn params
load(file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")
#load(file="/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/weeky_writer_level.rda")
require("RPostgreSQL")
library(dplyr)
Sys.getenv("HOME")
pass <- Sys.getenv("PW")
database <- Sys.getenv("DBNAME")
dbuser<- Sys.getenv("USER2")
dbhost<-Sys.getenv("HOST")
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = database,
                 host = dbhost, port = 5432,
                 user = dbuser, password = pass)
#  Pulling writer levels
sql_command<-"SELECT writers.id, levels.name FROM writers
INNER JOIN levels ON writers.level_id = levels.id
WHERE level_id in(1,2,3)"
writers<-dbGetQuery(con, sql_command)
x=data.frame(table(writers$name))
names(x)<-c("level","count")
# working on creating the data table
date.variable<-as.Date(Sys.Date())
x$level_date<-date.variable
weekly_level_002<-x
writers_002<-writers
writers_002$level_date<-date.variable
#saving weekly data
weekly_level_001<-rbind(weekly_level_001,weekly_level_002)
writers_001<-rbind(writers_001,writers_002)
# save as an rda file to the scripts folder
save(weekly_level_001, writers_001, file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")
#save(weekly_level_001, writers_001, file="/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/weeky_writer_level.rda")
rm(weekly_level_002,writers_002, Gold, Silver, Bronze, x, writers, drv, con, data)
#END

