-- DDL
CREATE TABLE student (
    -- primary-key
    sid VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    phone_number VARCHAR(30)
);
-- DML
-- 주의: 같은 PK를 갖는 데이터를 둘 이상 넣을 수 없음
INSERT INTO student (sid, name, age, phone_number)
VALUES ('2019147500', 'Alice', 20, '123-456-7890');
-- DQL
SELECT *
FROM student;