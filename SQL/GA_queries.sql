
SELECT sum(metric_count) FROM non_virtual_ga_metrics  WHERE metric = 'sessions' AND from_date between '2021-05-30' and '2021-06-05' ;


/*SELECT sum(metric_count) FROM non_virtual_ga_metrics  WHERE metric = 'users' AND from_date between '2021-05-30' and '2021-06-05' ;


SELECT sum(metric_count) FROM non_virtual_ga_metrics   WHERE segment = 'Organic Search - Destination Pages' AND from_date between '2021-05-30' and '2021-06-05'   */

/*sessions (excluding virtual) for last 7 days
/*users (excluding virtual) for last 7 days
/*Sessions from Organic Search (excluding virtual) for last 7 days.*/



SELECT sum(metric_count) FROM non_virtual_ga_metrics  WHERE metric = 'sessions' AND from_date >= (select DATE_SUB(from_date, INTERVAL 6 DAY) from non_virtual_ga_metrics where {{end_date}} limit 1) AND
from_date <= (select from_date from non_virtual_ga_metrics where {{end_date}} limit 1)

 

SELECT sum(metric_count) FROM non_virtual_ga_metrics  WHERE metric = 'users' AND from_date >= (select DATE_SUB(from_date, INTERVAL 6 DAY) from non_virtual_ga_metrics where {{end_date}} limit 1) AND
from_date <= (select from_date from non_virtual_ga_metrics where {{end_date}} limit 1)
 


SELECT sum(metric_count) FROM non_virtual_ga_metrics   WHERE segment = 'Organic Search - Destination Pages' AND 
from_date >= (select DATE_SUB(from_date, INTERVAL 6 DAY) from non_virtual_ga_metrics where {{end_date}} limit 1) AND
from_date <= (select from_date from non_virtual_ga_metrics where {{end_date}} limit 1)



SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date = '2021-06-13'



/* manual pull */
SELECT metric_count FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date = (select DATE_SUB(to_date, INTERVAL 1 DAY) from non_virtual_ga_metrics where {{end_date}} limit 1) and from_date != to_date


/* USERS : users (excluding virtual) for last 7 days*/
SELECT metric_count FROM non_virtual_ga_metrics  
WHERE metric = 'users'   AND segment = 'Excluding people who land on virtual' 
AND to_date = DATE_SUB(DATE(NOW()), INTERVAL 1 DAY) and from_date != to_date


/* SESSIONS : sessions (excluding virtual) for last 7 days*/
SELECT metric_count FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date = DATE_SUB(DATE(NOW()), INTERVAL 1 DAY) and from_date != to_date


/* SESSIONS : Sessions from Organic Search (excluding virtual) for last 7 days.*/
SELECT metric_count FROM non_virtual_ga_metrics  
WHERE metric = 'sessions' AND segment = 'Organic Search Non virtual' 
AND to_date = (select DATE_SUB({{end_date}} , INTERVAL 1 DAY)) and from_date != to_date


/*working soln */

/*sessions*/
SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 1 DAY)) and from_date != to_date


SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 8 DAY)) and from_date != to_date


SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 30 DAY)) and from_date != to_date

/*users */

SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 1 DAY)) and from_date != to_date


SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 8 DAY)) and from_date != to_date


SELECT * FROM non_virtual_ga_metrics  
WHERE metric = 'sessions'   AND segment = 'Excluding people who land on virtual' 
AND to_date =(select DATE_SUB({{end_date}} , INTERVAL 30 DAY)) and from_date != to_date


/* SESSIONS : Sessions from Organic Search (excluding virtual) for last 7 days.*/
SELECT metric_count FROM non_virtual_ga_metrics  
WHERE metric = 'sessions' AND segment = 'Organic Search Non virtual' 
AND to_date = (select DATE_SUB({{end_date}} , INTERVAL 1 DAY)) and from_date != to_date


