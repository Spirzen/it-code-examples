sqlite3_stmt *stmt = NULL;
int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
if (rc != SQLITE_OK)
    goto fail;

rc = sqlite3_step(stmt);
if (rc != SQLITE_DONE)
    goto fail;

sqlite3_finalize(stmt);
return 0;

fail:
    if (stmt != NULL)
        sqlite3_finalize(stmt);
    fprintf(stderr, "%s\n", sqlite3_errmsg(db));
    return 1;
