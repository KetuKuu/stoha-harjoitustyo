
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);

CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    choice TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices,
    sent_at TIMESTAMP
);

CREATE TABLE completions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    region TEXT,
    completion_date TIMESTAMP DEFAULT NOW()
);
