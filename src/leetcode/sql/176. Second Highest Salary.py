"""
Write a sql query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""


# Write your MySQL query statement below
"""
select (select distinct salary
        from employee 
        order by salary desc
        limit 1 offset 1)
as SecondHighestSalary;
"""


# Write your MySQL query statement below
"""
select max(Salary) as SecondHighestSalary 
from Employee
where Salary < (select max(Salary) from Employee)
"""

