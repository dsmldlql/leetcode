# v1

# Write your MySQL query statement below

SELECT e.name AS Employee
  FROM (SELECT *
          FROM Employee
         WHERE managerId IS NOT Null) AS e
LEFT JOIN (SELECT *
             FROM Employee) AS m
 ON e.managerId = m.Id
WHERE e.salary > m.salary


# v2

# Write your MySQL query statement below

select a.name as Employee
from Employee a, Employee b
where a.managerId = b.id and a.salary > b.salary