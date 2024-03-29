SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM USED_GOODS_REPLY B
JOIN USED_GOODS_BOARD A ON B.BOARD_ID = A.BOARD_ID
WHERE MONTH(A.CREATED_DATE) = 10
ORDER BY B.CREATED_DATE, A.TITLE