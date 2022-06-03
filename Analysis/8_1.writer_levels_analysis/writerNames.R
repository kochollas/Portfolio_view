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
#Loading writer names from elastic search
library(elastic)
library(dplyr)
library(lubridate)
Sys.getenv("HOME")
user <- Sys.getenv("ES_PASS")
host <- Sys.getenv("ES_HOST")
dbuser<- Sys.getenv("ES_USER")

user<-paste0("v?sF”xw@1by","\\","9-Zm0X’BlpL.0")

connect(es_host = host, es_port = 9243, es_path = NULL,
        es_transport_schema = "https", es_user = dbuser, es_pwd = user)


#Convert Writer ID to Writer Name

id<-as.list(writers$id)
select_variables <- c("_id","_source.name","_source.email","_source.phone_number")

#Loop through IDs and match them to name in ES database
df1 <- list()

for(i in id){
  if(!is.na(i)) {
    print(i)
    
    query=paste0("id:'",i,"'")

    
    ## Pull the total number of hits
    body2 <- Search('profiles', q=query)$hits$total
    
    ## Extract the data and convert to a dataframe
    if (body2!=0) {
      body3 <- Search('profiles', q=query, asdf = TRUE, size = 1)
      
      df1[[i]] <- body3$hits$hits %>%
        select(select_variables)
    }
  }
}

# Restructure the list appropriately
df2<-list()
for(i in 1:length(df1)){
  
  print(df1[[i]])
  df2[[i]]<-df1[[i]]

}

data1<-df2[[1]]
save(data1,file="/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/data1.rda")

for(i in 2:length(df2)){
  
  load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/data1.rda" )
  print(df2[[i]])
  data1<-rbind(data1,df2[[i]])
  save(data1,file="/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/data1.rda")
  rm(data1)
  
}

load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/data1.rda" )

data1$`_source.name`<-tolower(data1$`_source.name`)


simpleCap <- function(x) {
  s <- strsplit(x, " ")[[1]]
  paste(toupper(substring(s, 1,1)), substring(s, 2),
        sep="", collapse=" ")
}

data1$`_source.name`<-sapply(data1$`_source.name`,simpleCap)

names(data1)<-c("Writer_id","Name","Email","Phone_number") 
names(writers)<-c("Writer_id","Level")
Current_Writer_Details<-merge(data1,writers, by="Writer_id")
save(Current_Writer_Details,file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/WriterDetails")

#END

