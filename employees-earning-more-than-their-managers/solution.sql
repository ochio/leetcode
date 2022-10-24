SELECT name as Employee
FROM Employee as E
WHERE salary > (SELECT salary FROM Employee WHERE id = E.managerId)