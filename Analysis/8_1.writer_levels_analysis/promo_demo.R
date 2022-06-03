# Loading required data in memory
library(dplyr)
detach(package:RPostgreSQL)
library(sqldf)
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/weeky_writer_level.rda")
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Rise.rda")
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Drop.rda")
load(file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")
load(file = "/home/mikes/Loc_shiny/Rise.rda")
load(file = "/home/mikes/Loc_shiny/Drop.rda")



# monitoring promotions
levels_promotions<-function(){
  #Levels Promotions
  date_curr<-max(writers_001$level_date)
  date_prev<-date_curr-7
  #load whole data curr and prev week
  data_curr<-writers_001%>% filter(level_date==date_curr)
  data_prev<-writers_001%>% filter(level_date==date_prev)
  #load Bronze writers curr and prev
  bronze_curr<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_curr)
  bronze_prev<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_prev)
  #load silver writers curr and prev
  silver_curr<-writers_001%>% filter(name=="SILVER") %>% filter(level_date==date_curr)
  silver_prev<-writers_001%>% filter(name=="SILVER") %>% filter(level_date==date_prev)
  #load Gold writers curr and prev
  gold_curr<-writers_001%>% filter(name=="GOLD") %>% filter(level_date==date_curr)
  gold_prev<-writers_001%>% filter(name=="GOLD") %>% filter(level_date==date_prev)
 
  #Bronze promoted/new writers
  new_bronze<-sqldf("SELECT id , name, level_date FROM data_curr WHERE data_curr.id 
          NOT IN(SELECT id FROM data_prev )")
  bronze_promoted<-nrow(new_bronze)
  
  #Silver promoted writers
  new_silver<-sqldf("SELECT id , name, level_date FROM silver_curr WHERE silver_curr.id 
          IN(SELECT id FROM bronze_prev )")
  silver_promoted<-nrow(new_silver)
  #Gold Writers
  new_gold4rsilver<-  new_silver<-sqldf("SELECT id , name, level_date FROM gold_curr WHERE gold_curr.id 
          IN(SELECT id FROM silver_prev) ")
  new_gold4rbronze<- sqldf("SELECT id , name, level_date FROM gold_curr WHERE gold_curr.id 
          IN(SELECT id FROM bronze_prev) ")
  new_gold<-bind_rows(new_gold4rsilver,new_gold4rbronze)
  gold_promoted<-nrow(new_gold)
  
}

# Monitoring Demotions
levels_demotions<-function(){
  date_curr<-max(writers_001$level_date)
  date_prev<-date_curr-7
  #load whole data curr and prev week
  data_curr<-writers_001%>% filter(level_date==date_curr)
  data_prev<-writers_001%>% filter(level_date==date_prev)
  #load Bronze writers curr and prev
  bronze_curr<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_curr)
  bronze_prev<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_prev)
  #load silver writers curr and prev
  silver_curr<-writers_001%>% filter(name=="SILVER") %>% filter(level_date==date_curr)
  silver_prev<-writers_001%>% filter(name=="SILVER") %>% filter(level_date==date_prev)
  #load Gold writers curr and prev
  gold_curr<-writers_001%>% filter(name=="GOLD") %>% filter(level_date==date_curr)
  gold_prev<-writers_001%>% filter(name=="GOLD") %>% filter(level_date==date_prev)
  
  #Bronze promoted/new writers
  new_bronze<-sqldf("SELECT id , name, level_date FROM data_curr WHERE data_curr.id 
          NOT IN(SELECT id FROM data_prev )")
  bronze_promoted<-nrow(new_bronze)
  
  #Silver promoted writers
  new_silver<-sqldf("SELECT id , name, level_date FROM silver_curr WHERE silver_curr.id 
          IN(SELECT id FROM bronze_prev )")
  silver_promoted<-nrow(new_silver)
  #Gold Writers
  new_gold4rsilver<-  new_silver<-sqldf("SELECT id , name, level_date FROM gold_curr WHERE gold_curr.id 
          IN(SELECT id FROM silver_prev) ")
  new_gold4rbronze<- sqldf("SELECT id , name, level_date FROM gold_curr WHERE gold_curr.id 
          IN(SELECT id FROM bronze_prev) ")
  new_gold<-bind_rows(new_gold4rsilver,new_gold4rbronze)
  gold_promoted<-nrow(new_gold)
  
}





