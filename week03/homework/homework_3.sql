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
-- 5. select  (根据select指定字段得到检索到的记录信息)
-- 6. order by  (进行排序)
-- 7. limit  (限制最终返回记录条数)
