drop table if exists person;

create table person (
    id int primary_key not null,
    name text not null,
    age  int 
);

insert into person values 
    (1, 'Bob', 22);
insert into person values
    (2, 'Sue', 34);
insert into person values
    (3, 'Timmy', 19);
insert into person values
    (4, 'Ellen', 24);
