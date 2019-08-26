#!/bin/bash
tar xf /lnmp_soft.tar.gz &/dev/null
cd
cd lnmp_soft/	
tar xf nginx-1.12.2.tar.gz &>/dev/null
cd nginx-1.12.2/
echo '安装依赖软件'
yum -y install gcc pcre-devel openssl-devel &> /dev/null
echo '检查软件并指定需要的参数'
./configure  --user=nginx  --with-http_ssl_module --with-stream  --with-http_stub_status_module &> /dev/null
echo '正在制作程序' &> /dev/null
make ; make install &> /dev/null
useradd nginx	&>/dev/null
/usr/local/nginx/sbin/nginx &> /dev/null
echo '正在安装mariadb及其依赖包(及启动服务)' 
yum -y install mariadb mariadb-server mariadb-devel &> /dev/null
systemctl restart mariadb &> /dev/null
systemctl enable mariadb &> /dev/null
echo '正在安装php及其依赖包(及启动服务)'
yum -y install php-fpm php-mysql php &> /dev/null
systemctl restart php-fpm &> /dev/null
systemctl enable php-fpm &> /dev/null
echo '正在写入配置文件'
sed -i '65,71s/#//' /usr/local/nginx/conf/nginx.conf
sed -i '/SCRIPT_FILENAME/d' /usr/local/nginx/conf/nginx.conf
sed -i 's/fastcgi_params/fastcgi.conf/'  /usr/local/nginx/conf/nginx.conf
sed -i 's/index.html/index.php index.html/' /usr/local/nginx/conf/nginx.conf
echo '重新读取'
/usr/local/nginx/sbin/nginx -s reload
echo '拷贝php文件'
cd ~/lnmp_soft/php_scripts/
\cp test.php mysql.php /usr/local/nginx/html/
echo '完成'
