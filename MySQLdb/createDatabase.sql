
create database python_test character set gbk;
use python_test;
drop table if exists tb_test;
create table tb_test(
	id int not null auto_increment primary key,
	name varchar(30) not null
);
insert into tb_test(id,name) values(1,'liang');
