# ansible-debian_workstation
Ansible project to deploy my basic workstation configuration.
Got bored to repeat the same steps every time I have to set up a new workstation - so I automated it.

## Install
- install ansible, generate ssh keys, ... basics for host system
- target system shloud be a minimal debian netinstall with just a ssh server running
- put your target system into hosts
- allow your ssh key on the target system as the user root
- put your username into site.yml
- choose the desired roles in site.yml
- ansible-playbook -i hosts site.yml
- wait for deployment to finish and grab a coffee

## Design decisions
- Debian: It has reproducible builds. What's the use of open source software when I can't reproduce the binary and compare the hash? Without reproducability that binary could be anythin.
- dns-over-tls vs dnscrypt: https://www.reddit.com/r/privacy/comments/89pr15/dnsoverhttps_vs_dns_overtls_vs_dnscrypt/

## Workstation configuration
- i3 desktop + configs
- lightdm
- basic office setup:
  - pdf viewer
  - browser setup (ToDo: addons missing)
  - basic communication tools
  - nextcloud client
- basic daily tools (git, zsh, ...)
- security hardening and improvements:
  - apparmor (+ profiles)
  - firejail (+ putting apps by default into the sandbox)
  - usbguard (+ deny unknown usb devices by default)
  - ToDo: dns-over-tls
  - ToDo: iptables
  - ToDo: yubikey support for lightdm / su / ssh / gpg / ...
- development tools
  - ToDo: ...
