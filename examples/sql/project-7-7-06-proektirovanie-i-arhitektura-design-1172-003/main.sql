BEGIN;
  UPDATE payouts SET status = 'completed', updated_at = now()
  WHERE id = 'po_7f3c9a2e';

  INSERT INTO outbox (id, aggregate_type, aggregate_id, event_type, payload, created_at)
  VALUES (
    'evt_01JABC123',
    'payout',
    'po_7f3c9a2e',
    'payout.completed',
    '{"payoutId":"po_7f3c9a2e","amount":{"value":"1500.00","currency":"RUB"},"status":"completed"}',
    now()
  );
COMMIT;
