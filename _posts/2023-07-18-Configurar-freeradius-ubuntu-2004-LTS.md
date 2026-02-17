---
tags: [rascunho]
---

apt-get install freeradius freeradius-postgresql postgresql postgresql-contrib

sudo -i -u postgres

createuser radius --no-superuser --no-createdb --no-createrole -P

vim /etc/postgresql/12/main/pg_hba.conf

#local   all             all                                     peer

local   all             all                                     md5

#host    replication     all             127.0.0.1/32            md5

host    replication     all             127.0.0.1/32            trust

host    all             all             192.168.1.0/24        md5

cd /etc/freeradius/3.0/mods-enabled

ln -s ../mods-available/sql

cd /etc/freeradius/3.0/mods-config/sql/main/postgresql

psql -U radius radius < schema.sql

vim etc/freeradius/3.0/mods-available/sql

dialect = "postgresql"

password = ""

login = "radius"

read_clients = yes

vim /etc/freeradius/3.0/sites-available/default

descomentar "sql"

284 authorize {

412         sql




615 accounting {

647         sql




684 session {

688         # See "Simultaneous Use Checking Queries" in mods-available/sql

689 #      sql







696 post-auth {

756         sql




853         Post-Auth-Type REJECT {

854                 # log failed authentications in SQL, too.

855                 sql







vim /etc/freeradius/3.0/dictionary

ATTRIBUTE password 1100 string







vim /etc/freeradius/3.0/policy.d/filter 

#              if ((&User-Name =~ /@/) && (&User-Name !~ /@(.+)\\.(.+)$/))  {

#                      update request {

#                              &Module-Failure-Message += 'Rejected: Realm does not have at least one dot separator'

#                      }

#                      reject

#              }







no banco para teste:




password, Simultaneous-Use, Mikrotik-Rate-Limit,Acct-Interim-Interval mudou para ':='













INSERT INTO nas (nasname,shortname,type,ports,secret) VALUES ('192.168.1.210','NAS_TESTE','other',null,'000000');







INSERT INTO  radcheck (username,attribute,op,value) VALUES ('emazolini@empresa','password',':=','senha');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('emazolini@empresa','Mikrotik-Group',':=','full');




INSERT INTO  radcheck (username,attribute,op,value) VALUES ('emazolini','password',':=','senha');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('emazolini','Mikrotik-Group',':=','full');




INSERT INTO  radcheck (username,attribute,op,value) VALUES ('cliente1','Simultaneous-Use',':=','1');

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('cliente1','password',':=','senha');

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('cliente1','Calling-Station-Id','==','C0:D1:93:9C:BA:52');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('cliente1','Mikrotik-Rate-Limit',':=','165m/330m 0k/0k 0k/0k 0/0 8 150m/300m');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('cliente1','Framed-IP-Address',':=','100.64.1.2');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('cliente1','MS-MPPE-Encryption-Types',':=','0');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('cliente1','MS-MPPE-Encryption-Policy',':=','0');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('cliente1','Acct-Interim-Interval',':=','900');







INSERT INTO  radcheck (username,attribute,op,value) VALUES ('C0:D1:93:9C:BA:53','Auth-Type',':=','Accept');

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('C0:D1:93:9C:BA:53','Service-Type',':=','Framed-User');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('C0:D1:93:9C:BA:53','Mikrotik-Wireless-Comment','==','Cliente: Notebook TESTE1');




=====================================

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Auth-Type',':=','Accept');

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Service-Type',':=','Framed-User');




#Wireless

INSERT INTO  radreply (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Mikrotik-Wireless-Comment','==','Cliente: Celular');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Mikrotik-Wireless-PSK',':=','senha-wifi');




#DHCP

INSERT INTO  radreply (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Framed-IP-Address',':=','192.168.0.220');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('FA:90:2C:E3:7A:66','Mikrotik-Rate-Limit',':=','10m/10m');




====================================



```
INSERT INTO  radcheck (username,attribute,op,value) VALUES ('D8:1F:12:9E:E0:3E','Auth-Type',':=','Accept');

INSERT INTO  radcheck (username,attribute,op,value) VALUES ('D8:1F:12:9E:E0:3E','Service-Type',':=','Framed-User');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('D8:1F:12:9E:E0:3E','Mikrotik-Wireless-Comment','==','Cliente: Notebook TESTE1');

INSERT INTO  radreply (username,attribute,op,value) VALUES ('D8:1F:12:9E:E0:3E','Mikrotik-Wireless-PSK',':=','165m/330m');
```