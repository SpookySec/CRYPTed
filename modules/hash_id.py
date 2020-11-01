# taken from: https://github.com/psypanda/hashID

import sys
import re
from collections import namedtuple

Prototype = namedtuple('Prototype', ['regex', 'modes'])
HashInfo = namedtuple('HashInfo', ['name', 'hashcat', 'john'])


prototypes = [
    Prototype(
        regex=re.compile(r'^[a-f0-9]{4}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CRC-16', hashcat=None, john=None),
            HashInfo(name='CRC-16-CCITT', hashcat=None, john=None),
            HashInfo(name='FCS-16', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Adler-32', hashcat=None, john=None),
            HashInfo(name='CRC-32B', hashcat=None, john=None),
            HashInfo(name='FCS-32', hashcat=None, john=None),
            HashInfo(name='GHash-32-3', hashcat=None, john=None),
            HashInfo(name='GHash-32-5', hashcat=None, john=None),
            HashInfo(name='FNV-132', hashcat=None, john=None),
            HashInfo(name='Fletcher-32', hashcat=None, john=None),
            HashInfo(name='Joaat', hashcat=None, john=None),
            HashInfo(name='ELF-32', hashcat=None, john=None),
            HashInfo(name='XOR-32', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{6}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CRC-24', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$crc32\$[a-f0-9]{8}.)?[a-f0-9]{8}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CRC-32', hashcat=None, john='crc32')]),
    Prototype(
        regex=re.compile(r'^\+[a-z0-9\/.]{12}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Eggdrop IRC Bot', hashcat=None, john='bfegg')]),
    Prototype(
        regex=re.compile(r'^[a-z0-9\/.]{13}$', re.IGNORECASE),
        modes=[
            HashInfo(name='DES(Unix)', hashcat=1500, john='descrypt'),
            HashInfo(name='Traditional DES', hashcat=1500, john='descrypt'),
            HashInfo(name='DEScrypt', hashcat=1500, john='descrypt')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MySQL323', hashcat=200, john='mysql'),
            HashInfo(name='DES(Oracle)', hashcat=3100, john=None),
            HashInfo(name='Half MD5', hashcat=5100, john=None),
            HashInfo(name='Oracle 7-10g', hashcat=3100, john=None),
            HashInfo(name='FNV-164', hashcat=None, john=None),
            HashInfo(name='CRC-64', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9\/.]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco-PIX(MD5)', hashcat=2400, john='pix-md5')]),
    Prototype(
        regex=re.compile(r'^\([a-z0-9\/+]{20}\)$', re.IGNORECASE),
        modes=[
            HashInfo(name='Lotus Notes/Domino 6', hashcat=8700, john='dominosec')]),
    Prototype(
        regex=re.compile(r'^_[a-z0-9\/.]{19}$', re.IGNORECASE),
        modes=[
            HashInfo(name='BSDi Crypt', hashcat=None, john='bsdicrypt')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{24}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CRC-96(ZIP)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9\/.]{24}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Crypt16', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$md2\$)?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD2', hashcat=None, john='md2')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD5', hashcat=0, john='raw-md5'),
            HashInfo(name='MD4', hashcat=900, john='raw-md4'),
            HashInfo(name='Double MD5', hashcat=2600, john=None),
            HashInfo(name='LM', hashcat=3000, john='lm'),
            HashInfo(name='RIPEMD-128', hashcat=None, john='ripemd-128'),
            HashInfo(name='Haval-128', hashcat=None, john='haval-128-4'),
            HashInfo(name='Tiger-128', hashcat=None, john=None),
            HashInfo(name='Skein-256(128)', hashcat=None, john=None),
            HashInfo(name='Skein-512(128)', hashcat=None, john=None),
            HashInfo(name='Lotus Notes/Domino 5', hashcat=8600, john='lotus5'),
            HashInfo(name='Skype', hashcat=23, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$snefru\$)?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Snefru-128', hashcat=None, john='snefru-128')]),
    Prototype(
        regex=re.compile(r'^(\$NT\$)?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='NTLM', hashcat=1000, john='nt')]),
    Prototype(
        regex=re.compile(r'^([^\\\/:*?"<>|]{1,20}:)?[a-f0-9]{32}(:[^\\\/:*?"<>|]{1,20})?$', re.IGNORECASE),
        modes=[
            HashInfo(name='Domain Cached Credentials', hashcat=1100, john='mscach')]),
    Prototype(
        regex=re.compile(r'^([^\\\/:*?"<>|]{1,20}:)?(\$DCC2\$10240#[^\\\/:*?"<>|]{1,20}#)?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Domain Cached Credentials 2', hashcat=2100, john='mscach2')]),
    Prototype(
        regex=re.compile(r'^{SHA}[a-z0-9\/+]{27}=$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-1(Base64)', hashcat=101, john='nsldap'),
            HashInfo(name='Netscape LDAP SHA', hashcat=101, john='nsldap')]),
    Prototype(
        regex=re.compile(r'^\$1\$[a-z0-9\/.]{0,8}\$[a-z0-9\/.]{22}(:.*)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD5 Crypt', hashcat=500, john='md5crypt'),
            HashInfo(name='Cisco-IOS(MD5)', hashcat=500, john='md5crypt'),
            HashInfo(name='FreeBSD MD5', hashcat=500, john='md5crypt')]),
    Prototype(
        regex=re.compile(r'^0x[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Lineage II C4', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$H\$[a-z0-9\/.]{31}$', re.IGNORECASE),
        modes=[
            HashInfo(name='phpBB v3.x', hashcat=400, john='phpass'),
            HashInfo(name='Wordpress v2.6.0/2.6.1', hashcat=400, john='phpass'),
            HashInfo(name="PHPass' Portable Hash", hashcat=400, john='phpass')]),
    Prototype(
        regex=re.compile(r'^\$P\$[a-z0-9\/.]{31}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'Wordpress ≥ v2.6.2', hashcat=400, john='phpass'),
            HashInfo(name=u'Joomla ≥ v2.5.18', hashcat=400, john='phpass'),
            HashInfo(name="PHPass' Portable Hash", hashcat=400, john='phpass')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:[a-z0-9]{2}$', re.IGNORECASE),
        modes=[
            HashInfo(name='osCommerce', hashcat=21, john=None),
            HashInfo(name='xt:Commerce', hashcat=21, john=None)]),
    Prototype(
        regex=re.compile(r'^\$apr1\$[a-z0-9\/.]{0,8}\$[a-z0-9\/.]{22}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD5(APR)', hashcat=1600, john=None),
            HashInfo(name='Apache MD5', hashcat=1600, john=None)]),
    Prototype(
        regex=re.compile(r'^{smd5}[a-z0-9$\/.]{31}$', re.IGNORECASE),
        modes=[
            HashInfo(name='AIX(smd5)', hashcat=6300, john='aix-smd5')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='WebEdition CMS', hashcat=3721, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:.{5}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'IP.Board ≥ v2+', hashcat=2811, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:.{8}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'MyBB ≥ v1.2+', hashcat=2811, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9]{34}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CryptoCurrency(Adress)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{40}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-1', hashcat=100, john='raw-sha1'),
            HashInfo(name='Double SHA-1', hashcat=4500, john=None),
            HashInfo(name='RIPEMD-160', hashcat=6000, john='ripemd-160'),
            HashInfo(name='Haval-160', hashcat=None, john=None),
            HashInfo(name='Tiger-160', hashcat=None, john=None),
            HashInfo(name='HAS-160', hashcat=None, john=None),
            HashInfo(name='LinkedIn', hashcat=190, john='raw-sha1-linkedin'),
            HashInfo(name='Skein-256(160)', hashcat=None, john=None),
            HashInfo(name='Skein-512(160)', hashcat=None, john=None)]),

    Prototype(
        regex=re.compile(r'^\*[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MySQL5.x', hashcat=300, john='mysql-sha1'),
            HashInfo(name='MySQL4.1', hashcat=300, john='mysql-sha1')]),
    Prototype(
        regex=re.compile(r'^[a-z0-9]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco-IOS(SHA-256)', hashcat=5700, john=None)]),
    Prototype(
        regex=re.compile(r'^{SSHA}[a-z0-9\/+]{38}==$', re.IGNORECASE),
        modes=[
            HashInfo(name='SSHA-1(Base64)', hashcat=111, john='nsldaps'),
            HashInfo(name='Netscape LDAP SSHA', hashcat=111, john='nsldaps')]),
    Prototype(
        regex=re.compile(r'^[a-z0-9=]{47}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Fortigate(FortiOS)', hashcat=7000, john='fortigate')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{48}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Haval-192', hashcat=None, john=None),
            HashInfo(name='Tiger-192', hashcat=None, john='tiger'),
            HashInfo(name='SHA-1(Oracle)', hashcat=None, john=None),
            HashInfo(name='OSX v10.4', hashcat=122, john='xsha'),
            HashInfo(name='OSX v10.5', hashcat=122, john='xsha'),
            HashInfo(name='OSX v10.6', hashcat=122, john='xsha')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{51}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Palshop CMS', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9]{51}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CryptoCurrency(PrivateKey)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^{ssha1}[0-9]{2}\$[a-z0-9$\/.]{44}$', re.IGNORECASE),
        modes=[
            HashInfo(name='AIX(ssha1)', hashcat=6700, john='aix-ssha1')]),
    Prototype(
        regex=re.compile(r'^0x0100[a-f0-9]{48}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MSSQL(2005)', hashcat=132, john='mssql05'),
            HashInfo(name='MSSQL(2008)', hashcat=132, john='mssql05')]),
    Prototype(
        regex=re.compile(r'^(\$md5,rounds=[0-9]+\$|\$md5\$rounds=[0-9]+\$|\$md5\$)[a-z0-9\/.]{0,16}(\$|\$\$)[a-z0-9\/.]{22}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Sun MD5 Crypt', hashcat=3300, john='sunmd5')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{56}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-224', hashcat=None, john='raw-sha224'),
            HashInfo(name='Haval-224', hashcat=None, john=None),
            HashInfo(name='SHA3-224', hashcat=None, john=None),
            HashInfo(name='Skein-256(224)', hashcat=None, john=None),
            HashInfo(name='Skein-512(224)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Blowfish(OpenBSD)', hashcat=3200, john='bcrypt'),
            HashInfo(name='Woltlab Burning Board 4.x', hashcat=None, john=None),
            HashInfo(name='bcrypt', hashcat=3200, john='bcrypt')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{40}:[a-f0-9]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Android PIN', hashcat=5800, john=None)]),
    Prototype(
        regex=re.compile(r'^(S:)?[a-f0-9]{40}(:)?[a-f0-9]{20}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Oracle 11g/12c', hashcat=112, john='oracle11')]),
    Prototype(
        regex=re.compile(r'^\$bcrypt-sha256\$(2[axy]|2)\,[0-9]+\$[a-z0-9\/.]{22}\$[a-z0-9\/.]{31}$', re.IGNORECASE),
        modes=[
            HashInfo(name='bcrypt(SHA-256)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:.{3}$', re.IGNORECASE),
        modes=[
            HashInfo(name='vBulletin < v3.8.5', hashcat=2611, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:.{30}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'vBulletin ≥ v3.8.5', hashcat=2711, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$snefru\$)?[a-f0-9]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Snefru-256', hashcat=None, john='snefru-256')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{64}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-256', hashcat=1400, john='raw-sha256'),
            HashInfo(name='RIPEMD-256', hashcat=None, john=None),
            HashInfo(name='Haval-256', hashcat=None, john='haval-256-3'),
            HashInfo(name='GOST R 34.11-94', hashcat=6900, john='gost'),
            HashInfo(name='GOST CryptoPro S-Box', hashcat=None, john=None),
            HashInfo(name='SHA3-256', hashcat=5000, john='raw-keccak-256'),
            HashInfo(name='Skein-256', hashcat=None, john='skein-256'),
            HashInfo(name='Skein-512(256)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:[a-z0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Joomla < v2.5.18', hashcat=11, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f-0-9]{32}:[a-f-0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SAM(LM_Hash:NT_Hash)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$chap\$0\*)?[a-f0-9]{32}[\*:][a-f0-9]{32}(:[0-9]{2})?$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD5(Chap)', hashcat=4800, john='chap'),
            HashInfo(name='iSCSI CHAP Authentication', hashcat=4800, john='chap')]),
    Prototype(
        regex=re.compile(r'^\$episerver\$\*0\*[a-z0-9\/=+]+\*[a-z0-9\/=+]{27,28}$', re.IGNORECASE),
        modes=[
            HashInfo(name='EPiServer 6.x < v4', hashcat=141, john='episerver')]),
    Prototype(
        regex=re.compile(r'^{ssha256}[0-9]{2}\$[a-z0-9$\/.]{60}$', re.IGNORECASE),
        modes=[
            HashInfo(name='AIX(ssha256)', hashcat=6400, john='aix-ssha256')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{80}$', re.IGNORECASE),
        modes=[
            HashInfo(name='RIPEMD-320', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$episerver\$\*1\*[a-z0-9\/=+]+\*[a-z0-9\/=+]{42,43}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'EPiServer 6.x ≥ v4', hashcat=1441, john='episerver')]),
    Prototype(
        regex=re.compile(r'^0x0100[a-f0-9]{88}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MSSQL(2000)', hashcat=131, john='mssql')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{96}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-384', hashcat=10800, john='raw-sha384'),
            HashInfo(name='SHA3-384', hashcat=None, john=None),
            HashInfo(name='Skein-512(384)', hashcat=None, john=None),
            HashInfo(name='Skein-1024(384)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^{SSHA512}[a-z0-9\/+]{96}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SSHA-512(Base64)', hashcat=1711, john='ssha512'),
            HashInfo(name='LDAP(SSHA-512)', hashcat=1711, john='ssha512')]),
    Prototype(
        regex=re.compile(r'^{ssha512}[0-9]{2}\$[a-z0-9\/.]{16,48}\$[a-z0-9\/.]{86}$', re.IGNORECASE),
        modes=[
            HashInfo(name='AIX(ssha512)', hashcat=6500, john='aix-ssha512')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{128}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-512', hashcat=1700, john='raw-sha512'),
            HashInfo(name='Whirlpool', hashcat=6100, john='whirlpool'),
            HashInfo(name='Salsa10', hashcat=None, john=None),
            HashInfo(name='Salsa20', hashcat=None, john=None),
            HashInfo(name='SHA3-512', hashcat=None, john='raw-keccak'),
            HashInfo(name='Skein-512', hashcat=None, john='skein-512'),
            HashInfo(name='Skein-1024(512)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{136}$', re.IGNORECASE),
        modes=[
            HashInfo(name='OSX v10.7', hashcat=1722, john='xsha512')]),
    Prototype(
        regex=re.compile(r'^0x0200[a-f0-9]{136}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MSSQL(2012)', hashcat=1731, john='msql12'),
            HashInfo(name='MSSQL(2014)', hashcat=1731, john='msql12')]),
    Prototype(
        regex=re.compile(r'^\$ml\$[0-9]+\$[a-f0-9]{64}\$[a-f0-9]{128}$', re.IGNORECASE),
        modes=[
            HashInfo(name='OSX v10.8', hashcat=7100, john='pbkdf2-hmac-sha512'),
            HashInfo(name='OSX v10.9', hashcat=7100, john='pbkdf2-hmac-sha512')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{256}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Skein-1024', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^grub\.pbkdf2\.sha512\.[0-9]+\.([a-f0-9]{128,2048}\.|[0-9]+\.)?[a-f0-9]{128}$', re.IGNORECASE),
        modes=[
            HashInfo(name='GRUB 2', hashcat=7200, john=None)]),
    Prototype(
        regex=re.compile(r'^sha1\$[a-z0-9]+\$[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(SHA-1)', hashcat=124, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{49}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Citrix Netscaler', hashcat=8100, john='citrix_ns10')]),
    Prototype(
        regex=re.compile(r'^\$S\$[a-z0-9\/.]{52}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Drupal > v7.x', hashcat=7900, john='drupal7')]),
    Prototype(
        regex=re.compile(r'^\$5\$(rounds=[0-9]+\$)?[a-z0-9\/.]{0,16}\$[a-z0-9\/.]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-256 Crypt', hashcat=7400, john='sha256crypt')]),
    Prototype(
        regex=re.compile(r'^0x[a-f0-9]{4}[a-f0-9]{16}[a-f0-9]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Sybase ASE', hashcat=8000, john='sybasease')]),
    Prototype(
        regex=re.compile(r'^\$6\$(rounds=[0-9]+\$)?[a-z0-9\/.]{0,16}\$[a-z0-9\/.]{86}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-512 Crypt', hashcat=1800, john='sha512crypt')]),
    Prototype(
        regex=re.compile(r'^\$sha\$[a-z0-9]{1,16}\$([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64}|[a-f0-9]{128}|[a-f0-9]{140})$', re.IGNORECASE),
        modes=[
            HashInfo(name='Minecraft(AuthMe Reloaded)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^sha256\$[a-z0-9]+\$[a-f0-9]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(SHA-256)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^sha384\$[a-z0-9]+\$[a-f0-9]{96}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(SHA-384)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^crypt1:[a-z0-9+=]{12}:[a-z0-9+=]{12}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Clavister Secure Gateway', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{112}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco VPN Client(PCF-File)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{1329}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Microsoft MSTSC(RDP-File)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[^\\\/:*?"<>|]{1,20}[:]{2,3}([^\\\/:*?"<>|]{1,20})?:[a-f0-9]{48}:[a-f0-9]{48}:[a-f0-9]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='NetNTLMv1-VANILLA / NetNTLMv1+ESS', hashcat=5500, john='netntlm')]),
    Prototype(
        regex=re.compile(r'^([^\\\/:*?"<>|]{1,20}\\)?[^\\\/:*?"<>|]{1,20}[:]{2,3}([^\\\/:*?"<>|]{1,20}:)?[^\\\/:*?"<>|]{1,20}:[a-f0-9]{32}:[a-f0-9]+$', re.IGNORECASE),
        modes=[
            HashInfo(name='NetNTLMv2', hashcat=5600, john='netntlmv2')]),
    Prototype(
        regex=re.compile(r'^\$(krb5pa|mskrb5)\$([0-9]{2})?\$.+\$[a-f0-9]{1,}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Kerberos 5 AS-REQ Pre-Auth', hashcat=7500, john='krb5pa-md5')]),
    Prototype(
        regex=re.compile(r'^\$scram\$[0-9]+\$[a-z0-9\/.]{16}\$sha-1=[a-z0-9\/.]{27},sha-256=[a-z0-9\/.]{43},sha-512=[a-z0-9\/.]{86}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SCRAM Hash', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{40}:[a-f0-9]{0,32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Redmine Project Management Web App', hashcat=7600, john=None)]),
    Prototype(
        regex=re.compile(r'^(.+)?\$[a-f0-9]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SAP CODVN B (BCODE)', hashcat=7700, john='sapb')]),
    Prototype(
        regex=re.compile(r'^(.+)?\$[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SAP CODVN F/G (PASSCODE)', hashcat=7800, john='sapg')]),
    Prototype(
        regex=re.compile(r'^(.+\$)?[a-z0-9\/.+]{30}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='Juniper Netscreen/SSG(ScreenOS)', hashcat=22, john='md5ns')]),
    Prototype(
        regex=re.compile(r'^0x[a-f0-9]{60}\s0x[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='EPi', hashcat=123, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{40}:[^*]{1,25}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'SMF ≥ v1.1', hashcat=121, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$wbb3\$\*1\*)?[a-f0-9]{40}[:*][a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Woltlab Burning Board 3.x', hashcat=8400, john='wbb3')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{130}(:[a-f0-9]{40})?$', re.IGNORECASE),
        modes=[
            HashInfo(name='IPMI2 RAKP HMAC-SHA1', hashcat=7300, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}:[0-9]+:[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$', re.IGNORECASE),
        modes=[
            HashInfo(name='Lastpass', hashcat=6800, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9\/.]{16}([:$].{1,})?$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco-ASA(MD5)', hashcat=2410, john='asa-md5')]),
    Prototype(
        regex=re.compile(r'^\$vnc\$\*[a-f0-9]{32}\*[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='VNC', hashcat=None, john='vnc')]),
    Prototype(
        regex=re.compile(r'^[a-z0-9]{32}(:([a-z0-9-]+\.)?[a-z0-9-.]+\.[a-z]{2,7}:.+:[0-9]+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='DNSSEC(NSEC3)', hashcat=8300, john=None)]),
    Prototype(
        regex=re.compile(r'^(user-.+:)?\$racf\$\*.+\*[a-f0-9]{16}$', re.IGNORECASE),
        modes=[
            HashInfo(name='RACF', hashcat=8500, john='racf')]),
    Prototype(
        regex=re.compile(r'^\$3\$\$[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='NTHash(FreeBSD Variant)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$sha1\$[0-9]+\$[a-z0-9\/.]{0,64}\$[a-z0-9\/.]{28}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-1 Crypt', hashcat=None, john='sha1crypt')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{70}$', re.IGNORECASE),
        modes=[
            HashInfo(name='hMailServer', hashcat=1421, john='hmailserver')]),
    Prototype(
        regex=re.compile(r'^[:\$][AB][:\$]([a-f0-9]{1,8}[:\$])?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MediaWiki', hashcat=3711, john='mediawiki')]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{140}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Minecraft(xAuth)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$pbkdf2(-sha1)?\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{27}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2-SHA1(Generic)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$pbkdf2-sha256\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2-SHA256(Generic)', hashcat=None, john='pbkdf2-hmac-sha256')]),
    Prototype(
        regex=re.compile(r'^\$pbkdf2-sha512\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{86}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2-SHA512(Generic)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$p5k2\$[0-9]+\$[a-z0-9\/+=-]+\$[a-z0-9\/+-]{27}=$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2(Cryptacular)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$p5k2\$[0-9]+\$[a-z0-9\/.]+\$[a-z0-9\/.]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2(Dwayne Litzenberger)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^{FSHP[0123]\|[0-9]+\|[0-9]+}[a-z0-9\/+=]+$', re.IGNORECASE),
        modes=[
            HashInfo(name='Fairly Secure Hashed Password', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$PHPS\$.+\$[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PHPS', hashcat=2612, john='phps')]),
    Prototype(
        regex=re.compile(r'^[0-9]{4}:[a-f0-9]{16}:[a-f0-9]{2080}$', re.IGNORECASE),
        modes=[
            HashInfo(name='1Password(Agile Keychain)', hashcat=6600, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{64}:[a-f0-9]{32}:[0-9]{5}:[a-f0-9]{608}$', re.IGNORECASE),
        modes=[
            HashInfo(name='1Password(Cloud Keychain)', hashcat=8200, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{256}:[a-f0-9]{256}:[a-f0-9]{16}:[a-f0-9]{16}:[a-f0-9]{320}:[a-f0-9]{16}:[a-f0-9]{40}:[a-f0-9]{40}:[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='IKE-PSK MD5', hashcat=5300, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{256}:[a-f0-9]{256}:[a-f0-9]{16}:[a-f0-9]{16}:[a-f0-9]{320}:[a-f0-9]{16}:[a-f0-9]{40}:[a-f0-9]{40}:[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='IKE-PSK SHA1', hashcat=5400, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-z0-9\/+]{27}=$', re.IGNORECASE),
        modes=[
            HashInfo(name='PeopleSoft', hashcat=133, john=None)]),
    Prototype(
        regex=re.compile(r'^crypt\$[a-f0-9]{5}\$[a-z0-9\/.]{13}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(DES Crypt Wrapper)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$django\$\*1\*)?pbkdf2_sha256\$[0-9]+\$[a-z0-9]+\$[a-z0-9\/+=]{44}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(PBKDF2-HMAC-SHA256)', hashcat=10000, john='django')]),
    Prototype(
        regex=re.compile(r'^pbkdf2_sha1\$[0-9]+\$[a-z0-9]+\$[a-z0-9\/+=]{28}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(PBKDF2-HMAC-SHA1)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^bcrypt(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(bcrypt)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^md5\$[a-f0-9]+\$[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(MD5)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\{PKCS5S2\}[a-z0-9\/+]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2(Atlassian)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^md5[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PostgreSQL MD5', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\([a-z0-9\/+]{49}\)$', re.IGNORECASE),
        modes=[
            HashInfo(name='Lotus Notes/Domino 8', hashcat=9100, john=None)]),
    Prototype(
        regex=re.compile(r'^SCRYPT:[0-9]{1,}:[0-9]{1}:[0-9]{1}:[a-z0-9:\/+=]{1,}$', re.IGNORECASE),
        modes=[
            HashInfo(name='scrypt', hashcat=8900, john=None)]),
    Prototype(
        regex=re.compile(r'^\$8\$[a-z0-9\/.]{14}\$[a-z0-9\/.]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco Type 8', hashcat=9200, john='cisco8')]),
    Prototype(
        regex=re.compile(r'^\$9\$[a-z0-9\/.]{14}\$[a-z0-9\/.]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco Type 9', hashcat=9300, john='cisco9')]),
    Prototype(
        regex=re.compile(r'^\$office\$\*2007\*[0-9]{2}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Microsoft Office 2007', hashcat=9400, john='office')]),
    Prototype(
        regex=re.compile(r'^\$office\$\*2010\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Microsoft Office 2010', hashcat=9500, john=None)]),
    Prototype(
        regex=re.compile(r'^\$office\$\*2013\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Microsoft Office 2013', hashcat=9600, john=None)]),
    Prototype(
        regex=re.compile(r'^\$fde\$[0-9]{2}\$[a-f0-9]{32}\$[0-9]{2}\$[a-f0-9]{32}\$[a-f0-9]{3072}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'Android FDE ≤ 4.3', hashcat=8800, john='fde')]),
    Prototype(
        regex=re.compile(r'^\$oldoffice\$[01]\*[a-f0-9]{32}\*[a-f0-9]{32}\*[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'Microsoft Office ≤ 2003 (MD5+RC4)', hashcat=9700, john='oldoffice'),
            HashInfo(name=u'Microsoft Office ≤ 2003 (MD5+RC4) collider-mode #1', hashcat=9710, john='oldoffice'),
            HashInfo(name=u'Microsoft Office ≤ 2003 (MD5+RC4) collider-mode #2', hashcat=9720, john='oldoffice')]),
    Prototype(
        regex=re.compile(r'^\$oldoffice\$[34]\*[a-f0-9]{32}\*[a-f0-9]{32}\*[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name=u'Microsoft Office ≤ 2003 (SHA1+RC4)', hashcat=9800, john=None),
            HashInfo(name=u'Microsoft Office ≤ 2003 (SHA1+RC4) collider-mode #1', hashcat=9810, john=None),
            HashInfo(name=u'Microsoft Office ≤ 2003 (SHA1+RC4) collider-mode #2', hashcat=9820, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$radmin2\$)?[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='RAdmin v2.x', hashcat=9900, john='radmin')]),
    Prototype(
        regex=re.compile(r'^{x-issha,\s[0-9]{4}}[a-z0-9\/+=]+$', re.IGNORECASE),
        modes=[
            HashInfo(name='SAP CODVN H (PWDSALTEDHASH) iSSHA-1', hashcat=10300, john='saph')]),
    Prototype(
        regex=re.compile(r'^\$cram_md5\$[a-z0-9\/+=-]+\$[a-z0-9\/+=-]{52}$', re.IGNORECASE),
        modes=[
            HashInfo(name='CRAM-MD5', hashcat=10200, john=None)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{16}:2:4:[a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='SipHash', hashcat=10100, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$cisco4\$)?[a-z0-9\/.]{43}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Cisco Type 4', hashcat=None, john='cisco4')]),
    Prototype(
        regex=re.compile(r'^bcrypt_sha256\$\$(2[axy]|2)\$[0-9]+\$[a-z0-9\/.]{53}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Django(bcrypt-SHA256)', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^\$postgres\$.[^\*]+[*:][a-f0-9]{1,32}[*:][a-f0-9]{32}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PostgreSQL Challenge-Response Authentication (MD5)', hashcat=11100, john='postgres')]),
    Prototype(
        regex=re.compile(r'^\$siemens-s7\$[0-9]{1}\$[a-f0-9]{40}\$[a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Siemens-S7', hashcat=None, john='siemens-s7')]),
    Prototype(
        regex=re.compile(r'^(\$pst\$)?[a-f0-9]{8}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Microsoft Outlook PST', hashcat=None, john=None)]),
    Prototype(
        regex=re.compile(r'^sha256[:$][0-9]+[:$][a-z0-9\/+]+[:$][a-z0-9\/+]{32,128}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PBKDF2-HMAC-SHA256(PHP)', hashcat=10900, john=None)]),
    Prototype(
        regex=re.compile(r'^(\$dahua\$)?[a-z0-9]{8}$', re.IGNORECASE),
        modes=[
            HashInfo(name='Dahua', hashcat=None, john='dahua')]),
    Prototype(
        regex=re.compile(r'^\$mysqlna\$[a-f0-9]{40}[:*][a-f0-9]{40}$', re.IGNORECASE),
        modes=[
            HashInfo(name='MySQL Challenge-Response Authentication (SHA1)', hashcat=11200, john=None)]),
    Prototype(
        regex=re.compile(r'^\$pdf\$[24]\*[34]\*128\*[0-9-]{1,5}\*1\*(16|32)\*[a-f0-9]{32,64}\*32\*[a-f0-9]{64}\*(8|16|32)\*[a-f0-9]{16,64}$', re.IGNORECASE),
        modes=[
            HashInfo(name='PDF 1.4 - 1.6 (Acrobat 5 - 8)', hashcat=10500, john='pdf')])
]

class HashID(object):

    """HashID with configurable prototypes"""

    def __init__(self, prototypes=prototypes):
        super(HashID, self).__init__()
        self.prototypes = list(prototypes)

    def identifyHash(self, phash):
        """Returns identified HashInfo"""
        phash = phash.strip()
        for prototype in self.prototypes:
            if prototype.regex.match(phash):
                for mode in prototype.modes:
                    yield mode

def parseHashes(identified_modes):
    count = 0
    hashTypes = []
    for mode in identified_modes:
        count += 1
        hashTypes.append(mode.name)
    return hashTypes