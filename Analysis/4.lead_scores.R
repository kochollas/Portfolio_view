library(sqldf)
# Working on CS stab
setwd("~/Documents/upwork/SimplyEloped/AI/")
lead <- read.csv("leads.csv")
head(lead)
customer <- read.csv("customer.csv")

lead_customer <- read.csv("lead_customer.csv")

# order the data by created_at_x : lead creation date

lead_customers <- sqldf("SELECT * FROM lead_customer ORDER BY created_at_x DESC")


# Remove duplicate rows of lead_id_x
library(dplyr)
unique_lead_customers = distinct(lead_customers, id, .keep_all = TRUE)

# Creating status 2
unique_lead_customers$STATUS_CODE <- ifelse(unique_lead_customers$STATUS == 'Contact',0,1)

#STARTING WORKING ON CORRELATIONS

cor(unique_lead_customers$STATUS_CODE, unique_lead_customers$location_id_x)

#
df <-sqldf("select fc_referrer, count(*) from unique_lead_customers group by fc_referrer order by count(*) DESC")

# Recoding variables

unique_lead_customers$landingpage_CODE <- 1

unique_lead_customers$landingpage_CODE <- ifelse(unique_lead_customers$fc_landing_page=='simplyeloped.com/virtual-weddings/',1,
                                                 ifelse(unique_lead_customers$fc_landing_page=='simplyeloped.com/',2,
                                                        ifelse(unique_lead_customers$fc_landing_page=='/elopement-packages/',3,4)))



cor(unique_lead_customers$STATUS_CODE,unique_lead_customers$landingpage_CODE) 
chisq.test(table(unique_lead_customers$STATUS_CODE,unique_lead_customers$landingpage_CODE))

# second variable

unique_lead_customers$location_CODE <- ifelse(unique_lead_customers$location_text=='Digital',1,
                                                 ifelse(unique_lead_customers$location_text=='Tennessee - Gatlinburg',2,
                                                        ifelse(unique_lead_customers$location_text=='Colorado',3,
                                                               ifelse(unique_lead_customers$location_text=='Colorado',4,5))))



cor(unique_lead_customers$STATUS_CODE,unique_lead_customers$location_CODE) 
chisq.test(table(unique_lead_customers$STATUS_CODE,unique_lead_customers$location_CODE))

# third variable

unique_lead_customers$refferer_CODE <- ifelse(unique_lead_customers$fc_referrer=='google - Organic',1,
                                              ifelse(unique_lead_customers$fc_referrer=='Google - Organic',2,
                                                     ifelse(unique_lead_customers$fc_referrer=='adwords',3,
                                                            ifelse(unique_lead_customers$fc_referrer=='(direct)',4,5))))


cor(unique_lead_customers$STATUS_CODE,unique_lead_customers$refferer_CODE) 
chisq.test(table(unique_lead_customers$STATUS_CODE,unique_lead_customers$refferer_CODE))


# third tab : venue finder datasets Model training --------------------------------------------------------------

library(dplyr)
venue_finder <- read.csv("vf_customer.csv")

vf <- sqldf("SELECT * FROM venue_finder ORDER BY created_at_x DESC")
unique_vf = distinct(vf, id, .keep_all = TRUE)

unique_vf$type_CODE <-ifelse(unique_vf$type == 'date',3,
                             ifelse(unique_vf$type == 'month',2,1))

unique_vf$status_CODE <-ifelse(unique_vf$STATUS == 'Contact',0,1)

#guest number
unique_vf$guest_no_CODE <- ifelse(unique_vf$guest_no == 'Just the two of us', 1,
                                  ifelse(unique_vf$guest_no == '1-4',2,
                                         ifelse(unique_vf$guest_no == '10-19',3,
                                                ifelse(unique_vf$guest_no == '20+',4, 5))))

#location

unique_vf$location_CODE <-ifelse(unique_vf$location_type == 'inspiration',1,2)

#created_at and ceremony date


# Generating cor and association

cor(unique_vf$status_CODE,unique_vf$type_CODE)
chisq.test(table(unique_vf$status_CODE,unique_vf$type_CODE))


cor(unique_vf$status_CODE,unique_vf$guest_no_CODE)
chisq.test(table(unique_vf$status_CODE,unique_vf$guest_no_CODE))

# location type




cor(unique_vf$status_CODE,unique_vf$location_CODE)
chisq.test(table(unique_vf$status_CODE,unique_vf$location_CODE))                             

# time of using vf

unique_vf$time_CODE <- as.integer(substr(unique_vf$created_at_x,12,13))

cor(unique_vf$status_CODE,unique_vf$time_CODE)
chisq.test(table(unique_vf$status_CODE,unique_vf$time_CODE)) 

# selected_date_to_wedding_Time

unique_vf$created_date<- as.Date(substr(unique_vf$created_at_x,1,10))
unique_vf$date1 <- ifelse(unique_vf$date=="","2021-12-22", unique_vf$date)
unique_vf$date1 <- as.Date(unique_vf$date1)
unique_vf$datediff_CODE <- unique_vf$date1 - unique_vf$created_date
unique_vf$datediff_CODE <-as.integer(unique_vf$datediff_CODE)

#unique_vf%>%select(datediff_CODE,STATUS)%>%filter(STATUS == 'Customer')%>%mutate(x=mean(datediff_CODE),y=sd(datediff_CODE))




cor(red_uvf$status_CODE,red_uvf$datediff_CODE)

chisq.test(table(unique_vf$status_CODE,unique_vf$datediff_CODE)) 


#------------------ Addressing class imbalance------------------------------------------
contacts_only <- subset(unique_lead_customers, STATUS == 'Contact')
customers_only <- subset(unique_lead_customers, STATUS == 'Customer')
contacts_num_rows <-sample(1:nrow(contacts_only), 2130)

#ind <- sample(1,nrow(data),replace=TRUE, prob=c(0.8,.2))
contacts_60_perc <- contacts_only[contacts_num_rows, ]

# Combine the two datasets
unique_lead_customers_red <- rbind(contacts_60_perc, customers_only)

# fc landing page

cor(unique_lead_customers_red$STATUS_CODE,unique_lead_customers_red$landingpage_CODE) 

# location code
cor(unique_lead_customers_red$STATUS_CODE,unique_lead_customers_red$location_CODE) 
chisq.test(table(unique_lead_customers$STATUS_CODE,unique_lead_customers$location_CODE))

#refferer_CODE
cor(unique_lead_customers_red$STATUS_CODE,unique_lead_customers_red$refferer_CODE) 

#location : destination selected
cor(unique_lead_customers_red$STATUS_CODE,unique_lead_customers_red$location_CODE) 


## II Second imbalance senario

contacts_vf<- subset(unique_vf, STATUS == 'Contact')
customers_vf <- subset(unique_vf, STATUS == 'Customer')
contacts_vf_rows <-sample(1:nrow(contacts_vf), 1368)

contacts_vf_60perc <- contacts_vf[contacts_vf_rows, ]

# Combine the two datasets
unique_vf_red <- rbind(contacts_vf_60perc, customers_vf)


# type : date selected

cor(unique_vf_red$status_CODE,unique_vf_red$type_CODE)

#time of the day
cor(unique_vf_red$status_CODE,unique_vf_red$time_CODE)

#guest count

cor(unique_vf_red$status_CODE,unique_vf_red$guest_no_CODE)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Adding more variables

unique_vf_red$timetowedding <-1
unique_vf_red$created_at<-ifelse(unique_vf_red$created_at == "", lubridate::as_date(today()), unique_vf_red$created_at)

#Add additional variables work HERE
query <- "SELECT id,status_CODE, type_CODE, guest_no_CODE,location_CODE,time_CODE, datediff_CODE 
FROM unique_vf_red "
unique_vf_data <- sqldf(query)
# Data from central station
query2 <- "SELECT id,landingpage_CODE, refferer_CODE FROM unique_lead_customers_red"
unique_lead_customers_data <- sqldf(query2)

query3 <- "SELECT * FROM unique_vf_data INNER JOIN unique_lead_customers_data ON 
unique_lead_customers_data.id = unique_vf_data.id"
mod_data <- sqldf(query3)






#------------ working on modelling------------------------------------------------------#

# logistic regression, Bayesian modelling, 

#-----LOGISTIC REGRESSION---------------------------------------------------------------#
# create the train and test data

ind <- sample(2,nrow(unique_vf_red),replace=TRUE, prob=c(0.8,.2))

train<-unique_vf_red[ind==1,]
test<-unique_vf_red[ind==2,]

# starting the modelling time_CODE,guest_no_CODE, ,landingpage_CODE
train = train %>% select(datediff_CODE,location_CODE,type_CODE,guest_no_CODE,status_CODE)
# Changing variables type to factor
no_of_cols = length(colnames(train))
for (i in 2:no_of_cols) {
  print(i)
  train[,i] <-factor(train[,i])
}
str(train)

mymodel <- glm(status_CODE ~ location_CODE + type_CODE + datediff_CODE+guest_no_CODE, data = train, family = 'binomial')
summary(mymodel)

# Prediction
p1 <- predict(mymodel, train, type = 'response')

# Misclassification error - train data
pred1 <- ifelse(p1>0.4, 1, 0)
tab1 <- table(Predicted = pred1, Actual = train$status_CODE)
tab1
1 - sum(diag(tab1))/sum(tab1)


# working with the test data
test = test %>% select(id,datediff_CODE,location_CODE,type_CODE,guest_no_CODE,status_CODE)
# Changing variables type to factor
no_of_cols = length(colnames(test))
for (i in 3:no_of_cols) {
  print(i)
  test[,i] <-factor(test[,i])
}
str(test)

# Write a csv to disc
write.csv(test, 'testing_data.csv')

# Misclassification error - test data
p2 <- predict(mymodel, test, type = 'response')
pred2 <- ifelse(p2>0.4, 1, 0)
tab2 <- table(Predicted = pred2, Actual = test$status_CODE)
tab2
1 - sum(diag(tab2))/sum(tab2)

#++++++++++++++++++++++++++= Generating data for human consumption
test_data <- cbind(test,pred2,p2)
test_data$location_CODE <-factor(test_data$location_CODE, levels = c(1,2),
                                 labels = c("inspiration","market"))
test_data$type_CODE <-factor(test_data$type_CODE, levels = c(1,2,3),
                                 labels = c("None","only month provided","date specified"))
test_data$guest_no_CODE <-factor(test_data$guest_no_CODE, levels = c(1,2,3,4,5),
                             labels = c("Just the two of us",
                                        "1-4","10-19","20+","5-9"))
test_data$status_CODE <-factor(test_data$status_CODE, levels = c(0,1),
                                 labels = c("Contact","Customer"))

test_data$pred2 <-factor(test_data$pred2, levels = c(0,1),
                               labels = c("Contact","Customer"))
colnames(test_data)<-c("user ids","days since first VF use","VF location type", "VF date type","VF guest_no",
                       "actual lead_status","Predicted lead status","prediction probabilities")
write.csv(test_data, "test_data.csv")

### ----------------------serious testing---------------------####
# main predictors : datediff_CODE,location_CODE,type_CODE,guest_no_CODE

test_replica <- rbind(c(10,1,1,1,0),c(7,2,3,3,1))
colnames(test_replica)<-colnames(test)
test_replica <-data.frame(test_replica)

# Changing variables type to factor
no_of_cols = length(colnames(test_replica))
for (i in 2:no_of_cols) {
  print(i)
  test_replica[,i] <-factor(test_replica[,i])
}
str(test_replica)


# Misclassification error - test data
p2 <- predict(mymodel, test_replica, type = 'response')
pred2 <- ifelse(p2>0.4, 1, 0)
tab2 <- table(Predicted = pred2, Actual = test$status_CODE)
tab2
1 - sum(diag(tab2))/sum(tab2)


# predicting from raw data 

venue_finder <- read.csv("vf_customer2.csv")
vf <- sqldf("SELECT * FROM venue_finder ORDER BY created_at_x DESC")
unique_vf = distinct(vf, id, .keep_all = TRUE)

unique_vf$type_CODE <-ifelse(unique_vf$type == 'date',3,
                             ifelse(unique_vf$type == 'month',2,1))

unique_vf$status_CODE <-ifelse(unique_vf$STATUS == 'Contact',0,1)

unique_vf$guest_no_CODE <- ifelse(unique_vf$guest_no == 'Just the two of us', 1,
                                  ifelse(unique_vf$guest_no == '1-4',2,
                                         ifelse(unique_vf$guest_no == '10-19',3,
                                                ifelse(unique_vf$guest_no == '20+',4, 5))))

#location

unique_vf$location_CODE <-ifelse(unique_vf$location_type == 'inspiration',1,2)

# selected_date_to_wedding_Time

unique_vf$created_date<- as.Date(substr(unique_vf$created_at_x,1,10))
unique_vf$date1 <- ifelse(unique_vf$date=="","2022-01-04", unique_vf$date)
unique_vf$date1 <- as.Date(unique_vf$date1)
unique_vf$datediff_CODE <- unique_vf$date1 - unique_vf$created_date
unique_vf$datediff_CODE <-as.integer(unique_vf$datediff_CODE)

test <- unique_vf



# Testing prediction from the python file

test_data = read.csv('for_prediction.csv')

test_data$type_CODE <-factor(test_data$type_CODE)
test_data$guest_no_CODE <-factor(test_data$guest_no_CODE)
test_data$location_CODE <-factor(test_data$location_CODE)
str(test_data)

p2 <- predict(mymodel, test_data, type = 'response')
pred2 <- ifelse(p2>0.4, 1, 0)

test_data <- cbind(test_data,pred2,p2*100)
head(test_data)

# Merging back to human readable format


# Working now on the model aspects in python
write.csv(train, "training_data.csv")

