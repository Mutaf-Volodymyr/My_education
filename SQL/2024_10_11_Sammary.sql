use medical_healthcare;

# Получить список докторов, назначивших медикаменты стоимостью более 500.
# Необходимы email доктора, количество медикаментов,
# назначенных им, общая стоимость этих медикаментов

select d.first_name, d.last_name, sum(m.cost) as all_cost, count(m.medication_id) as count_medicam
from Doctors d
left join Prescriptions as p
on d.doctor_id = p.doctor_id
inner join Medications as m
on p.medication_id = m.medication_id
    and m.cost > 500
group by d.doctor_id
order by all_cost;

# Получить список пациентов с использованием метода оплаты 'Credit Card'
# и общей суммой оплат по страховке более 1000
# Получить список пациентов с использованием метода оплаты 'Credit Card'
# и общей суммой оплат по страховке более 1000
select pat.first_name,
       pm.method,
       sum(ip.amount_paid) as total_paid
from medical_healthcare.Patients pat
inner join medical_healthcare.Payment_Methods pm
    on pm.patient_id = pat.patient_id
    and pm.method = 'Credit Card'
inner join medical_healthcare.Insurance_Bills  ib
    on ib.patient_id = pat.patient_id
inner join medical_healthcare.Insurance_Payments ip
    on ip.bill_id = ib.bill_id
group by pat.first_name
having total_paid >= 5000
order by total_paid;



# Найти всех пациентов, у которых дата последнего теста превышает дату
# последнего назначения более чем на 30 дней.
# Вывести полное имя пациента, дату последнего теста и дату последнего назначения

select * from Test_Results;
select * from Prescriptions;


# Получить информацию о пациентах с диагнозом "рак", или "Глоукома", у которых
# заболевание рецидивировало, и страховка не покрывает лечение

###########################
# Найти всех пациентов, у которых дата последнего теста превышает дату
# последнего назначения более чем на 30 дней.
# Вывести полное имя пациента, дату последнего теста и дату последнего назначения

select * from Test_Results;
select * from Prescriptions;


# Получить информацию о пациентах с диагнозом "рак", или "Глоукома", у которых
# заболевание рецидивировало, и страховка не покрывает лечение


