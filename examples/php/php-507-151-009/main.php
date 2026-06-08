function sendToCRM($data) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://crm.example.com/api/leads');
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . CRM_API_KEY
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

// После успешной валидации
sendToCRM([
    'email' => $_POST['email'],
    'name' => $_POST['name']
]);
