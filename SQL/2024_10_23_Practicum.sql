use world;
# Напишите запрос для определения доли населения города от общей
# численности населения страны и проведите ранжирование городов
# в пределах каждой страны:

select ci.Name, ci.Population, c.Population, c.Name,
    ci.Population / c.Population * 100 as res,
    dense_rank() over (partition by c.Name order by ci.Population / c.Population * 100 desc ) as r
from city as ci
left join world.country c
    on c.Code = ci.CountryCode;


# Написать SQL-запрос для выбора городов, занимающих первое
# место по населению в своих странах и превышающих среднее
# население по всем городам.

select city_name, city_population
    from
        (select ci.Name as city_name,
               ci.Population as city_population,
               avg(ci.Population) over () as avg_all_city,
               rank() over (partition by c.Name order by ci.Population desc) as rang
        from city as ci
        left join world.country c
            on c.Code = ci.CountryCode) as t
where rang = 1 and city_population > avg_all_city;


use medical_healthcare;

# Найти количество назначенных тестов для каждого пациента,
# вывести только тех пациентов, у которых количество тестов больше 3.

select distinct tab.last_name, tab.first_name, count_test
from (

    select t.test_id, p.last_name, p.first_name, p.patient_id,
           count(*) over (partition by p.patient_id) as count_test
    from Tests as t
    inner join Appointment_Tests as at
    on t.test_id = at.test_id
    inner join Appointments as a
    on at.appointment_id = a.appointment_id
    inner join Patients as p
    on a.patient_id = p.patient_id) as tab
where count_test > 3
order by count_test desc;


# Найти общие затраты по каждому пациенту на основании назначенных
# им медикаментов и вычислить сумму этих затрат по каждому пациенту

select distinct p.patient_id,
       sum(m.cost) over(partition by p.patient_id) as sum_cost
from Prescriptions as pr
left join Patients as p
on pr.patient_id = p.patient_id
inner join Medications as m
on pr.medication_id = m.medication_id;



select distinct p.patient_id,
       sum(m.cost) as sum_cost
from Prescriptions as pr
left join Patients as p
on pr.patient_id = p.patient_id
inner join Medications as m
on pr.medication_id = m.medication_id
group by p.patient_id
order by sum_cost desc;


# Для каждого пациента вывести список их диагнозов,
# отсортированных по дате, и присвоить каждой
# записи порядковый номер.

select a.patient_id, diagnosis_date, notes,
       dense_rank() over (partition by a.patient_id order by diagnosis_date) as res
from Diagnoses as d
inner join Appointments as a
on d.appointment_id = a.appointment_id
inner join Patients as p
on a.patient_id = p.patient_id;



# Найти пациентов, которые проходят наибольшее количество
# процедур (treatments), и ранжировать их.
# Выводить только тех, кто прошел больше трех процедур.

select tab.patient_id,
       tab.count_Treatments,
       dense_rank() over (order by count_Treatments) as rang
from (
    select p.patient_id,
           count(p.patient_id) as count_Treatments
    from Treatments as t
    inner join Patients as p
    on t.patient_id = p.patient_id
    group by p.patient_id
    having count_Treatments > 3) as tab;


# Разделить пациентов на четыре равные группы по
# возрасту и вывести возраст пациентов в каждой группе.

with tab as
    (select patient_id, last_name, first_name,
           TIMESTAMPDIFF(YEAR, date_of_birth, now()) as year
    from Patients)
select *,
       ntile(4) over (order by year desc ) as `group`
from tab;


# Разделить пациентов на 4 равные группы по общей сумме их страховых
# счетов и вычислить количество пациентов в каждой группе.
with tab as
    (select *,
            ntile(4) over (order by all_amount) as grouper
    from (
            select
            p.patient_id,
            sum(ib.total_amount) as all_amount
            from Patients as p
            inner join Insurance_Bills as ib
            on p.patient_id = ib.patient_id
            group by p.patient_id
         ) as iner_tab
    )
select *,
       count(*) over (partition by grouper) as counter
from tab;


# Для каждого пациента вычислите среднее количество дней между датой
# начала назначения (Prescriptions.start_date) и датой оплаты страхового
# счета (Insurance_Payments.payment_date). Отобразите patient_id, полное
# имя пациента, и среднее количество дней.


with iner_tab as
    (select pat.patient_id, concat(pat.first_name, ' ', last_name) as full_name,
           TIMESTAMPDIFF(DAY, ip.payment_date, pres.start_date) as dif_date
    from Patients as pat
    inner join Prescriptions as pres
    on pat.patient_id = pres.patient_id
    inner join Insurance_Bills as ib
    on pat.patient_id = ib.patient_id
    inner join Insurance_Payments as ip
    on ib.bill_id = ip.bill_id)
select full_name,
       avg(dif_date) as averig
from iner_tab
group by patient_id;


# Найти все болезни, у которых существует более одной стадии,
# и вывести их имена и количество стадий

select d.name, iner_tab.count_stage
from medical_healthcare.Diseases as d
inner join
    (select disease_id, count(stage_name) as count_stage
    from Disease_Stages as ds
    group by disease_id
    having count_stage > 1) as iner_tab
on d.disease_id=iner_tab.disease_id;


# Разделить пациентов на 5 возрастных групп и внутри каждой
# группы ранжировать их по доступным средствам (funds_available)

with tab as
    (select patient_id, concat(first_name, ' ', last_name) as full_name,
        TIMESTAMPDIFF(YEAR, date_of_birth, now()) as `year`,
        ntile(5) over (order by TIMESTAMPDIFF(YEAR, date_of_birth, now())) as `year_group`,
        funds_available
    from Patients as p)
select *,
       dense_rank() over (partition by year_group order by funds_available desc) as rang
from tab












