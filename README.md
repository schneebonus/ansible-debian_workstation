# ansible-debian_workstation
Ansible project to deploy my basic workstation configuration.

## Install
- target system shloud be a minimal debian netinstall with just a ssh server running
- put your target system into hosts
- allow your ssh key on the target system as the user root
- ToDo: allow other usernames than null
- choose the desired roles in site.yml
- ansible-playbook -i hosts site.yml

## Content
- i3 desktop + configs
- basic office setup:
  - pdf viewer
  - browser setup (addons missing)
  - basic communication tools
  - nextcloud client
- basic daily tools (git, zsh, ...)
- security hardening:
  - apparmor (+ profiles)
  - firejail (+ putting apps by default into the sandbox)
  - usbguard (+ deny unknown usb devices by default)
