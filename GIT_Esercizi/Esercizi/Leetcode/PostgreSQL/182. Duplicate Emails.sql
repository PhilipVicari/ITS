select distinct p.email as Email
from Person p
join Person Pe on Pe.email = p.email
where Pe.id != p.id