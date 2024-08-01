CREATE TABLE assignment (
    -- auto-created primary key
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    -- foreign key
    -- many-to-one relationship
    student_sid VARCHAR(10) NOT NULL REFERENCES student(sid)
);
-- 주의: auto_increment primary key이므로 여러번 실행하면 중복되는 데이터가 들어갈 수 있음
INSERT INTO assignment (title, student_sid)
VALUES ('hello, world', '2019147500'),
    ('help me, world', '2019147500');
SELECT *
FROM assignment;