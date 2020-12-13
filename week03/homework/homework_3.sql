SELECT DISTINCT player_id, player_name, count(*) as num
FROM player JOIN team ON player.team_id = team.team_id
WHERE height > 1.80
GROUP BY player.team_id
HAVING num > 2
ORDER BY num DESC
LIMIT 2


-- 执行顺序为：
-- 1. from  (从player和team联表中查询)
-- 2. where  (查询条件)
-- 3. group by  (根据查询条件查询出结果后再进行分组)
-- 4. having  (分完组后根据having条件再次过滤)
-- 5. order by  (根据having过滤后进行排序)
-- 6. limit  (选择多少条记录)
-- 7. select  (根据select后面的字段返回最终的查询结果)