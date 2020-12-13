# step 1
    # 创建一个week03的数据库(默认方式)
        week03>create database week03;
        Query OK, 1 row affected (0.00 sec)

        week03>show databases;
        +---------------------+
        | Database            |
        +---------------------+
        | information_schema  |
        | mysql               |
        | performance_schema  |
        | sys                 |
        | week03              |
        +---------------------+
        5 rows in set (0.00 sec)

        week03>


# step 2
    # 修改字符集
        week03>alter database week03 character set utf8mb4;
        Query OK, 1 row affected (0.00 sec)

# step 3
    #查看字符集
        week03>alter database week03 character set utf8mb4;
        Query OK, 1 row affected (0.00 sec)


# step 4
    # 添加用户
        week03>grant all privileges on *.* to 'xiong'@'%' identified by 'xiong';
        Query OK, 0 rows affected, 1 warning (0.01 sec)
