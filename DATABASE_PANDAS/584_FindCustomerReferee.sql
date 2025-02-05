-- query = all name of customer's referred to by customer_id !=2

select 'name' 
from cusomters
where referee_id != 2 or referee_id is null
