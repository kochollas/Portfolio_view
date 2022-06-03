

/* Version 4 */



SELECT  c.id, c.name as Name,  m.name as Market,/*v.name as Venue*/case when v.name is null then 'Not Finalized' else v.name end as Venue, case
	when package_name='Bloom Package' or package_name='Bloom' or package_name='Bloom - Holiday' or package_name='Bloom - Sun Valley' then 'Bloom'
	when package_name='Custom Package for Alan Riche - Virtual Officiant Only' or package_name='Shauni Tiller' 
or package_name='Traveling Hopfs - Domestic'  then 'Custom'
	when package_name='Day of Helper' then 'Day of Helper'
	when package_name='Oasis' or package_name='Oasis - Grand Canyon' then 'Oasis'
	when package_name='Seed' or package_name='Seed Package' or package_name='Seed - Holiday' or package_name='Seed - Sun Valley' then 'Seed'
	when package_name='Simply Photographed' or package_name='Simply Photos' or package_name='Simply Photos - Holiday'  then 'Simply Photos'
	when package_name='Simply Video' then 'Simply Video'
	when package_name='Sprout' or package_name='Sprout' or package_name='Sprout - SV' or package_name='Sprout Holiday' or package_name='Sprout Package' or package_name='Sprout- Holiday' then 'Sprout'
	when package_name='Urban Wildflower- Holiday' or package_name='Urban Wildflower' then 'Urban Wildflower'
	when package_name='Virtual Ceremony' then 'Virtual'
	when package_name='Virtual Wedding Tech and Planning Support' then 'Virtual tech and Support'
	when package_name='Wildflower' or package_name='Wildflower Holiday' or package_name='Wildflower Package' then 'Wildflower'
	else 'No Package Category'	
end as Package, case when c.postponed = 1 then 'postponed' when c.cancel =1 then 'cancelled' when c.archive =1 then 'archived'  else 'Active' end as status,

c.wedding_date as `Ceremony Date`, c.cancel_date as `Date Cancelled`,c.postponed_at as `Date Postponed` , c.deposit_amount  /*J*/, c.created_at as `Deposit Date`, 

c.invoice_amount as `Total Invoice Amount`,  /* L */

/*m2.discount as 'Discount', */

round(c.deposit_amount + c.invoice_amount,2) as `Total Price`,  /* J+L */

round(c.vn_amount_with_spo - case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end,2) as `Total Invoice Cost`, /*P*/
case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end as sale_tax, /*Q*/

round(c.invoice_amount- round(c.vn_amount_with_spo - case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end,2) - case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end,2) as `Invoice Profit`,

c.deposit_amount + round(c.invoice_amount - round(c.vn_amount_with_spo - case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end,2) - case when tab1.sale_tax is null then 0 when tab1.sale_tax is not null then tab1.sale_tax end,2) as `Total Profit`
,

d01.`sum(c1.officiant_cost)` as officiant_cost, d01.`sum(c1.officiant_invoiced)` as officiant_invoiced, 

d02.`sum(c2.photo_cost)` as photo_cost, d02.`sum(c2.photo_invoiced)` as photo_invoiced,


dd5.`sum(b1.flower_cost)` as flower_cost, dd5.`sum(b1.flower_invoiced)` as flower_invoiced,

d03.`sum(c3.video_cost)` as video_cost, d03.`sum(c3.video_invoiced)` as video_invoiced,

d5.`sum(a1.hmu_cost)` as hmu_cost, d5.`sum(a1.hmu_invoiced)` as hmu_invoiced, 

d04.`sum(c4.permit_cost)` as permit_cost, d04.`sum(c4.permit_invoiced)` as permit_invoiced,

d7.`sum(a2.travel_cost)` as travel_cost, d7.`sum(a2.travel_invoiced)` as travel_invoiced,
d8.`sum(a3.violin_cost)` as violin_cost, d8.`sum(a3.violin_invoiced)` as violin_invoiced,

d9.`sum(a4.DOH_cost)` as DOH_cost,d9.`sum(a4.DOH_invoiced)` as DOH_invoiced ,

others.`sum(Os.Other_cost)` as Other_cost, others.`sum(Os.Other_invoiced)` as Other_invoiced

FROM customer c 
left join market m 
on m.id = c.market_id 
left join venues v 
on v.id = c.venue_id 
left join
(select  customer_id,total as sale_tax  from purchase_item where service_type='sales tax'
) as tab1 on tab1.customer_id = c.id
/* The query runs for long when this part is added
left join
(select  customer_id,total as discount  from purchase_item where service_type='discount'
)as m2 on m2.customer_id = c.id  */

left join
(select c1.customer_id, sum(c1.officiant_cost),sum(c1.officiant_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as officiant_cost, sum(total) as officiant_invoiced from purchase_item group by customer_id, service_type having service_type like 'officiant%' ) as c1 group by c1.customer_id
)as d01 on d01.customer_id = c.id 


left join
(select c2.customer_id, sum(c2.photo_cost),sum(c2.photo_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as photo_cost, sum(total) as photo_invoiced from purchase_item group by customer_id, service_type having service_type like 'photograph%' ) as c2 group by c2.customer_id
)as d02 on d02.customer_id = c.id 




left join 
(
select b1.customer_id, sum(b1.flower_cost),sum(b1.flower_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as flower_cost, sum(total) as flower_invoiced from purchase_item group by customer_id, service_type having service_type like 'flower%' ) as b1 group by b1.customer_id
)as dd5 on dd5.customer_id = c.id


left join 
(select c3.customer_id, sum(c3.video_cost),sum(c3.video_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as video_cost, sum(total) as video_invoiced from purchase_item group by customer_id, service_type having service_type like 'video%' ) as c3 group by c3.customer_id
)as d03 on d03.customer_id = c.id 




left join
(
select a1.customer_id, sum(a1.hmu_cost),sum(a1.hmu_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as hmu_cost, sum(total) as hmu_invoiced from purchase_item group by customer_id, service_type having service_type like 'hmu%' ) as a1 group by a1.customer_id
)as d5 on d5.customer_id = c.id


left join
(select c4.customer_id, sum(c4.permit_cost),sum(c4.permit_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as permit_cost, sum(total) as permit_invoiced from purchase_item group by customer_id, service_type having service_type like 'permit%' ) as c4 group by c4.customer_id
)as d04 on d04.customer_id = c.id 


left join
(select a2.customer_id, sum(a2.travel_cost),sum(a2.travel_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as travel_cost, sum(total) as travel_invoiced from purchase_item group by customer_id, service_type having service_type like 'travel%' ) as a2 group by a2.customer_id
)as d7 on d7.customer_id = c.id 

left join

(select a3.customer_id, sum(a3.violin_cost),sum(a3.violin_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as violin_cost, sum(total) as violin_invoiced from purchase_item group by customer_id, service_type having service_type like 'violin%'  ) as a3 group by a3.customer_id
)as d8 on d8.customer_id = c.id 

left join

(select a4.customer_id, sum(a4.DOH_cost),sum(a4.DOH_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as DOH_cost, sum(total) as DOH_invoiced from purchase_item group by customer_id, service_type having service_type like 'Day of Helper%'  or 
service_type like 'On-site Helper%' ) as a4 group by a4.customer_id
)as d9 on d9.customer_id = c.id 

left join
(select Os.customer_id, sum(Os.Other_cost), sum(Os.Other_invoiced) from (select distinct customer_id, service_type, sum(vn_amount_with_spo) as Other_cost, sum(total) as Other_invoiced from purchase_item group by customer_id, service_type having service_type not like 'officiant%' and service_type not like 'photograph%' and service_type not like 'flower%'
and service_type not like 'video%' and service_type not like 'hmu%' and service_type not like 'permit%' and service_type not like 'travel%' and 
service_type not like 'violin%' and service_type not like 'Day of Helper%' and service_type not like 'On-site Helper%' and service_type != 'Sales Tax' and service_type != 'discount' 
 
) as Os group by Os.customer_id

) as others on others.customer_id = c.id 

where c.id in(97194, 97376,97329,97297,87173,97088,95450,95900, 104724 ) 


























