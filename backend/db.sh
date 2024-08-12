0. login to db
docker-compose exec db psql -U postgres -d monorepo_saas_db

1. create new table

DROP TABLE IF EXISTS public.mix_user_table;

CREATE TABLE IF NOT EXISTS public.mix_user_table
(
    "ID" SERIAL PRIMARY KEY,
    "firstName" VARCHAR(50) NOT NULL,
    "lastName" VARCHAR(50) NOT NULL,
    "age" INTEGER,
    "email" VARCHAR(100) UNIQUE NOT NULL,
    "music" VARCHAR(100)
);

-- Insert data
INSERT INTO public.mix_user_table
    ("firstName", "lastName", "age", "email", "music")
VALUES 
    ('Vlady', 'Davit', 35, 'lovedev0829@gmail.com', 'Rock');