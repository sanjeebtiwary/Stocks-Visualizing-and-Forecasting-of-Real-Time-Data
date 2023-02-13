import psycopg2
t_host = "localhost"
t_host = "5432"
t_dbname = "visualising and forecasting stocks"
t_software = "pgAdmin 4"
t_pw = "Sanjeeb@9006"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, software=t_software, password=t_pw)
db_cursor = db_conn.cursor()