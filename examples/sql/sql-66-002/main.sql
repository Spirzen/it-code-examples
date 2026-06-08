INSERT INTO shop_data.events (account_id, event_type, source, created_at, payload)
VALUES
(1, 'order_created', 'web', '2026-05-15 10:03:00+00', '{
  "order": {"id": "ORD-1001", "status": "new", "currency": "RUB", "total": 12450.75},
  "customer": {"id": 201, "segment": "b2c", "city": "Moscow"},
  "delivery": {"method": "courier", "eta_days": 2},
  "items": [
    {"sku": "KB-001", "qty": 1, "price": 8450.50, "tags": ["keyboard", "wireless"]},
    {"sku": "MS-009", "qty": 2, "price": 2000.125, "tags": ["mouse", "gaming"]}
  ],
  "flags": {"is_priority": true, "is_gift": false},
  "metrics": {"discount_pct": 5.5, "weight_kg": 1.85}
}'::jsonb),
(1, 'order_paid', 'web', '2026-05-15 10:10:00+00', '{
  "order": {"id": "ORD-1001", "status": "paid", "currency": "RUB", "total": 12450.75},
  "payment": {"method": "card", "provider": "tbank", "paid_amount": 12450.75},
  "items": [
    {"sku": "KB-001", "qty": 1, "price": 8450.50},
    {"sku": "MS-009", "qty": 2, "price": 2000.125}
  ],
  "flags": {"is_priority": true, "is_gift": false},
  "metrics": {"discount_pct": 5.5, "fraud_score": 0.02}
}'::jsonb),
(2, 'order_created', 'mobile', '2026-05-16 07:01:00+00', '{
  "order": {"id": "ORD-1002", "status": "new", "currency": "RUB", "total": 8900.00},
  "customer": {"id": 305, "segment": "b2b", "city": "Kazan"},
  "items": [
    {"sku": "MON-01", "qty": 1, "price": 7900.00, "tags": ["monitor"]},
    {"sku": "HDMI-2", "qty": 2, "price": 500.00, "tags": ["cable"]}
  ],
  "flags": {"is_priority": false, "is_gift": false},
  "metrics": {"discount_pct": 0, "weight_kg": 4.2}
}'::jsonb),
(2, 'order_cancelled', 'mobile', '2026-05-16 07:35:00+00', '{
  "order": {"id": "ORD-1002", "status": "cancelled", "currency": "RUB", "total": 8900.00},
  "reason": {"code": "CLIENT_CHANGED_MIND"},
  "flags": {"is_priority": false},
  "metrics": {"cancel_fee": 0}
}'::jsonb),
(3, 'order_created', 'api', '2026-05-17 09:11:00+00', '{
  "order": {"id": "ORD-1003", "status": "new", "currency": "USD", "total": 210.99},
  "customer": {"id": 881, "segment": "b2b", "city": "Almaty"},
  "items": [
    {"sku": "SSD-1T", "qty": 1, "price": 120.50},
    {"sku": "RAM-32", "qty": 1, "price": 90.49}
  ],
  "flags": {"is_priority": true, "is_export": true},
  "metrics": {"discount_pct": 2.25, "weight_kg": 0.2}
}'::jsonb),
(1, 'shipment_created', 'worker', '2026-05-17 10:45:00+00', '{
  "order": {"id": "ORD-1001", "status": "paid"},
  "shipment": {"id": "SHP-301", "carrier": "cdek", "warehouse": "MSK-1"},
  "items": [
    {"sku": "KB-001", "qty": 1},
    {"sku": "MS-009", "qty": 2}
  ],
  "flags": {"is_priority": true}
}'::jsonb),
(3, 'order_created', 'api', '2026-05-18 08:00:00+00', '{
  "order": {"id": "ORD-1004", "status": "new", "currency": "EUR", "total": 540.40},
  "customer": {"id": 882, "segment": "b2c", "city": "Berlin"},
  "items": [
    {"sku": "CPU-I7", "qty": 1, "price": 340.40},
    {"sku": "FAN-12", "qty": 2, "price": 100.00}
  ],
  "flags": {"is_priority": false, "is_export": true},
  "metrics": {"discount_pct": 10.0}
}'::jsonb),
(2, 'order_paid', 'mobile', '2026-05-18 09:20:00+00', '{
  "order": {"id": "ORD-1005", "status": "paid", "currency": "RUB", "total": 3300.30},
  "payment": {"method": "sbp", "provider": "bank-x", "paid_amount": 3300.30},
  "items": [
    {"sku": "HUB-8", "qty": 1, "price": 2300.30},
    {"sku": "USB-C", "qty": 2, "price": 500.00}
  ],
  "flags": {"is_priority": false, "is_gift": true},
  "metrics": {"discount_pct": 1.0}
}'::jsonb),
(1, 'refund_created', 'web', '2026-05-19 13:12:00+00', '{
  "order": {"id": "ORD-1001", "status": "refund_pending"},
  "refund": {"amount": 2000.13, "reason": "damaged_item"},
  "items": [{"sku": "MS-009", "qty": 1, "price": 2000.125}],
  "flags": {"is_priority": true},
  "metrics": {"refund_ratio": 0.1606}
}'::jsonb),
(3, 'order_paid', 'api', '2026-05-20 11:04:00+00', '{
  "order": {"id": "ORD-1004", "status": "paid", "currency": "EUR", "total": 540.40},
  "payment": {"method": "wire", "provider": "bank-eu", "paid_amount": 540.40},
  "items": [
    {"sku": "CPU-I7", "qty": 1, "price": 340.40},
    {"sku": "FAN-12", "qty": 2, "price": 100.00}
  ],
  "flags": {"is_priority": false, "is_export": true},
  "metrics": {"discount_pct": 10.0, "fraud_score": 0.01}
}'::jsonb)
RETURNING event_id, account_id, event_type, created_at;
