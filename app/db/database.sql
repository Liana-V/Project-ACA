CREATE TABLE IF NOT EXISTS USERS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  first_name TEXT ,
  last_name TEXT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  age INTEGER,
  phone TEXT UNIQUE ,
  gender TEXT,
  education TEXT,
  image_file TEXT DEFAULT 'default.png' NOT NULL,
  experience TEXT
);

CREATE TABLE IF NOT EXISTS USER_SKILLS  (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  skill_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  level_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS LEVEL (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  level_name TEXT
);
REPLACE INTO LEVEL (id,level_name)
VALUES(1,'Student '),(2,'Junior '),(3,'Mid level'),(4,'Senior'),(5,'C level'),(6,'Not defined');

CREATE TABLE IF NOT EXISTS CATEGORY (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cat_name TEXT
);

REPLACE INTO CATEGORY (id,cat_name)
VALUES(1,'Software development'),(2,'Quality Assurance /Control'),(3,'Web/Graphic design'),
(4,'Product/Project Management'),(5,'Hardware design'),(6,'Other IT'),
(7,'Sales/service management'),(8,'Administrative/office-work'),(9,'Tourism/Hospitality/HoReCa'),
(10,'Marketing/Advertising'),(11,'Communications/Journalism/PR'),(12,'Accounting/Bookkeeping/Cash register'),
(13,'Finance Management'),(14,'Banking/credit'),(15,'TV/Radio/Entertainment'),
(16,'Education/training'),(17,'Legal'),(18,'Audit/Compliance'),
(19,'Healthcare/Pharmaceutical'),(20,'Healthcare/Pharmaceutical'),(19,'Human Resources'),(21,'Sports/Beauty'),
(22,'Procurement/Logistics/Courier '),(23,'Production'),(24,'Business/Management '),
(25,'Art/Design/Architecture'),(26,'General/professional/Other services'),(27,'IT security/Networks'),
(28,'NGO/Nonprofit'),(29,'Insurance'),(30,'Hospitality/Entertainment'),(31,'Data Science/Data Analytics'),
(32,'Foreign language'),(33,'Economics'),
(34,'Hardware Design / Engineering'),(35,'Data Collection & Analytics'),(36,'Mechanical'),(37,'System Admin/Engineer'),
(38,'Retail business'),(39,'Network Administration'),(40,'Consultancy'),(41,'Content writing'),(42,'Security')

;

CREATE TABLE IF NOT EXISTS SAVED_JOBS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  job_id INTEGER NOT NULL
);

