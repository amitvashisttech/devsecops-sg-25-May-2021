```
 1353  ansible web -i testing/test_inventory -m user -a "name={{username}} password=12345"
 1354  ansible web -i production/prod_inventory -m user -a "name={{username}} password=12345"
 1355  ansible web -i production/prod_inventory -m user -a "name={{username}} password=12345" -s
 1356  ansible all -i production/prod_inventory -m user -a "name={{username}} password=12345" -s
 1357  tree production/
 1358  cat production/group_vars/all
 1359  cat production/prod_inventory
 1360  vim production/prod_inventory
 1361  ls
 1362  ansible all -i production/prod_inventory -m user -a "name={{username}} password=12345" -s
 1363  cp -rf production/group_vars/all production/group_vars/web
 1364  vim production/group_vars/web
 1365  tree production/
 1366  ansible all -i production/prod_inventory -m user -a "name={{username}} password=12345" -s
 1367  ls
 1368  cp -rf production/group_vars/all production/host_vars/172.31.0.100
 1369  vim production/host_vars/172.31.0.100
 1370  ansible all -i production/prod_inventory -m user -a "name={{username}} password=12345" -s
```
