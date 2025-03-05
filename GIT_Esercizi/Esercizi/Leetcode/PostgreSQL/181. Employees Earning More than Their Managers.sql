Select e.name
from Employee e
join Employee m on e.managerid = m.id
where e.salary > m.salary