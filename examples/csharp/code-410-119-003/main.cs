protected override void Up(MigrationBuilder migrationBuilder)
{
    migrationBuilder.Sql(@"
        ALTER TABLE teams
        DROP CONSTRAINT IF EXISTS teams_lead_id_fkey;

        ALTER TABLE teams
        ADD CONSTRAINT teams_lead_id_fkey
        FOREIGN KEY (lead_id) REFERENCES employees(id)
        DEFERRABLE INITIALLY DEFERRED;
    ");
}
