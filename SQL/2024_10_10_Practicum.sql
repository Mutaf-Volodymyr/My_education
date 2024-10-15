use medical_healthcare;


# Найдите все рецепты, которые были выписаны за последние 30 дней.
# Вывести patient_id, doctor_id, medication_id, и дату назначения рецепта. Результаты отсортировать по дате
select patient_id, doctor_id, medication_id, start_date
from Prescriptions
where start_date > now() - interval 30 day;

# Определите, какие врачи выписали более 5 рецептов.
# Вывести полное имя врача, его email и количество рецептов. Показывать только тех, у кого больше 5 назначений.
# Отсортировать по количеству назначений.
select concat(d.last_name,' ', d.first_name) as full_name,
       d.email,
       count(d.doctor_id) as count_Prescriptions
from Prescriptions p
inner join medical_healthcare.Doctors d
on p.doctor_id = d.doctor_id
group by d.doctor_id
having count_Prescriptions > 5;


# Найдите пациентов, у которых нет назначенных рецептов.
# Выведите дополнительно Его данные из медицинской истории.
select p.first_name, p.last_name,  mh.*
from Patients as p
left join Prescriptions as r
on p.patient_id = r.patient_id
inner join Medical_History as mh
on p.patient_id = mh.patient_id
where r.prescription_id is null;



# Найдите пациентов, которые за последние 12 месяцев получили рецепты
# как минимум от трёх разных врачей.
select p.patient_id, first_name, last_name,
       r.prescription_id, doctor_id,
       count(distinct doctor_id) as recepts
from Patients as p
inner join Prescriptions as r
on p.patient_id = r.patient_id
    and start_date >= now() - interval 12 month
group by p.patient_id
having recepts > 2;

# Найдите пациента с максимальной разницей между количеством
# выписанных рецептов в 2022 и 2023 годах.
select p.patient_id,
       p.last_name,
       p.first_name,
       max(sub.diff) as max_diff

from Patients as p
inner join (
    select patient_id,
       abs(count(if(year(start_date) = 2022, 1, null))
               - count(if(year(start_date) = 2023, 1, null))
       ) as diff

    from Prescriptions
    group by patient_id) as sub
on p.patient_id = sub.patient_id;





















