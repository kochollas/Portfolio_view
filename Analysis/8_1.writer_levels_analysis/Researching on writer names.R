#########################################################################
# Script populating the shares dataframe
library(elastic)
library(dplyr)
library(lubridate)
date_to1<-as.Date(Sys.Date())-1
#date_to1<-as.Date("2018-05-26")
date_from1<-date_to1-6

# Weeks calculation
#Function to calculate week
findWeekNo <- function(myDate){
  if (!is.na(myDate)){
    # Find out the start day of week 1; that is the date of first Sun in the year
    weekday <- switch(weekdays(as.Date(paste(format(as.Date(myDate),"%Y"),"01-01", sep = "-"))),
                      "Monday"={2},
                      "Tuesday"={3},
                      "Wednesday"={4},
                      "Thursday"={5},
                      "Friday"={6},
                      "Saturday"={7},
                      "Sunday"={1}
    )
    
    firstSun <- ifelse(weekday==1,1, 9 - weekday )
    
    weekNo <- ifelse(weekday==1, floor((as.POSIXlt(myDate)$yday - (firstSun-1))/7)+1, floor((as.POSIXlt(myDate)$yday - (firstSun-1))/7)+2)
    
  }
  else{
    weekNo <-NA
  }
  return(weekNo)
}

Sys.getenv("HOME")
user <- Sys.getenv("ES_PASS")
host <- Sys.getenv("ES_HOST")
dbuser<- Sys.getenv("ES_USER")

user<-paste0("v?sF”xw@1by","\\","9-Zm0X’BlpL.0")

connect(es_host = host, es_port = 9243, es_path = NULL,
        es_transport_schema = "https", es_user = dbuser, es_pwd = user)

body1 <- list(query = list(range = list(create_date = list(gte = "2015-01-01", lte = "2017-12-25"))))

body6 <- Search('profiles',body=body1, asdf = TRUE, size = 10000)
profiles<-body6$hits$hits
# hits 464

profiles <- profiles %>%
  mutate(created.date=as.POSIXct(`_source.create_date`/1000, origin="1970-01-01", tz = "Africa/Nairobi")) 

profiles <- profiles %>%
  mutate(last_update.date=as.POSIXct(`_source.last_update_date`/1000, origin="1970-01-01", tz = "Africa/Nairobi")) 

save(profiles,file="new writers.rda")

aggs <- '{
    "aggs": {
        "stats" : {
            "terms" : {
                "level" : "BRONZE"
            }
        }
    }
}'

aggs<-'{
"query": {
  "term" : { "_source.level" : "BRONZE" } 
}
}'



prof<-Search(index="profiles*", body=aggs)
prof<-body6$hits$hits






#  Research on displaying the writer names 



# Kibana Problems and Researching for Solutions

GET articles/article/_search
{
  "query": {
    "regexp":{
      "body": "obado "
    }
  }
}


body : "obado" AND "Sharon"

GET articles/article/_search
{
  "query": {
    "regexp":{
      "body":"obado" AND "Sharon"
    }
  }
}


# Wladecks Query
POST /articles/article/_search
{
  "size": 100,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "status": "published","title": "Obado"
          }
        },
        {
          "range": {
            "publish_date": {
              "gte": "2017-10-30",
              "lt": "2017-11-05"
            }
          }
        }
        ]
    }
  },
  "_source": [
    "status",
    "kcategory",
    "publish_date"
    ]
}


POST /articles/article/_search
{
  "size": 100,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "title": "Obado"
            
          }
        },
        {
          "range": {
            "publish_date": {
              "gte": "2018-10-30",
              "lt": "2018-11-05"
            }
          }
        }
        ]
    }
  },
  "_source": [
    "status",
    "kcategory",
    "publish_date",
    "body"
    ]
}


#  Rodgers

POST /articles/article/_search
{
  "size": 100,
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "body": "william"
            
          }
        },
        {
          "range": {
            "publish_date": {
              "gte": "2018-10-30",
              "lt": "2018-11-05"
            }
          }
        }
        ]
    }
  },
  "_source": [
    "status",
    "kcategory",
    "publish_date",
    "title"
    ]
}



# Chloe Query request for kisii total published writers for 2018


{
  "size": 10000,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "klocation": "Kisii"
          }
        },
        {
          "range": {
            "publish_date": {
              "gte": "2018-01-01",
              "lt": "2018-12-31"
            }
          }
        }
        ]
    }
  },
  "_source": [
    "status",
    "kcategory",
    "publish_date",
    "klocation",
    "editor_id",
    "writer_id"
    ]
}


tims


{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "status": "published"
          }
        },
        {
          "term": {
            "klocation": "Kisii"
          }
        },
        {
          "range": {
            "publish_date": {
              "gte": "2018-01-01",
              "lt": "2018-12-31"
            }
          }
        }
        ]
    }
  },
  "size": 0,
  "aggs": {
    "group_by_status": {
      "terms": {
        "field": "status"
      }
    },
    "group_by_writer": {
      "terms": {
        "field": "writer_id"
        
      }
    },
    "group_by_caterogy": {
      "terms": {
        "field": "category_id"
      }
    }
  }
}


























