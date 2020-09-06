学习笔记
运行方式：

1、启动爬虫：

项目名：smzdm

cd Python001-class01\week10\graduation_design\smzdm\smzdm

scrapy crawl mobile

2、数据库信息(数据库密码是我个人的虚机，可以暴露，专门用于做作业)

数据库：mobile

表：mobile

字段信息：

+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| name       | varchar(100) | NO   |     | NULL    |                |
| input_time | datetime     | NO   |     | NULL    |                |
| comment    | varchar(500) | NO   |     | NULL    |                |
| sentiments | float        | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+

3、Django展示

项目名：djangosmzdm

应用程序：mobile

启动Django：

cd Python001-class01\week10\graduation_design\djangosmzdm

python manage.py runserver

访问地址：http://127.0.0.1:8000/mobile/index
