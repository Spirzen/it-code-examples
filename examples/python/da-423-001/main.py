# Порог "подозрительного" расстояния между транзакциями (км)
GEO_ANOMALY_KM = 500

def check_transaction(txn, last_location):
    if txn.amount > 100_000:
        flag_high_value(txn)

    # distance_km — функция из вашей геобиблиотеки (haversine и т.п.)
    if distance_km(txn.location, last_location) > GEO_ANOMALY_KM:
        flag_geo_anomaly(txn)

    return True

def flag_high_value(transaction):
    send_alert_to_security(transaction)
    log_event("High value transaction", transaction)

def flag_geo_anomaly(transaction):
    trigger_two_factor_auth(transaction.user_id)
    log_event("Suspicious geo location", transaction)
