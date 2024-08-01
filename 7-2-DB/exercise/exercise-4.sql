CREATE TABLE lecture (title VARCHAR(50) PRIMARY KEY);
-- many-to-many relationship table
CREATE TABLE student_lecture (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_sid VARCHAR(10) NOT NULL,
    lecture_title VARCHAR(50) NOT NULL,
    FOREIGN KEY (student_sid) REFERENCES student(sid),
    FOREIGN KEY (lecture_title) REFERENCES lecture(title)
);
INSERT INTO lecture (title)
VALUES ('coding'),
    ('math'),
    ('english'),
    ('database');
INSERT INTO student_lecture (student_sid, lecture_title)
VALUES ('2019147500', 'coding'),
    ('2019147500', 'english'),
    ('2019147500', 'database');