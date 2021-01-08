# from subprocess import Popen, PIPE
# hdfs_path = '/user/flume/tweets'
# process = Popen('/home/manojkhatokar/Downloads/work/hadoop-2.7.2/bin/hdfs.sh dfs -ls /user/flume/tweets', shell=True, stdout=PIPE, stderr=PIPE)
# std_out, std_err = process.communicate()
# print(std_out,std_err)
# list_of_file_names = [fn.split(' ')[-1].split('/')[-1] for fn in std_out.decode().split('\n')[1:]][:-1]
# list_of_file_names_with_full_address = [fn.split(' ')[-1] for fn in std_out.decode().split('\n')[1:]][:-1]
# print(list_of_file_names)
# print(list_of_file_names_with_full_address)

# import sh
# hdfsdir = '/home/manojkhatokar/Downloads/work/hadoop-2.7.2/bin/./hdfs.sh'
# sh.hdfs('dfs','-ls',hdfsdir)

# importing the library 
# from snakebite.client import Client 

  
# # the below line create client connection to the HDFS NameNode 
# client = Client('localhost', 9000) 
# print(client.text(['/user/flume/tweets/merged_20210101133906']))
# # iterate over data.txt file and will show all the content of data.txt 
# for l in client.text(['/user/flume/tweets/merged_20210101133906']): 
#         print l


from snakebite.client import Client 
import json

def get_json_object():

    client = Client('localhost', 9000) #merged filename is hardcoded , you hav to keep changing the filename for every analysis!!
    for a in client.copyToLocal(['/user/flume/tweets/merged_20210102123709.json'], '/home/manojkhatokar/Downloads/BGD/final_python_scripts/merged_data'):
        print(a)


    # with open('/home/manojkhatokar/Downloads/merged_20210101142527.json') as f:
    #     raw_data = f.read().splitlines()[-1]
    #     list_data = f'[{raw_data}]'
    #     json_data = json.loads(list_data)
    #     print(json_data)

    json_file =  open('/home/manojkhatokar/Downloads/BGD/final_python_scripts/merged_data/merged_20210102123709.json')
    json_object = json.load(json_file)
    json_file.close
    return json_object
