# Generating ids for drops and spikes in writers levels
library(dplyr)
detach(package:RPostgreSQL)
library(sqldf)
load(file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")

# DETERMING DROP AND RISE OF WRITER LEVELS
date_2<-max(weekly_level_001$level_date)
date_2less6<-date_2-7
bronze_curr_week<-weekly_level_001%>% filter(level=="BRONZE") %>% filter(level_date==date_2)%>% select(count)
bronze_curr_weekless6<-weekly_level_001%>% filter(level=="BRONZE") %>% filter(level_date==date_2less6)%>% select(count)

if(bronze_curr_week<bronze_curr_weekless6){
  print("drop")
  Drop<-sqldf("SELECT id FROM bronze_curr_week_listless6 WHERE bronze_curr_week_listless6.id 
          NOT IN(SELECT id FROM bronze_curr_week_listless6 )")
  
  
}else{
  
  print("Rise")
  Rise<-sqldf("SELECT id FROM bronze_curr_week_list WHERE bronze_curr_week_list.id 
          NOT IN(SELECT id FROM bronze_curr_week_listless6 )")
  Rise$level_date<-date_2
  Rise$level<-"Bronze"
}

bronze_curr_week_list<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_2)
bronze_curr_week_listless6<-writers_001%>% filter(name=="BRONZE") %>% filter(level_date==date_2less6)


# DETERMINING THE NUMBER WHO DROPPED OR INCREASED
library(dplyr)
detach(package:RPostgreSQL)
library(sqldf)
load(file = "/home/mikes/Loc_shiny/weeky_writer_level.rda")
load(file = "/home/mikes/Loc_shiny/Rise.rda")
load(file = "/home/mikes/Loc_shiny/Drop.rda")
# function to handle the task 

writer_level_monitor<-function(writerlevel){
  date_curr<-max(writers_001$level_date)
  date_prev<-date_curr-7
  level_count_curr<-weekly_level_001%>% filter(level==writerlevel) %>% filter(level_date==date_curr)%>% select(count)
  level_count_prev<-weekly_level_001%>% filter(level==writerlevel) %>% filter(level_date==date_prev)%>% select(count)
  level_curr_week_list<-writers_001%>% filter(name==writerlevel) %>% filter(level_date==date_curr)
  level_prev_week_list<-writers_001%>% filter(name==writerlevel) %>% filter(level_date==date_prev)
  print(level_count_curr)
  print(level_count_prev)
  if(level_count_curr < level_count_prev){
    print("drop")
    Drop<-sqldf("SELECT id FROM level_prev_week_list WHERE level_prev_week_list.id 
          NOT IN(SELECT id FROM level_curr_week_list)")
    Drop$level_date<-date_curr
    Drop$level<-writerlevel
    print(Drop)
    Drop_002<-Drop
    load(file = "/home/mikes/Loc_shiny/Drop.rda")
    Drop_001<-rbind(Drop_001,Drop_002)
    save(Drop_001, file = "/home/mikes/Loc_shiny/Drop.rda")
    #save(Drop, file = "/home/mikes/Loc_shiny/Drop.rda")
    
  }else if(level_count_curr > level_count_prev){
    
    print("Rise")
    Rise<-sqldf("SELECT id FROM level_curr_week_list WHERE level_curr_week_list.id 
          NOT IN(SELECT id FROM level_prev_week_list )")
    Rise$level_date<-date_curr
    Rise$level<-writerlevel
    print(Rise)
    Rise_002<-Rise
    load(file = "/home/mikes/Loc_shiny/Rise.rda")
    Rise_001<-rbind(Rise_001,Rise_002)
    save(Rise_001, file = "/home/mikes/Loc_shiny/Rise.rda")
  }else{
  
    print("Levels did not change")
  }

}

writer_level_monitor("BRONZE")
writer_level_monitor("SILVER")
writer_level_monitor("GOLD")



# changing staff for testing
table(writers_0011$name,writers_0011$level_date)
weekly_level_001
for (i in 1:nrow(weekly_level_001)) {
  if(weekly_level_001[i,3]=="2019-03-03"){
    weekly_level_001[i,3] <-"2019-02-24"
    print(weekly_level_001[i,3])
  }
}

for (i in 1:nrow(writers_001)) {
  if(writers_001[i,3]=="2019-03-03"){
    writers_001[i,3] <-"2019-02-24"
   print(writers_001[i,3])
  }
}





table(weekly_level_001$count)
writers_0011<-writers_0011[c(198-219),]


