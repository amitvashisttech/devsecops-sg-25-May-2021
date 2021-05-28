```
1335  ls
 1336  ansible-doc -l
 1337  ansible-doc command
 1338  ls
 1339  ansible web -i testing/test_inventory -m command -a 'df -h'
 1340  date
 1341  ansible web -i testing/test_inventory -m command -a 'date'
 1342  cat /etc/os-release
 1343  ansible web -i testing/test_inventory -m command -a 'cat /etc/os-release'
 1344  cat /etc/*-release
 1345  ansible web -i testing/test_inventory -m command -a 'cat /etc/*-release'
 1346  ansible web -i testing/test_inventory -m shell -a 'cat /etc/*-release'
 1347  ansible web -i testing/test_inventory -m shell -a 'cat /etc/*-release' -vvv
 1348  ansible-doc command
```
