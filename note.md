# 数据库更改语句

```mysql
INSERT INTO `tb_thread_num` (`thread_num_now`, `thread_max`) VALUES ('0', '3');
UPDATE `tb_thread_num` SET `thread_num_now` = '0' WHERE `tb_thread_num`.`thread_max` = 2;
UPDATE `tb_thread_num` SET `thread_max` = '3' WHERE `tb_thread_num`.`thread_max` = 2;
```