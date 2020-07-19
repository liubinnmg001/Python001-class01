import pymysql
import pandas as pd
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')

1. SELECT * FROM data;
sql  =  'SELECT * FROM data'
df = pd.read_sql(sql,conn)
print(df)
 
2. SELECT * FROM data LIMIT 10;
df[0:10]

3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']

4. SELECT COUNT(id) FROM data;
df['id'].count()

5. SELECT * FROM data WHERE id<1000 AND age>30;
df[ ( df['id']<1000 ) & ( df['age']>30 ) ]

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
sql2  =  'SELECT * FROM table1'
df2 = pd.read_sql(sql2,conn)
df2.drop_duplicates(['id','order_id'],keep='last',inplace=False).groupby('id').aggregate( {'order_id':'count'})

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1, table2, on='id')

8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2]).drop_duplicates()

9. DELETE FROM table1 WHERE id=10;
df2.drop(df[ df['id'] == 10 ].index)

10. ALTER TABLE table1 DROP COLUMN column_name;
df2.drop( 'column_name' ,axis = 1)