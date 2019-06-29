# ansible-debian_workstation
Ansible project to deploy my basic workstation configuration.
Got bored to repeat the same steps every time I have to set up a new workstation - so I automated it.

## Install
- install ansible, generate ssh keys, ... basics for host system
- target system shloud be a minimal debian 10 netinstall with just a ssh server running and python3
- put your target system into hosts
- allow your ssh key on the target system as the user root
- put your username into site.yml
- choose the desired roles in site.yml
- ansible-playbook -i hosts site.yml
- wait for deployment to finish and grab a coffee

## Design decisions
- Debian: It has reproducible builds. What's the use of open source software when I can't reproduce the binary and compare the hash? Without reproducability that binary could be anythin... and nobody has the time to gentoo everything.
- dns-over-tls vs dnscrypt: https://www.reddit.com/r/privacy/comments/89pr15/dnsoverhttps_vs_dns_overtls_vs_dnscrypt/

## Workstation configuration
- i3 window manager + configs (py3status, i3lock, dmenu for applications, ...)
- lightdm
- moved /tmp and caches to ramdisks
- basic office setup:
  - pdf viewer
  - browser setup (currently only chromium)
  - thunderbird
  - rambox-os
  - nextcloud client
  - keepassxc
- basic daily tools (git, zsh, z, tlp, ...)
- security hardening and improvements (lynis hardening index is 85):
  - apparmor (+ profiles + extra profiles from apparmor-gitlab)
  - firejail (+ putting apps by default into the sandbox)
  - usbguard (+ deny unknown usb devices by default)
  - random mac address after every reboot for pre defined interfaces
  - mullvad preinstalled (waiting for an account)
  - dns-over-tls
  - iptables
  - tons of sysctl changes
  - ToDo: yubikey support for lightdm / su / ssh / gpg / dmcrypt ...
- development tools
  - ToDo: ...

## ToDo:
- seperate files
- cleanup files
- add more software
