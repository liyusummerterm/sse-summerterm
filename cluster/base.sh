#!/bin/bash

systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
touch /etc/resolv.conf
cat > /etc/resolv.conf << EOF
nameserver 2001:da8::666
EOF


cat > us1.ovpn << EOF
###############################################################################
# OpenVPN 2.0 Sample Configuration File
# for PacketiX VPN / SoftEther VPN Server
# 
# !!! AUTO-GENERATED BY SOFTETHER VPN SERVER MANAGEMENT TOOL !!!
# 
# !!! YOU HAVE TO REVIEW IT BEFORE USE AND MODIFY IT AS NECESSARY !!!
# 
# This configuration file is auto-generated. You might use this config file
# in order to connect to the PacketiX VPN / SoftEther VPN Server.
# However, before you try it, you should review the descriptions of the file
# to determine the necessity to modify to suitable for your real environment.
# If necessary, you have to modify a little adequately on the file.
# For example, the IP address or the hostname as a destination VPN Server
# should be confirmed.
# 
# Note that to use OpenVPN 2.0, you have to put the certification file of
# the destination VPN Server on the OpenVPN Client computer when you use this
# config file. Please refer the below descriptions carefully.

dev tun


###############################################################################
# Specify the underlying protocol beyond the Internet.
# Note that this setting must be correspond with the listening setting on
# the VPN Server.
# 
# Specify either 'proto tcp' or 'proto udp'.

proto udp
remote 2001:da8:205::58 1194

cipher AES-128-CBC
auth SHA1


###############################################################################
# Other parameters necessary to connect to the VPN Server.
# 
# It is not recommended to modify it unless you have a particular need.

resolv-retry infinite
nobind
persist-key
persist-tun
client
verb 3

###############################################################################
# Authentication with credentials.
# 
# Comment the line out in case you want to use the certificate authentication.

auth-user-pass pass.txt

<ca>
-----BEGIN CERTIFICATE-----
MIIDgjCCAmqgAwIBAgIBADANBgkqhkiG9w0BAQsFADBAMQ8wDQYDVQQDDAZtaXJy
b3IxDzANBgNVBAoMBm1pcnJvcjEPMA0GA1UECwwGbWlycm9yMQswCQYDVQQGEwJV
UzAeFw0yMDA2MjQwNzMzMTlaFw0zNzEyMzEwNzMzMTlaMEAxDzANBgNVBAMMBm1p
cnJvcjEPMA0GA1UECgwGbWlycm9yMQ8wDQYDVQQLDAZtaXJyb3IxCzAJBgNVBAYT
AlVTMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsGaI7nsWSVQtmWyO
/2n5tCblx/vRdguVFvaTD1rtelVcLfzxrcvX0ps02gOv868izpxBwHZG8OfsDCJH
euWQN89BgN2CqWth0iCkgtQJaXoAHhYKbsvn/ewhrHNWwPJBMqpkdk+xQNNGRIrk
iu8HeCUwUEaX38sd/AP6Noj+LXS7Ha/9uxNBGKO2rxFZyTjYv5XZ2NqBhtfqufJJ
yPxD1UBUA65bb+IRgavjvPntCY64Rd3LJnipnq8jpm2JOQ/yLsDfD3uT4SSXwRzV
c+gU4O3hrnzg5hzfuis3WSts4Ta75DLFyMMWuexV/1mkxruOJo8qYudi4Zj+eSu1
0eiyeQIDAQABo4GGMIGDMA8GA1UdEwEB/wQFMAMBAf8wCwYDVR0PBAQDAgH2MGMG
A1UdJQRcMFoGCCsGAQUFBwMBBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwME
BggrBgEFBQcDBQYIKwYBBQUHAwYGCCsGAQUFBwMHBggrBgEFBQcDCAYIKwYBBQUH
AwkwDQYJKoZIhvcNAQELBQADggEBAHmzKz9CXOOZKNf85UkNgisdQjBdINdT32HR
MUDCgcV5VrSv8V0AJuFSZmjtZNwVt8C0oO9YoryfAkdX1T8WaFAN/7v3x0J6QKMy
pa2DsFgIQ1XD1WE9S3v/uAdRE2m1nCYOGPgJ6wit/jRAJg0D3JlX0D0zvXYTaN99
+BX/mQXBt1uZjvXf/D8YO13W4nhsIXg9bwt3LNstOGPhu8SStkJRDLhYc15/5Hyi
OaB+rjlaozrYlE2Or71RkKBZzS4WykdYjb/LFYE/fzs/FKBlNt87NZ74HiO0grDH
4ZARgK+LqypWHxaIO7NlLTx3p2GWmkjJh2BsmIgvX7tv0rWToq8=
-----END CERTIFICATE-----

</ca>
EOF

cat > pass.txt << EOF
dd726987-90da-46ca-a7d0-2c26554ea078
dd726987-90da-46ca-a7d0-2c26554ea078
EOF

apt update