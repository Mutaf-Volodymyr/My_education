# Data Types for Date

Date - '%YYYY-%mm-%dd' -> 3 bytes
Datetime - '%YYYY-%mm-%ddT%H:%i:%s%.%f' -> 8 bytes
Timestamp - '12345678954125' -> 4 bytes;


select STR_TO_DATE('21, 5, 2018', '%d, %m, %Y');
select STR_TO_DATE('21, 5, 2018T14:45:13.444', '%d, %m, %YT%H:%i:%s');


# от чего отнять, что отнять
select DATEDIFF('2023-05-21', '2023-01-30'); # разница первого от второго - строго в днях
select DATEDIFF('2023-01-30', '2023-05-21'); # если поменять местами - будет отрицательное число, не ошибка


# от чего отнять, что отнять
select DATEDIFF('2023-05-21', '2023-01-30'); # разница первого от второго - строго в днях
select DATEDIFF('2023-01-30', '2023-05-21'); # если поменять местами - будет отрицательное число, не ошибка


select TIMESTAMPDIFF(MONTH, '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ МЕСЯЦЕВ
select TIMESTAMPDIFF(MINUTE, '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ МИНУТ
select TIMESTAMPDIFF(DAY, '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ ДНЕЙ
select TIMESTAMPDIFF(WEEK, '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ НЕДЕЛЬ
select TIMESTAMPDIFF(YEAR, '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ ЛЕТ
select TIMESTAMPDIFF(QUARTER , '2023-01-30', '2023-05-21'); # кол-во только ПОЛНЫХ КВАРТАЛОВ
select TIMESTAMPDIFF(month , '2016-03-03', '2019-01-04'); # кол-во только ПОЛНЫХ КВАРТАЛОВ



select TIMESTAMPDIFF(MONTH, '2023-01-30', '2023-02-01'); # кол-во только ПОЛНЫХ МЕСЯЦЕВ
select TIMESTAMPDIFF(QUARTER , '2023-03-01', '2023-07-01'); # кол-во только ПОЛНЫХ КВАРТАЛОВ


select DATE_ADD(now(), INTERVAL 1 YEAR); # добавить дату
select now() + INTERVAL 1 YEAR;

SELECT SUBDATE(now(), INTERVAL 6 MONTH); # отнять дату
select now() - INTERVAL 6 MONTH;

select DATE_ADD(now(), INTERVAL -1 YEAR); # отнимает (не совсем очевидно)

select employees.employee_id, employees.email
from employees
where WEEKDAY(hire_date) = 5;
select WEEKDAY(now());


select LAST_DAY(now());
select DAYOFYEAR(now());
select DAYOFMONTH(now());
select DAYOFWEEK(now());

select DAYOFWEEK(now()), WEEKDAY(now());

select DAYNAME(now());


select DATE_FORMAT(now(), '%Y');
select YEAR(now());
select DAY(now());
select MONTH(now());

SET lc_time_names = 'ru_RU';

# Используя базу данных hr, написать запрос, который отображает сотрудников, нанятых в 2005 году.
use hr;

select concat(last_name, ' ', first_name) as full_name, hire_date
from employees
where hire_date between '2005-01-01' and '2005-12-31'
order by hire_date;

select * from employees
where hire_date between
str_to_date("01, 2005, 01", "%m, %Y, %d")
and str_to_date("2005, 12, 31", "%Y, %m, %d");

SELECT *
FROM hr.employees e
WHERE DATE_FORMAT(hire_date, '%Y') = 2005;

select now() + interval 24 day;

select dayofyear(now());


# Определите месяц, в который чаще всего принимают на работу
select monthname(hire_date) as `month`, count(*) as `count`
from hr.employees emp
where hire_date is not null
group by `month`
order by `count` desc
limit 1;

# Напишите SQL-запрос для анализа средней стоимости покупок, совершенных в марте,
# и определите, какие продавцы имеют самую высокую и самую низкую среднюю стоимость
# покупок в этом месяце. Обязательно выведите имя продавца.

use shop;

SELECT AVG(O.AMT) AS AVERAGE_COST, S.SNAME
FROM ORDERS AS O
JOIN SELLERS AS S ON S.SELL_ID = O.SELL_ID
WHERE MONTH(O.ODATE) = 3
GROUP BY S.SNAME
ORDER BY AVERAGE_COST;


# Выведите все новости, которые были созданы в понедельник. Отобразите идентификатор
# статьи, заголовок и название дня недели создания.

use social_media;
select id, title, dayname(created_at) as day
from social_media.news
where weekday(created_at) = 0;

# Список имен и фамилий пользователей, которые зарегистрировались за последние 30 дней.
select first_name, last_name, created_at
from user
where created_at >= (now() - interval 365 day);

# Найдите количество комментариев, сделанных в каждом месяце текущего года.
# Отобразите название месяца и количество комментариев.

select monthname(created_at) as `month`, count(*) as `count`
from comment
where year(created_at) = year(now() - interval 1 year)
group by month(created_at)
order by `count` desc;


# Выведите новости, которые не обновлялись более года. Отобразите их идентификатор,
# заголовок и количество дней с момента последнего обновления.
select id, title, moderated, TIMESTAMPDIFF(day, ifnull(updated_at, created_at), now()) as upd_count
from news
where ifnull(updated_at, created_at) < now() - interval 1 year;


# Выведите небольшую статистику за последние 18 месяцев в формате: ID автора, кол-во
# новостей, опубликованных им

select u.id, concat(u.last_name,' ', u.first_name) as full_name, count(*) as count_craete_news
from user u
inner join news as n
on u.id = n.author_id
    and n.created_at > now() - interval 18 month
group by u.id;


# Выведите все комментарии, сделанные за последние 512 дней, вместе с
# идентификатором комментария, содержанием, именем и фамилией автора, а
# также количеством дней назад, когда был сделан комментарий.

select  concat(u.last_name,' ', u.first_name) as full_name, c.content, c.id, TIMESTAMPDIFF(day, c.created_at, now()) as dey_after
from user u
inner join comment as c
on u.id = c.author_id
    and c.created_at > now() - interval 512 day;

# Рассчитайте процент новостей, которые были отмодерированы (moderated = 1)
# за последние 18 месяцев. Отобразите общее количество статей,
# количество отмодерированных статей и процент модерации.

select count(id) as all_count, sum(moderated) as count_mod, concat(round((sum(moderated) / count(id)  * 100), 2), '%') as per
from news
where created_at > now() - interval 18 month;


# Найдите разницу в днях между датой создания аккаунта пользователя и датой его первого
# комментария. Отобразите имя, фамилию пользователя и количество дней до первого комментария.
select u.id,  u.first_name, u.last_name, ifnull(TIMESTAMPDIFF(day, new_tab.created_at, u.created_at), 'no comment') as dey_dif
from user as u
left join (
    select author_id, min(c.created_at) as created_at
    from social_media.comment c
    group by c.author_id) as new_tab
    on u.id = new_tab.author_id;


# Выведите новости, которые не получили ни одного комментария в течение 30 дней с момента
# их создания. Отобразите идентификатор статьи, заголовок и дату создания.

select us.first_name, us.last_name, timestampdiff(day, first_coment, us.created_at) as day_diff
FROM social_media.user as us
inner join (select author_id, min(created_at) as first_coment
from comment group by author_id) as com
on us.id = com.author_id;



# Выведите новости, которые не получили ни одного комментария в течение 30 дней с момента
# их создания. Отобразите идентификатор статьи, заголовок и дату создания.
SELECT n.created_at, cf.created_at
FROM social_media.news n
LEFT JOIN social_media.comment c ON c.news_id = n.id
AND TIMESTAMPDIFF(DAY, n.created_at, c.created_at) > 300
LEFT JOIN (
SELECT c2.news_id, c2.created_at
FROM social_media.comment c2
GROUP BY c2.news_id
ORDER BY c2.created_at
) as cf ON cf.news_id = n.id
WHERE c.id IS NULL
AND cf.created_at >= n.created_at;




