#############################################33
#sudo apt-get install libpq-dev

installed.packages("RPostgreSQL")
require("RPostgreSQL")
pw <- {
  "pa3967ba284a8953a8190f81ade2f7a157c4cacd93c38d4327730ba87798be0ef"
}
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "d3f234is95egp7",
                 host = "ec2-63-33-54-34.eu-west-1.compute.amazonaws.com", port = 5432,
                 user = "u5bkt37ja3i32k", password = pw)
rm(pw) # removes the password

# check for the writers table
dbExistsTable(con, "writers")
sql_command<-"SELECT writers.id, levels.name FROM writers
INNER JOIN levels ON writers.level_id = levels.id
WHERE level_id in(1,2,3)"
#sql_command<-"SELECT * FROM writers where writers.level_id is not null"
save(writers,file = "Writers_Levels")
writers<-dbGetQuery(con, sql_command)
# Plotting pie chart to show current writer level stats
x=table(writers$name)
lbls<-paste(names(x),x,sep = ":")
title<-"Current Writer Levels"
total<-paste("Total Writers", sum(x),sep = ":")
pie(x,labels=lbls,col=rainbow(length(lbls)), main =paste(title,"\n",total,sep = ""))






# working on connection using enviroment variables
require("RPostgreSQL")
Sys.getenv("HOME")
pass <- Sys.getenv("PW")
database <- Sys.getenv("DBNAME")
dbuser<- Sys.getenv("USER2")

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = database,
                 host = "ec2-63-33-54-34.eu-west-1.compute.amazonaws.com", port = 5432,
                 user = dbuser, password = pass)
#  Pulling writer levels
sql_command<-"SELECT writers.id, levels.name FROM writers
INNER JOIN levels ON writers.level_id = levels.id
WHERE level_id in(1,2,3)"
writers<-dbGetQuery(con, sql_command)
x=table(writers$name)
#save(writers,file = "/Writers_Levels.rda")
# close the connection
#dbDisconnect(con)
#dbUnloadDriver(drv)

# Plotting pie charts for the writer levels - GET CURRENT WRITER LEVELS
x=table(writers$name)
lbls<-paste(names(x),x,sep = ":")
title<-"Current Writer Levels"
total<-paste("Total Writers", sum(x),sep = ":")
pie(x,labels=lbls,col=rainbow(length(lbls)), main =paste(title,"\n",total,sep = ""))

# Weekly Writer Levels
# Creating an rda file
date_to<-as.Date(Sys.Date())-1
date_from<-date_to-6

