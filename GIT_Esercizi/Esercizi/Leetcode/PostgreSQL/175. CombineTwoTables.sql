Select p.firstName, p.lastName, a.city, a.state
from Person p
left outer join Address a on a.personid = p.personid