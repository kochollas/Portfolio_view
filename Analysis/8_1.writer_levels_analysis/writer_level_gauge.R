# DETERMINING THE WRITERS WHO DROPPED OR INCREASED A LEVEL
library(dplyr)
detach(package:RPostgreSQL)
library(sqldf)
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/weeky_writer_level.rda")
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Rise.rda")
#load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Drop.rda")
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
          NOT IN(SELECT id FROM level_curr_week_list )")
    Drop$level_date<-date_curr
    Drop$level<-writerlevel
    print(Drop)
    Drop_002<-Drop
    #load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Drop.rda")
    load(file = "/home/mikes/Loc_shiny/Drop.rda")
    Drop_001<-rbind(Drop_001,Drop_002)
    #save(Drop_001,file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Drop.rda")
    save(Drop_001, file = "/home/mikes/Loc_shiny/Drop.rda")
    
    
  }else if(level_count_curr > level_count_prev){
    
    print("Rise")
    Rise<-sqldf("SELECT id FROM level_curr_week_list WHERE level_curr_week_list.id 
          NOT IN(SELECT id FROM level_prev_week_list )")
    Rise$level_date<-date_curr
    Rise$level<-writerlevel
    print(Rise)
    Rise_002<-Rise
    #load(file = "/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Rise.rda")
    load(file = "/home/mikes/Loc_shiny/Rise.rda")
    Rise_001<-rbind(Rise_001,Rise_002)
    #save(Rise_001, file="/opt/shiny-server/samples/sample-apps/hivisasa-dashboard/scripts/Rise.rda")
    save(Rise_001, file = "/home/mikes/Loc_shiny/Rise.rda")
  }else{
    
    print("Levels did not change")
  }
  
}


writer_level_monitor("GOLD")
writer_level_monitor("SILVER")
writer_level_monitor("BRONZE")
