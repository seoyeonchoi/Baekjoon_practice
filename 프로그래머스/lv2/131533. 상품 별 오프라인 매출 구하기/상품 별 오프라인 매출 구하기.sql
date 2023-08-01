-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, SUM(P.PRICE * O.SALES_AMOUNT)
    FROM PRODUCT AS P
        JOIN OFFLINE_SALE AS O ON P.PRODUCT_ID = O.PRODUCT_ID
    GROUP BY P.PRODUCT_CODE
    ORDER BY 2 DESC, 1