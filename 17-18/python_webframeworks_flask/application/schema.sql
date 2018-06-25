drop table if exists todolist;
create table todolist (
  id integer primary key autoincrement,
  title text not null
);