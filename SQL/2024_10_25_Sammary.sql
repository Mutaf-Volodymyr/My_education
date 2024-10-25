# Найти пациентов, которым были назначены тесты, и вычислить общую стоимость
# назначенных тестов для каждого пациента. Вывести только тех пациентов,
# у которых сумма тестов превышает 2000.
use medical_healthcare;


select p.patient_id, sum(cost) as total_cost
from Patients p
inner join Test_Results as tr
on p.patient_id = tr.patient_id
inner join Tests as t
on tr.test_id = t.test_id
group by p.patient_id
having  total_cost > 2000;


# Найти количество назначений на визиты у каждого врача за последний
# год, а также вывести общее количество назначений для всех врачей
# за этот период с использованием оконных функций.

select distinct first_name, last_name,
       count(appointment_id) over (partition by a.doctor_id) as count_appointment,
       count(*) over() as all_appountment
from Doctors as d
inner join Appointments as a
on d.doctor_id = a.doctor_id
    and appointment_date > now() - interval 1 year;



# Найти пациентов, которые заплатили больше $15000 за
# последний год по страховке, ранжируя их по сумме уплаченных денег.
# Вывести ID пациента, его email для связи, общую уплаченную сумму, ранг

select p.patient_id, email,
       sum(amount_paid) as total_paid,
       dense_rank() over (order by sum(amount_paid) desc) as besser_client
from Patients as p
inner join Insurance_Bills as ib
on p.patient_id = ib.patient_id
inner join Insurance_Payments as ip
on ib.bill_id = ip.bill_id
    and ip.payment_date > now() - interval 1 year
group by p.patient_id
having total_paid > 15000;


# Разделить болезни на 4 группы на основе частоты их диагностики
# и вывести номер группы для каждой болезни.
with tab as (
    select s.name,
           count(s.disease_id) as count_disease
    from Diseases as s
    inner join Diagnoses as d
    on s.disease_id = d.disease_id
    group by s.disease_id)
select *,
       ntile(4) over (order by count_disease) grouper
from tab;


# Найти пациентов из штатов Юты, или Техаса у которых общая
# стоимость процедур больше $50000.

select p.patient_id, first_name, last_name, state,
       sum(cost) as total_cost
from Patients as p
inner join Addresses as a
    on p.address_id = a.address_id
    and a.state in ('Utah', 'Texas')
inner join Treatments as t
on p.patient_id = t.patient_id
group by p.patient_id
having total_cost > 50000;

# Найти пациентов, живущих в городах, где почтовый индекс заканчивается на 08
# и подсчитать количество тестов, назначенных за последний год.
select first_name, last_name,
       count(p.patient_id) as count_test
from Patients as p
inner join Addresses as a
on p.address_id = a.address_id
    and a.zip_code like '%08'
inner join (
    select test_id, patient_id
    from  Appointment_Tests as at
    inner join Appointments as ap
    on ap.appointment_id = at.appointment_id
    and ap.appointment_date > now() - interval  1 year)
    as tab
on p.patient_id = tab.patient_id
group by p.patient_id;


















