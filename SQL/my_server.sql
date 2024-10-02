use library;

create table test_dade(
    falsh_date varchar(15),
    true_date datetime
);
select * from test_dade;

insert into test_dade
(falsh_date, true_date)
values
('2023-05-06', '2022-05-06');

select DATEDIFF(falsh_date, '2023-05-04')
from test_dade;

select DATEDIFF(true_date, '2022-05-04')
from test_dade;