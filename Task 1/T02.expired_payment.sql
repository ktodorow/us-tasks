WITH latest_borrows AS
(
SELECT
        pe.id,
        pe.user_id,
        pe.product_id,
        pe.evt_date AS borrow_date,
		json_extract_path_text(ue.meta::json, 'valid_until') AS valid_until
    FROM
        product_events AS pe
    JOIN
        user_events AS ue ON pe.user_id = ue.user_id
    WHERE
        pe.evt_type = 'borrow' 
		AND ue.evt_type = 'add-payment-method'
)

SELECT
    lb.id,
    lb.user_id,
    lb.product_id,
    lb.borrow_date,
    lb.valid_until
FROM
    latest_borrows AS lb
WHERE
    TO_DATE(lb.valid_until, 'MM/YY') IS NOT NULL
    AND (TO_DATE(lb.valid_until, 'MM/YY') <= CURRENT_DATE + INTERVAL '30 days'
         OR TO_DATE(lb.valid_until, 'MM/YY') < CURRENT_DATE);