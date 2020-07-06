%spark2.sql
show schemas
use masai

path = "Path_to_the_file"
fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration())
list_status = fs.listStatus(spark._jvm.org.apache.hadoop.fs.Path(path))
result = [file.getPath().getName() for file in list_status]

### Small script to get all the files in HDFS sub directory
for e in result:
    p = path+e
    list_file = fs.listStatus(spark._jvm.org.apache.hadoop.fs.Path(p))
    for file in list_file:
       print(p+"/"+file.getPath().getName()) 

### check file header 
file_name = "hdfs://hdp3001/" + z.input("name")
df_test=  sqlContext.read.format("csv") \
            .option("inferSchema","true") \
            .load(file_name)
z.show(df_test.head(5))              

### Extraire les données des fichiers plats et les mettre dans une table temporaire
from  pyspark.sql.functions import input_file_name
file_name =  z.input("name")
sep = z.input("Delimiter")
has_header = z.input("Header","false")

df = sqlContext.read.format("csv") \
            .option("header", has_header) \
            .option("delimiter", sep) \
            .option("inferSchema","true")\
            .option("encoding", "UTF-8")
# uncomment for schema
df = df.schema(ot_dd_schema)
df = df.load(file_name)
df = df.withColumn("source",input_file_name())

table_name=z.input("Table Name")
df.registerTempTable(table_name)
print("[LOG]: Temporary table '"+table_name+"' has been created.")

z.show(df.limit(5))

### Requêter la table temporaire et mettre l'output dans un fichier CSV
Output = z.input("Output")
Date = z.inpuattributt("Date")

r = sqlContext.sql("""
Select * from table_name

""")
r.coalesce(1).write.mode('overwrite').option("header","true").format("com.databricks.spark.csv").csv(Output)
