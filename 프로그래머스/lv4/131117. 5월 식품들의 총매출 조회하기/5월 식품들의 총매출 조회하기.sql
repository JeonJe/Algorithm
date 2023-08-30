-- 코드를 입력하세요
SELECT FR.PRODUCT_ID,FR.PRODUCT_NAME, SUM(FR.PRICE*FO.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT AS FR
JOIN FOOD_ORDER AS FO
ON FR.PRODUCT_ID = FO.PRODUCT_ID
WHERE YEAR(FO.PRODUCE_DATE) = 2022 AND MONTH(FO.PRODUCE_DATE) = 5
GROUP BY PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, FR.PRODUCT_ID
