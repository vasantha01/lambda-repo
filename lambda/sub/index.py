import psycopg2
import boto3
from config import config
s3 = boto3.client('s3')
def lambda_handler(event, context):
    conn = None
    # read connection parameters
    rsparams= config()
    # connect to the Redshift server
    print('Connecting to the Greenplum Database...')
    conn = psycopg2.connect(**rsparams)
    print(conn)
    conn = psycopg2.connect(dbname="aims_bi_dev", user="aimsbi-dev", password="Aimsbi0123", port=5439,host="aims-bi-redshiftcluster-eu-central-1-195644677231.cqxzffz280ih.eu-central-1.redshift.amazonaws.com")
    print(conn)
    cur = conn.cursor()
    print("redshift connected successfully")
    bucket_name = "ranibucket2"
    #folder_name = "lambda-poc-test1/aims-bi-app/sql/wipo_emr_ddl_scripts.sql"
    folder_name = "wipo_emr_ddl_scripts.sql
    data = s3.get_object(Bucket=bucket_name, Key=(folder_name))
    #data = s3.get_object(Bucket='analytics-v1-application-eu-central-1-195644677231/aims-bi-app/sql/', Key='wipo_emr_ddl_scripts.sql')
    print(type(data))
    contents = data['Body'].read()
    print(contents)
    cur.execute(contents)
    cur.execute("commit")
    cur.close()
    conn.close()


