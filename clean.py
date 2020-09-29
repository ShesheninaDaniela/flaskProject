import os

clean_container = 'docker rm -f `docker ps -a | grep \'test_calculator\' | awk \'{print $1;}\'`'
print(str(os.system(clean_container)))
