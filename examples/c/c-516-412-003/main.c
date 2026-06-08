/* db.c — детали скрыты */
struct Database {
    FILE *log;
    /* внутренние поля */
};

void db_close(Database *db)
{
    if (db == NULL)
        return;
    if (db->log != NULL)
        fclose(db->log);
    free(db);
}
