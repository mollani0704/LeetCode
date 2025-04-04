SELECT
    a.name AS Employee
FROM 
    Employee A
INNER JOIN (
    SELECT 
        id,
        salary
    FROM 
        Employee
) B
    ON B.id = A.managerId
where a.salary > b.salary
