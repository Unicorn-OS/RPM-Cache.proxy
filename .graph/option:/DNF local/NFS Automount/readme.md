## Automount when needed
https://fedoramagazine.org/use-the-dnf-local-plugin-to-speed-up-your-home-lab/

quote:
>The role that installs and configures the NFS client does so via /etc/fstab but also takes it a step further by creating an automount for the NFS share in systemd. The automount is configured to mount the share only when needed and then to automatically unmount. This saves network bandwidth and CPU cycles which can be important for low power devices like a Raspberry Pi. See the github repository for the role and for more information.

source: https://github.com/buckaroogeek/ansible-role-fedora-nfs-client/blob/master/defaults/main.yaml

```
# The following option is the default setting for fstab options.
# fnm_default_options: Default NFS options to use in fstab. A key option is
# automount which will only mount the NFS share when needed and then unmount.
# See: https://www.freedesktop.org/software/systemd/man/systemd.mount.html
fnm_default_options: "_netdev,noauto,x-systemd.automount,x-systemd .mount-timeout=10,timeo=14,x-systemd.idle-timeout=1min"
```