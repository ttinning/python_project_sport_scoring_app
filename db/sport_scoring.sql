DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    away_team_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    away_team_score INT,
    home_team_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    home_team_score INT
);