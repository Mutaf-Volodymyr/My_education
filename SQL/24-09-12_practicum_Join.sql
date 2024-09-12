use Students;
select * from Students;
select * from Students2Courses;
select * from Courses;


# Выведите список студентов с курсом, на который студент записан
# (результат содержит имя студента - name и course_id).
select
    s.first_name as student_name,
    c2.title as course_name
from Students as s
left join Students.Students2Courses as s2c
    on s.id = s2c.student_id
inner join Students.Courses as c2
    on s2c.course_id = c2.id


# Выведите список студентов, который не записаны на какой-либо курс.
select
    s.first_name
from Students as s
left join Students.Students2Courses S2C on s.id = S2C.student_id
where S2C.student_id is null;


# Выведите список стран со столицами.
use world;
select * from world.country;
select * from world.city;

select
    w.Name as Country,
    c.Name as Capital
from world.country as w
inner join world.city c
    on w.Capital = c.ID;


# Выведите список стран с языками, на которых в них говорят.
select
    c.Name,
    cl.Language
from world.countrylanguage as cl
inner join world.country as c
    on cl.CountryCode = c.Code;

# Выведите список стран с официальными языками.
select * from  countrylanguage;
select
    c.Name,
    cl.Language
from world.countrylanguage as cl
inner join world.country as c
    on cl.CountryCode = c.Code
where cl.IsOfficial = 'T';


# Вывести имя, фамилию и город сотрудников,
# которые работают в Seattle или Toronto
use hr;
select * from employees;
select * from locations;
select * from departments;

select
    emp.first_name,
    emp.last_name,
    loc.city
from employees as emp
inner join departments as dep
on emp.department_id = dep.department_id
inner join locations as loc
on dep.location_id = loc.location_id
    and loc.city in ('Seattle', 'Toronto');

