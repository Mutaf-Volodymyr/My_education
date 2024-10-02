# Подключитесь к базе данных Students (которая находится на удаленном сервере).
use Students;

# Найдите самого старшего студента
select *
from Students
order by age desc
limit 1;

# Найдите самого старшего преподавателя
select *
from Teachers
order by age desc
limit 1;

# Выведите список преподавателей с количеством компетенций у каждого
select T.name, count(competencies_id) as count_comp
from Teachers as T
left join Students.Teachers2Competencies T2C
    on T.id = T2C.teacher_id
group by T.id;


# Выведите список курсов с количеством студентов в каждом
select C.title, count(S2C.student_id) as count_student
from Courses as C
left join Students2Courses as S2C
on C.id = S2C.course_id
group by S2C.course_id;

# Выведите список студентов, с количеством курсов, посещаемых каждым студентом.
select S.first_name, S.last_name, count(S2C.course_id) as count_cours
from Students as S
left join Students2Courses as S2C
on S2C.student_id = S.id
group by S.id
