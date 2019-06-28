# ansible-debian_workstation
Ansible project to deploy my basic workstation configuration.

## Install
- install ansible, generate ssh keys, ... basics for host system
- target system shloud be a minimal debian netinstall with just a ssh server running
- put your target system into hosts
- allow your ssh key on the target system as the user root
- put your username into site.yml
- choose the desired roles in site.yml
- ansible-playbook -i hosts site.yml
- wait for deployment to finish and grab a coffee

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
  - dnscrypt (random resolver)
  - ToDo: iptables
  - ToDo: yubikey support for lightdm / su / ssh / gpg / ...
