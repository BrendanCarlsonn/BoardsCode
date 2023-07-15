CREATE TABLE table_PC(
PC_id int NOT NULL AUTO_INCREMENT,
character_name varchar(100) NOT NULL,
character_level varchar(100) NOT NULL,
character_class varchar(100) NOT NULL,
PRIMARY KEY (PC_id)
);

INSERT INTO table_PC
VALUES("5","Otto", "Five", "Rogue");

SELECT * FROM table_PC;

DROP TABLE table_PC;

DELETE FROM table_PC
WHERE PC_id = 1;

CREATE TABLE table_NPC(
NPC_id int NOT NULL AUTO_INCREMENT,
NPC_name varchar(100) NOT NULL,
NPC_level varchar(100) NOT NULL,
NPC_class varchar(100) NOT NULL,
PRIMARY KEY (NPC_id)
);
INSERT INTO table_NPC
VALUES("5","Gramm", "Twelve", "Warlock");

CREATE TABLE table_Enemy(
Enemy_id int NOT NULL AUTO_INCREMENT,
Enemy_name varchar(100) NOT NULL,
Enemy_level varchar(100) NOT NULL,
Enemy_class varchar(100) NOT NULL,
PC_id int,
PRIMARY KEY (Enemy_id),
CONSTRAINT FK_PC_id FOREIGN KEY (PC_id)
REFERENCES table_PC(PC_id)
);
INSERT INTO table_Enemy
VALUES("5","Drakkthar", "Twelve", "Paladin","5");

CREATE TABLE table_Location(
Location_id int NOT NULL AUTO_INCREMENT,
Location_name varchar(100) NOT NULL,
Location_level varchar(100) NOT NULL,
PRIMARY KEY (Location_id)
);

ALTER TABLE table_Location
ADD FOREIGN KEY (PC_id) REFERENCES table_PC(PC_id);

INSERT INTO table_Location
VALUES("5","Reigar Mountain", "Ten");

CREATE TABLE table_Quest(
Quest_id int NOT NULL AUTO_INCREMENT,
Quest_name varchar(100) NOT NULL,
Quest_level varchar(100) NOT NULL,
Location_id int,
PRIMARY KEY (Quest_id),
FOREIGN KEY (Location_id) REFERENCES table_Location(Location_id)
);
INSERT INTO table_Quest
VALUES("5","Save the world!", "Fifteen", "5");


SELECT * FROM table_Enemy;

CREATE TABLE table_Rule(
Rule_id int NOT NULL AUTO_INCREMENT,
Ruler_name varchar(100) NOT NULL,
Rule_description varchar(100) NOT NULL,
PRIMARY KEY (Rule_id)
);
INSERT INTO table_Rule
VALUES("5","Have Fun!", "This is the most important rule! If you aren't having a good time and begin to bother people you will leave for the session.");

CREATE TABLE table_Item(
Item_id int NOT NULL AUTO_INCREMENT,
Item_name varchar(100) NOT NULL,
Item_description varchar(100) NOT NULL,
PRIMARY KEY (Item_id)
);
INSERT INTO table_Item
VALUES("5","Black Iron Boots", "Increases Armor Class by 1.");

CREATE TABLE table_Encounter(
Encounter_id int NOT NULL AUTO_INCREMENT,
Encounter_name varchar(100) NOT NULL,
Encounter_level varchar(100) NOT NULL,
Encounter_monsters varchar(100) NOT NULL,
PRIMARY KEY (Encounter_id)
);
INSERT INTO table_Encounter
VALUES("5","Stop the thief!", "Six","Cultist Servants");

UPDATE table_Encounter SET Encounter_level = "Seven" WHERE Encounter_id = 5;
SELECT * FROM table_Encounter;

DELETE FROM table_Rule WHERE Rule_id = 5;
SELECT * FROM table_Rule;