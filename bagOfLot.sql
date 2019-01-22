
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS Child;
DROP TABLE IF EXISTS Presents;

CREATE TABLE `Child` (
    `child_Id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name`    TEXT NOT NULL,
    'delivered' BIT NOT NULL
);

INSERT INTO Child VALUES (null, 'Sussy', 1);
INSERT INTO Child VALUES (null, 'Billy', 1);
INSERT INTO Child VALUES (null, 'Maddie', 1);

CREATE TABLE `Presents`(
    `present_Id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `present_name`    TEXT NOT NULL,
    'child_id'  INTEGER NOT NULL,
    FOREIGN KEY(`child_Id`)
 REFERENCES `Child`(`child_Id`)
 ON DELETE cascade
);

INSERT INTO Presents
SELECT NULL, 'LightSaber' ,child_id
FROM Child c
Where  c.Name = 'Billy';

INSERT INTO Presents
SELECT NULL, 'Doll', child_id
FROM Child c
WHERE  c.Name = 'Sussy';

INSERT INTO Presents
Select null, 'Bike' , child_id
FROM Child c
WHERE  c.Name = 'Maddie';
