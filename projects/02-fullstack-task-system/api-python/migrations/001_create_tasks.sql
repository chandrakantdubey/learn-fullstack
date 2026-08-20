CREATE TABLE IF NOT EXISTS tasks (
    id UUID PRIMARY KEY,
    owner_id UUID NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_tasks_owner_created
    ON tasks (owner_id, created_at DESC);
