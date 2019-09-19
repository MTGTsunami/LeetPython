"""
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.


Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State
"""

# Write your MySQL query statement below
"""
SELECT per.FirstName, per.LastName, addr.City, addr.State
FROM Person per, Address addr
WHERE per.PersonId = addr.PersonId
UNION
SELECT per.FirstName, per.LastName, NULL as City, NULL as State
FROM Person per
WHERE per.PersonId NOT IN (SELECT PersonId from Address);
"""


# left join answer
"""
select FirstName, LastName, City, State
from Person
left join Address
on Person.PersonId = Address.PersonId;
"""
