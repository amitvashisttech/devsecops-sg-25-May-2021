```
 1654  cp -rf 08-Templates 09-Roles 
 1655  ls
 1656  cd 09-Roles/
 1657  ls
 1658  mkdir roles 
 1659  ls
 1660  cd roles/
 1661  ls
 1662  ansible-galaxy init webserver
 1663  ansible-galaxy init server-common
 1664  ansible-galaxy init firewalld
 1665  ll
 1666  tree webserver/
 1667  ls
 1668  vim webserver/vars/main.yml 
 1669  ls
 1670  vim webserver/tasks/main.yml 
 1671  ls
 1672  vim webserver/handlers/main.yml 
 1673  ls
 1674  cp -rf ../files/* webserver/files/
 1675  cp -rf ../templates/* webserver/templates/
 1676  ls
 1677  tree  webserver/
 1678  ls
 1679  cd ..
 1680  ls
 1681  rm -rf files templates 
 1682  ls
 1683  rm group_vars host_vars/
 1684  rm -rf group_vars host_vars README.md 
 1685  ll
 1686  vim webserver.yaml 
 1687  ls
 1688  cp -rf webserver.yaml{,.org}
 1689  ls
 1690  vim webserver.yaml
 1691  ls
 1692  ansible-playbook webserver.yaml
 1693  ls
 1694  vim roles/firewalld/tasks/main.yml 
 1695  ls
 1696  vim roles/server-common/tasks/main.yml 
 1697  ls
 1698  vim roles/server-common/tasks/ntp.html
 1699  vim roles/server-common/tasks/common-user.yaml
 1700  ls
 1701  tree 
 1702  ls
 1703  vim webserver.yaml
 1704  ls
 1705  cp -rf webserver.yaml dbservers.yaml
 1706  ls
 1707  vim dbservers.yaml 
 1708  ls
 1709  ansible-playbook webserver.yaml
 1710  ansible-playbook dbservers.yaml 
 1711  cat webserver.yaml
 1712  ls
 1713  ansible-playbook dbservers.yaml 
 1714  cd roles/server-common/
 1715  ls
 1716  cd tasks/
 1717  ls
 1718  cat main.yml 
 1719  mv ntp.html ntp.yaml
 1720  ls
 1721  cd ../../
 1722  cd ../
 1723  ;s
 1724  ls
 1725  ansible-playbook dbservers.yaml 
 1726  ls
 1727  vim dbservers.yaml 
 1728  ansible-playbook dbservers.yaml 
 1729  ls
 1730  vim dbservers.yaml 
 1731  ansible-playbook dbservers.yaml 
 1733  cat roles/server-common/tasks/main.yml 
 1734  cp -rf  roles/server-common/tasks/main.yml site.yaml
 1735  vim site.yaml 
 1736  vim dbservers.yaml 
 1737  vim site.yaml 
 1738  ansible-playbook site.yaml --check 
 1739  vim site.yaml 
 1740  ansible-playbook site.yaml --check 
 1741  ls
 1742  vim site.yaml 
 1743  ls
 1744  vim site.yaml 
 1745  ansible-playbook site.yaml --check 
 1746  vim site.yaml 
 1747  ls
 1748  ansible-playbook site.yaml --tags "web"
 1749  ansible-playbook site.yaml --tags "db"
 1750  ls
 1751  vim webserver.yaml
 1752  vim dbservers.yaml 
 1753  ansible-playbook site.yaml --tags "db"
 1754  ansible-playbook site.yaml --tags "web"
 1755  ansible-playbook site.yaml --tags "web" --limit 172.31.0.100
 1756  ls
 1757  history 
 1758  history > README.md
```
