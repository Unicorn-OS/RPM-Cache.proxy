# Guide:
https://fedoramagazine.org/use-the-dnf-local-plugin-to-speed-up-your-home-lab/ [ark:](https://web.archive.org/web/20240110214131/https://fedoramagazine.org/use-the-dnf-local-plugin-to-speed-up-your-home-lab/)

## Automount when needed
>The role that installs and configures the NFS client does so via /etc/fstab but also takes it a step further by creating an automount for the NFS share in systemd. The automount is configured to mount the share only when needed and then to automatically unmount. This saves network bandwidth and CPU cycles which can be important for low power devices like a Raspberry Pi. See the github repository for the role and for more information.

# Doc:
- https://dnf-plugins-core.readthedocs.io/en/latest/local.html

# Discuss:
https://www.reddit.com/r/selfhosted/comments/x9zfyj/caching_server_for_fedora/

# source:
- https://github.com/buckaroogeek/ansible-role-fedora-dnf-local-plugin [ark:](https://github.com/EternalFS/ansible-role-fedora-dnf-local-plugin)
- https://github.com/buckaroogeek/dnf-local-plugin-examples [ark:](https://github.com/EternalFS/dnf-local-plugin-examples)