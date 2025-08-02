-- First query
SELECT 
    t.date AS vente, 
    SUM(t.prod_price * t.prod_qty) AS total_vente
FROM TRANSACTIONS t
WHERE t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY t.date
ORDER BY t.date;

-- Second query
SELECT 
    t.client_id,
    SUM(CASE WHEN pn.product_type = 'MEUBLE' 
             THEN t.prod_price * t.prod_qty 
             ELSE 0 END) AS ventes_meuble,
    SUM(CASE WHEN pn.product_type = 'DECO' 
             THEN t.prod_price * t.prod_qty 
             ELSE 0 END) AS ventes_deco
FROM TRANSACTIONS t
INNER JOIN PRODUCT_NOMENCLATURE pn
    ON t.prod_id = pn.product_id
WHERE t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY t.client_id;
