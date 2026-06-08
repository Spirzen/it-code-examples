CREATE TABLE teams (
    id      SERIAL PRIMARY KEY,
    name    TEXT NOT NULL,
    lead_id INT
);

CREATE TABLE employees (
    id      SERIAL PRIMARY KEY,
    name    TEXT NOT NULL,
    team_id INT
);

ALTER TABLE teams
    ADD CONSTRAINT teams_lead_id_fkey
    FOREIGN KEY (lead_id) REFERENCES employees(id)
    DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE employees
    ADD CONSTRAINT employees_team_id_fkey
    FOREIGN KEY (team_id) REFERENCES teams(id)
    DEFERRABLE INITIALLY DEFERRED;
