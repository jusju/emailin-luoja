rivi1 = "root:x:0:0:root:/root:/bin/bash"
rivi2 = "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin"
rivi3 = "bin:x:2:2:bin:/bin:/usr/sbin/nologin"
rivi4 = "sys:x:3:3:sys:/dev:/usr/sbin/nologin"

rivi1taulukko = rivi1.split(":");
print(rivi1taulukko[0] + "@myy.haaga-helia.fi");




