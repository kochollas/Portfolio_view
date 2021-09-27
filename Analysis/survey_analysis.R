library(dplyr)
var = data.frame(table(final_survey_data$selected_region))
colnames(var)[1]<-c("Region")
var$Freq = round(var$Freq/sum(var$Freq)*100,2)
var %>% arrange(Freq)

freq_gen <- function(data,colname){

  var = data.frame(table(data[,c(colname)]))
  colnames(var)[1]<-c(colname)
  var$Percentage = round(var$Freq/sum(var$Freq)*100,2)
  var %>% arrange(Percentage)
  var_header = cbind.data.frame(colname,"Freq","Percentage") 
  names(var_header) <- colnames(var)
  var_final <- rbind(var_header,var)
  var_footer <- cbind.data.frame("***** "," *****"," *****") 
  names(var_footer) <- colnames(var)
  var_final2 <- rbind(var_final,var_footer)
  return(var_final2)
  
}

reg = freq_gen(final_survey_data,"selected_region")
reg2 = freq_gen(final_survey_data,"network")
gender = freq_gen(final_survey_data,"secA_q2")
gender2 = freq_gen(final_survey_data,"secA_q3")

write.table(reg, "myDF.csv", sep = ",", col.names = !file.exists("myDF.csv"), append = T)
write.table(gender2, "myDF.csv", sep = ",", col.names = !file.exists("myDF.csv"), append = T)


dataB = final_survey_data[,c(1:40)]
Batch <- function(dataB){
  i=20
  N = ncol(dataB)
  for (i in 20:N){
      if(class(dataB[,c(i)])=="character"){
        print("RESET to Character")
      }else if(class(dataB[,c(i)])=="integer"){
        print("RESET to integer")
      }else if(class(dataB[,c(i)])=="numeric"){
        print("RESET to numeric")
      }else if(class(dataB[,c(i)])=="factor"){
        print(i)
        reg = freq_gen(final_survey_data,colnames(final_survey_data)[i], "secA_q2")
        write.table(reg[[2]], "myDF3.csv", sep = ",", col.names = !file.exists("myDF3.csv"), append = T)
        dummytab <- generate_dummy_tabs(reg)
        write.table(dummytab, "myDF3.csv", sep = ",", col.names = !file.exists("myDF3.csv"), append = T)
        
      }else{
        print("No changes")
      }
      
    }
    
  }

Batch(dataB)
setwd("~/Documents/upwork/Georges")
write.csv(final_survey_data, "finalsurvey.csv")
final_survey_data <-read.csv("finalsurvey.csv")

#---------- Batch cross tabulation-------------------------------

freq_gen <- function(data,colname,colname2){
  var <- data.frame(table(data[,c(colname)], data[,c(colname2)]))
  var$Total_percentage<- round(var$Freq/sum(var$Freq)*100,2)
  sum_var2 <- levels(final_survey_data[,c(colname2)])
  #sum_var2 <- levels(final_survey_data[,c("secA_q2")])
  var$Var2_total <- 0
  n_of_rows = nrow(var)
  n_of_levels <- length(sum_var2)
  
  for (j in 1:n_of_rows) {
    
    for (k in 1:n_of_levels) {
      print(sum_var2[k])
      if (var[j,c("Var2")] == sum_var2[k]) {
        var[j,c("Var2_total")] <-filter(var, Var2==sum_var2[k]) %>% select(Freq) %>% sum()
        
      }
      
    }
  }
  
  
  sum_var1 <- levels(final_survey_data[,c(colname)])
  #sum_var1 <- levels(final_survey_data[,c("selected_region")])
  var$Var1_total <- 0
  n_of_rows1 = nrow(var)
  n_of_levels1 <- length(sum_var1)
  
  for (j in 1:n_of_rows1) {
    
    for (k in 1:n_of_levels1) {
      print(sum_var1[k])
      if (var[j,c("Var1")] == sum_var1[k]) {
        var[j,c("Var1_total")] <-filter(var, Var1==sum_var1[k]) %>% select(Freq) %>% sum()
        
      }
      
    }
  }
  
  #colnames(var)[1]<-c(colname)
  var$Var2Percentage <- round(var$Freq/var$Var2_total*100,2)
  var$Var1Percentage <- round(var$Freq/var$Var1_total*100,2)
  var$grandtotal <- sum(var$Freq)
  var %>% arrange(Var1,Var2)
  #2125
  rowstot <-2125
  df <- var %>% select(Var1,Var2,Freq,Var1_total,Var1Percentage, Var2_total,Var2Percentage,grandtotal,Total_percentage)
  df$result <- paste(df$Freq,"(",df$Var2Percentage,")",sep = "") 
  df$result2 <- paste(df$Var1_total,"(",round(df$Var1_total/rowstot*100,2),")",sep = "") 
  colnames(df) <-c(colname,colname2,"Freq",paste(colname,"total"), paste(colname,"%"),
                   paste(colname2,"total"), paste(colname2,"%"),"Grand total","Total %",paste(colname2,"_"),"row_sum")
  var_header = rbind.data.frame(c(colnames(df)))
  names(var_header) <- colnames(df)
  var_final <- rbind(var_header,df)
  var_footer <- cbind.data.frame("*","*","*","*","*","*","*","*","*","*","*")
  names(var_footer) <- colnames(df)
  var_final2 <- rbind(var_final,var_footer)
  dfs = list(df,var_final2)
  return(dfs)
}

var1 = freq_gen(final_survey_data,"selected_region","secA_q2")

generate_dummy_tabs <- function(df){
  df_1 <- df[[1]]
  df_red <-df_1 %>% select(colnames(df_1)[1],colnames(df_1)[2],colnames(df_1)[10],colnames(df_1)[11])
  mn <- reshape(df_red, idvar = colnames(df_red)[1], timevar = colnames(df_red)[2], direction = "wide")
  m <- mn %>% select(-colnames(mn)[3])
  colnames(m)[4] <- c("Total")
  var_header = rbind.data.frame(c(colnames(m)))
  names(var_header) <- colnames(m)
  var_final <- rbind(var_header,m)
  var_footer <- cbind.data.frame("*","*","*","*")
  names(var_footer) <- colnames(m)
  var_final2 <- rbind(var_final,var_footer)
  var_final2
}

z <- generate_dummy_tabs(var1)


write.table(z, "myDF3.csv", sep = ",", col.names = !file.exists("myDF3.csv"), append = T)



summing_across<-function(n_of_rows,n_of_levels,v1 = "Var2", v2="Var2_total", Var2, sum_var2){
  for (j in 1:n_of_rows) {
    
    for (k in 1:n_of_levels) {
      print(sum_var2[k])
      if (var[j,c(v1)] == sum_var2[k]) {
        var[j,c(v2)] <-filter(var, Var2==sum_var2[k]) %>% select(Freq) %>% sum()
        
      }
      
    }
  }
  
}


summing_across(n_of_rows,n_of_levels,v1 = "Var2", v2="Var2_percent", Var2, sum_var2)
