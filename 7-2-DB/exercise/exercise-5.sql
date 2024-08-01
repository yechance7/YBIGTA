INSERT INTO student (sid, name, age, phone_number)
VALUES ('2019147501', 'Bob', 21, '123-456-7891'),
    ('2019147502', 'Charlie', 22, '123-456-7892'),
    ('2019147503', 'David', 23, '123-456-7893');
INSERT INTO student_lecture (student_sid, lecture_title)
VALUES ('2019147501', 'coding'),
    ('2019147501', 'math'),
    ('2019147502', 'english');
-- join
SELECT *
FROM student_lecture;
SELECT l.title
FROM lecture l
    JOIN student_lecture sl ON l.title = sl.lecture_title
WHERE sl.student_sid = '2019147500';