MySQL8.0 迁移数据存储位置到指定位置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

一：具体步骤
---------------------------------------------------------
**停止mysql服务**
	(1) sudo service mysql stop
**拷贝数据存储到你的新位置**
    (1) 例如: /home/database/
    (#) sudo cp -R /var/lib/mysql /home/database/
**打开/etc/mysql/mysql.conf.d/mysqld.cnf**
    (1) 将以下两行注释掉并加入新的两行(按自己的位置修改)
    (#) #socket	= /var/run/mysqld/mysqld.sock
    (#) #datadir= /var/lib/mysql
    (#) socket	= /home/database/mysql/mysql.sock
    (#) datadir	= /home/database/mysql
    (#) 再接着添加以下内容
    (#) [client]
    (#) socket	= /home/database/mysql/mysql.sock
    (#) [mysql]
    (#) socket	= /home/database/mysql/mysql.sock
**打开/etc/apparmor.d/usr.sbin.mysqld**
    (1) 注释以下两行并加入新的两行(网上很多教程没讲这个，用gedit修改该文件要记得删除可能存在的usr.sbin.mysqld~ 文件，不然启动会失败)
    (#) #/var/lib/mysql/ r,
    (#) #/var/lib/mysql/** rwk,
    (#) /home/database/mysql/ r,
    (#) /home/database/mysql/** rwk,
**打开/etc/apparmor.d/abstractions/mysql**
   (1) 注释下面一行并加入第三行(这是个大坑)
   (#) #/var/lib/mysql{,d}/mysql{,d}.sock rw,
   (#) /home/database/mysql/mysql.sock rw,
**重新加载apparmor**
	(1) sudo /etc/init.d/apparmor reload
**重新加载mysql**
	(1) sudo service mysql start

二：其他几个大坑可能导致启动失败
---------------------------------------------------------
**mysql/的权限属性**
    (1) 注意查看/home/database/mysql是否属于mysql组和mysql用户，及权限，若不是则
    (#) sudo chown -R mysql:mysql /home/database/mysql 
    (#) sudo chmod 755 /home/database/mysql/
    (#) 没有mysql组的通过以下命令创建mysql组和用户
    (#) sudo groupadd mysql
    (#) sudo useradd -r -g mysql mysql
**database/的权限属性**
    (#) database/的权限，建议是755,属于root,root
    (#) sudo chgrp root database/
    (#) sudo chown root database/
    (#) sudo chmod 755 database/
**Linux selinux安全机制**
    (1) 在/etc/selinux/config 或类似的文件里，如有SELINUX，修改为
 	(#) SELINUX=disabled

三：结语
---------------------------------------------------------
**感想**
    (1) 网上的很多教程都过时了且不详细，提到这个又漏掉那个。
    (#) MySQL 8.0的配置文件太多了，my.cnf conf.d mysql.cnf mysql.conf.d 等等交叉引用。
    (#) `官方文档 <https://downloads.mysql.com/docs/refman-8.0-en.a4.pdf>`_ 有六千多页，够玩儿一年。



