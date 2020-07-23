CREATE TABLE IF NOT EXISTS USERS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  age INTEGER,
  phone TEXT UNIQUE NOT NULL,
  gender TEXT NOT NULL,
  education TEXT,
  image,
  experience TEXT
);

CREATE TABLE IF NOT EXISTS USER_SKILLS  (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  skill_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL
  level_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS LEVEL (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  level_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS JOBS_SKILLS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id INTEGER NOT NULL
  skill_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS SKILLS  (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  skill_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT JOBS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category TEXT,
  company TEXT NOT NULL,
  title TEXT NOT NULL,
  deadline TEXT,
  job_responsibilities TEXT,
  required TEXT,
  specialist_level TEXT

);

CREATE TABLE IF NOT EXISTS SAVED_JOBS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  job_id INTEGER NOT NULL
);
