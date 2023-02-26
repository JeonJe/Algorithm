-- 코드를 입력하세요
SELECT
    FLAVOR
FROM
    FIRST_HALF
WHERE
    TOTAL_ORDER > 3000 and 
    FLAVOR in ('peach', 'watermelon', 'mango', 'strawberry','melon','orange','pineapple')
ORDER BY
    FLAVOR
    