# Write your MySQL query statement below
SELECT
    MAX(A.num) AS num
FROM 
    MyNumbers A
JOIN   
    (SELECT num, count(*) AS count from MyNumbers group by num) B
    ON B.num = A.num
WHERE B.count = 1