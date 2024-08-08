-- Creates an index on the `names` table to improve query performance when filtering by the first character of the `name` column and the `score` column.

CREATE INDEX idx_name_first_score ON names (name(1), score)