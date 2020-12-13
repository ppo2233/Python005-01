-- name 添加索引
week03>create index `name_index` on table1 (`name`);
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

week03>

-- id 为主键

-- 添加索引会加快，尤其是在大量数据且基本无变动的情况下