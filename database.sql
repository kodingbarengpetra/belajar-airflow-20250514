-- install uuid-ossp extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    id UUID PRIMARY KEY NOT NULL DEFAULT uuid_generate_v4(),
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (id, username, email) VALUES
    ('123e4567-e89b-12d3-a456-426614174000', 'user1', 'user1@example.com'),
    ('123e4567-e89b-12d3-a456-426614174001', 'user2', 'user2@example.com'),
    ('123e4567-e89b-12d3-a456-426614174002', 'user3', 'user3@example.com'),
    ('123e4567-e89b-12d3-a456-426614174003', 'user4', 'user4@example.com'),
    ('123e4567-e89b-12d3-a456-426614174004', 'user5', 'user5@example.com');

SELECT * FROM users;
