SELECT
    A.name,
    B.bonus
FROM
    EMPLOYEE A
LEFT OUTER JOIN BONUS B
    ON B.empId = A.empId
WHERE B.bonus < 1000 or Isnull(b.bonus)