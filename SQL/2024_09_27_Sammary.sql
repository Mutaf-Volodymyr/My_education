use airport;
# Найдите всех клиентов, которые приобрели более одного билета.

select c.name, count(ti.client_id) as count_ticket
from tickets ti
inner join clients c
on ti.client_id = c.id
group by client_id
having count_ticket > 1;

select cl.name
from clients cl
where exists(
    select 1
    from tickets ti
    where ti.client_id = cl.id and exists(
        select 1
        from tickets ti2
        where ti2.client_id = cl.id and ti.id != ti2.id));

# Найдите всех клиентов, купивших билеты на рейсы, которые были отменены.
select cl.name
from clients cl
inner join tickets ti
on cl.id = ti.client_id
inner join trips tr
    on ti.trip_id = tr.id
    and  tr.status = 'Cancelled';

select cl.name
from clients cl
where exists(
    select 1
    from tickets ti
    where ti.client_id = cl.id and exists(
        select 1
        from trips tr
        where ti.trip_id = tr.id and tr.status = 'Cancelled'));

select cl.name
from clients cl
where exists(
    select 1
    from tickets ti
    inner join trips tr
        on ti.trip_id = tr.id
        and  tr.status = 'Cancelled'
    where ti.client_id = cl.id);


# Для каждого пользователя укажите его полное имя и общее количество написанных
# им статей и комментариев.Упорядочьте результаты по общей активности (сумма
# статей и комментариев) в порядке убывания.

use social_media;



select
    concat(u.first_name, ' ', u.last_name) AS UserName,
    ifnull(n_stat.news_count, 0) AS news_activ,
    ifnull(c_stat.comment_count, 0) AS comments_activ,
    (ifnull(n_stat.news_count, 0) + ifnull(c_stat.comment_count, 0)) AS total_activ
from user as u
left join (
    select
        n.author_id,
        count(n.id) as news_count
    from news as n
    group by n.author_id
) as n_stat
    on u.id = n_stat.author_id
left join (
    select
        c.author_id,
        count(c.id) as comment_count
    from comment as c
    group by
        c.author_id
) as c_stat on u.id = c_stat.author_id
order by total_activ desc;


