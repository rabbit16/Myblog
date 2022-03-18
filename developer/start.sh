conda activate myblog
cd /usr/jiang/blogProj/developer
uwsgi --ini uwsgi_conf.ini &
echo "需要再启动docker"
echo "项目初始化完成"