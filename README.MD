
1. Create the MYSQL Container:
docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_USER=appuser -e MYSQL_PASSWORD=password -e MYSQL_DATABASE=appdb -p 3306:3306 -p 33060:33060 -d mysql/mysql-server:5.7


2. Run the App Container with the following env variables
MYSQL_DB_HOST=[db container ip]
MYSQL_DB_USER=appuser
MYSQL_USER_PASSWORD=password
MYSQL_DB_NAME=appdb
