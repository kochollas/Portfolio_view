
# Bookings solution  

SELECT  c.id, c.name as Name,  m.name as Market , c.created_at, c.wedding_date, p_i.service_type, p_i.total, p_i.date `bookings date`,
case 
	when datediff(p_i.date, c.created_at) = 0 then 'Day of Deposit'
	when datediff(p_i.date, c.created_at) > 0 and  datediff(p_i.date, c.created_at) <=7 then 'Within 7 days of Deposit'
	when datediff(p_i.date, c.created_at) > 7 and  datediff(c.wedding_date, p_i.date) >= 7 then 'After 7 days of deposit and 7 days before ceremony'
	when datediff(c.wedding_date, p_i.date) <= 7 then '7 days before ceremony'
	
	else 'None'
end as Booking_time
FROM customer c 
left join market m 
on m.id = c.market_id 

left join purchase_item p_i
on p_i.customer_id = c.id

/* Average number of days between bookig and wedding */

SELECT AVG(t1.`datediff(c.wedding_date, c.created_at)`) as 'Avg days' FROM
(
SELECT c.id, m.name as Market, c.created_at,c.wedding_date, datediff(c.wedding_date, c.created_at) FROM 
customer c 
LEFT JOIN market m ON m.id = c.market_id 
WHERE c.created_at between '2021-01-01' and '2021-05-29' and c.wedding_date between '2021-01-01' and '2021-05-29' 
) as t1


/* Median number of days between bookig and wedding */
/*----------------------------------------------------------------------------------------------------------------------------------*/

SET @rowindex := -1;

SELECT AVG(T3.daysCount) AS median_days FROM(
SELECT T2.rowindex, T2.daysCount
FROM
(
SELECT @rowindex:=@rowindex + 1 AS rowindex,T1.`datediff(c.wedding_date, c.created_at)` AS daysCount 
FROM
(
SELECT c.id, m.name as Market, c.created_at,c.wedding_date, datediff(c.wedding_date, c.created_at) FROM 
customer c 
LEFT JOIN market m ON m.id = c.market_id 
WHERE /*c.id in(97194, 97376,97329,97297,87173,97088,95450,95900) /*and */ c.created_at between '2021-01-01' and '2021-05-29' and c.wedding_date between '2021-01-01' and '2021-05-29'
) T1 ORDER BY T1.`datediff(c.wedding_date, c.created_at)`, (SELECT @rownum:=0) r
) T2 WHERE T2.rowindex IN(FLOOR(@rowindex / 2) , CEIL(@rowindex / 2))) AS T3



SELECT AVG(dd.val) as median_val
FROM (
SELECT d.val, @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum
  FROM data d, (SELECT @rownum:=0) r
  WHERE d.val is NOT NULL
  -- put some where clause here
  ORDER BY d.val
) as dd
WHERE dd.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) );





SELECT AVG(T2.dayscount) as median_days FROM
(
    SELECT T1.dayscount, T1.row_number FROM
    (
        SELECT d.`datediff(c.wedding_date, c.created_at)` as dayscount,@rownum:=@rownum+1 as `row_number`,  @total_rows:=@rownum
        FROM
        (
        SELECT c.id, m.name as Market, c.created_at,c.wedding_date, datediff(c.wedding_date, c.created_at) FROM 
        customer c 
        LEFT JOIN market m ON m.id = c.market_id 
        WHERE  c.created_at between '2021-01-01' and '2021-05-29' and c.wedding_date between '2021-01-01' and '2021-05-29' /*more conditions */
        ) d, (SELECT @rownum := -1) r
        WHERE d.`datediff(c.wedding_date, c.created_at)` IS NOT NULL
        ORDER BY d.`datediff(c.wedding_date, c.created_at)` 
    ) AS T1
) as T2 WHERE T2.row_number IN(FLOOR(@total_rows / 2) , CEIL(@total_rows / 2))











