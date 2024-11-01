create schema taxi_fatum;
use taxi_fatum;

create table orders (
    orders_id int primary key auto_increment,
    travel_id int not null,
    review_id int not null,
    clients_id int not null,
    drivers_id int not null,
    auto_id int not null,
    cost float not null,
    created_ad datetime not null,
    start datetime,
    finish datetime,
    sex set('male', 'female', 'not'),
    foreign key (travel_id) references travel (travel_id),
    foreign key (clients_id) references clients (clients_id),
    foreign key (drivers_id) references drivers (drivers_id),
    foreign key (auto_id) references auto (auto_id),
    foreign key (review_id) references review (review_id)
);

create table review (
    review_id int primary key auto_increment,
    rating set('1', '2', '3', '4', '5') not null,
    comment text
);

create table clients (
    clients_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50),
    sex set('male', 'female'),
    phone_number char(10) not null
);

create table travel (
    travel_id int primary key auto_increment,
    addresses_start int not null,
    addresses_finish int not null,
    foreign key (addresses_start) references addresses (addresses_id),
    foreign key (addresses_finish) references addresses (addresses_id)
);

create table addresses (
    addresses_id int primary key auto_increment,
    street varchar(250) not null unique
);

create table drivers (
    drivers_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    sex set('male', 'female'),
    phone_number char(10) not null,
    auto_id int unique not null,
    foreign key (auto_id) references auto (auto_id)
);

create table auto (
    auto_id int primary key auto_increment,
    mark varchar(200) not null,
    model varchar(200) not null,
    nummer varchar(10) not null,
    color varchar(10) not null,
    class set('Comfort', 'Business', 'Lux') not null,
--  если авто не в auto_park_id (Null), то оно не в собственности фирмы
    auto_park_id int,
    type set('Sedan', 'hatchback', 'station wagon', 'coupe', 'convertible', 'roadster', 'crossover', 'SUV', 'pickup', 'minivan', 'liftback'),
    foreign key (auto_park_id) references auto_park (auto_park_id)
);


create table auto_park (
    auto_park_id int primary key auto_increment,
    addresses_id int not null unique
);

create table sto (
    sto_id int primary key auto_increment,
    auto_id int not null,
    auto_park_id int not null,
    procedures_id int not null,
    date_start date not null,
    date_finish date,
    foreign key (procedures_id) references procedures (procedures_id),
    foreign key (auto_id) references auto (auto_id),
    foreign key (auto_park_id) references auto_park (auto_park_id)
);


create table procedures(
    procedures_id int primary key auto_increment,
    procedure_name varchar(250) not null unique
);


create table procedures2masters(
    procedures_id int,
    masters_id int,
    primary key (procedures_id, masters_id),
    foreign key (masters_id) references masters(masters_id),
    foreign key (procedures_id) references procedures(procedures_id)
);


create table masters(
    masters_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    sex set('male', 'female'),
    phone_number char(10) not null
);


alter table auto_park
add foreign key (addresses_id) references addresses (addresses_id);