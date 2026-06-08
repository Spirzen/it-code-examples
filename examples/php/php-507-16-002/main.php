$action = 'delete';

switch ($action) {
    case 'create':
        $id = createRecord();
        if ($id > 0) {
            notifyUser($id);
        }
        break;
    case 'update':
        updateRecord($id);
        logChange();
        break;
    case 'delete':
        deleteRecord($id);
        logChange();
        break;
    default:
        echo "Неизвестное действие";
}
