# elastic-ccs-test

Spin up 4 Vagrant virtual machines for me to test cross cluster search (CCS) in Elasticsearch.
* VM node1 - Cluster 1 node 1
* VM node2 - Cluster 2 node 1
* VM nodekb - Kibana, connected to Cluster 1 node 1
* VM nodetest - With Elasticsearch Python client libraries and dependencies (to be manually installed), and some Python code to test CCS in Python.

Note: 
  * You will need to manually install Python 3:
  
    ```sudo yum install python3```
      
    and Elasticsearch Python client libraries: 
      
    ```pip3 install ~/*.whl```
  
  * I may eventually automate the Python 3 and libaries installation in the future.




