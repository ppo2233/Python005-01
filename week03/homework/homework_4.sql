# step 1
    # 数据准备(查看表)
        week03>show tables;
        Empty set (0.00 sec)

    # 数据准备(创建table1表)
        week03>create table `table1` (`id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(255), PRIMARY KEY (`id`)) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci;;
        Query OK, 0 rows affected (0.12 sec)

        ERROR:
        No query specified

        week03>show tables;

    # 数据准备(创建table2表)
        week03>create table `table2` (`id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(255), PRIMARY KEY (`id`)) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci;;
        Query OK, 0 rows affected (0.12 sec)

        ERROR:
        No query specified

        week03>show tables;

    # 查询表
        week03>show tables;
        +------------------+
        | Tables_in_week03 |
        +------------------+
        | table1           |
        | table2           |
        +------------------+
        2 rows in set (0.00 sec)

        week03>

    # 向table1表中插入两条数据
        week03>insert into table1 values('1', 'table1_table2');
        Query OK, 1 row affected (0.01 sec)

        week03>insert into table1 values('2', 'table2');
        Query OK, 1 row affected (0.01 sec)

        week03>select * from table1;
        +----+---------------+
        | id | name          |
        +----+---------------+
        |  1 | table1_table2 |
        |  2 | table1        |
        +----+---------------+
        2 rows in set (0.00 sec)

        week03>

    # 向table2表中插入两条数据
        week03>insert into table2 values('1', 'table1_table2');
        Query OK, 1 row affected (0.01 sec)

        week03>insert into table2 values('3', 'table2');
        Query OK, 1 row affected (0.01 sec)

        week03>select * from table2;
        +----+---------------+
        | id | name          |
        +----+---------------+
        |  1 | table1_table2 |
        |  3 | table2        |
        +----+---------------+
        2 rows in set (0.00 sec)

        week03>

# step 2
    # (inner)join
        week03>select t1.id, t1.name, t2.id, t2.name from table1 t1 join table2 t2 on t1.id = t2.id;
        +----+---------------+----+---------------+
        | id | name          | id | name          |
        +----+---------------+----+---------------+
        |  1 | table1_table2 |  1 | table1_table2 |
        +----+---------------+----+---------------+
        1 row in set (0.00 sec)

# step 3
    # left join
        week03>select t1.id, t1.name, t2.id, t2.name from table1 t1 left join table2 t2 on t1.id = t2.id;
        +----+---------------+------+---------------+
        | id | name          | id   | name          |
        +----+---------------+------+---------------+
        |  1 | table1_table2 |    1 | table1_table2 |
        |  2 | table1        | NULL | NULL          |
        +----+---------------+------+---------------+
        2 rows in set (0.00 sec)

# step 4
    # right join
    week03>select t1.id, t1.name, t2.id, t2.name from table1 t1 right join table2 t2 on t1.id = t2.id;
    +------+---------------+----+---------------+
    | id   | name          | id | name          |
    +------+---------------+----+---------------+
    |    1 | table1_table2 |  1 | table1_table2 |
    | NULL | NULL          |  3 | table2        |
    +------+---------------+----+---------------+
    2 rows in set (0.00 sec)

# step 5 总结
    # inner join 表示两个都是表一样没有主副表之分，因此，只会查询出满足条件的记录
    # left join 会以左边的表作为主表，主表有多少记录都会展示出来，而副表没有数据则给null
    # right join 会以右边的表作为主表，主表有多少记录都会展示出来，而副表没有数据则给null
