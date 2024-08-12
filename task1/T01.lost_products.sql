WITH last_product_events AS (
    SELECT
        product_id,
        evt_type,
        MAX(evt_date) AS last_evt_date
    FROM
        product_events
    WHERE
        evt_type = 'borrow'
    GROUP BY
        product_id, evt_type
),
lost_products AS (
    SELECT
        product_id, 
		evt_type, 
		last_evt_date
    FROM
        last_product_events 
    WHERE
        last_evt_date <= CURRENT_DATE - INTERVAL '3 months'
)	

SELECT
    product_id, 
	evt_type, 
	last_evt_date
FROM
    lost_products