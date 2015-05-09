insmod /home/kernel/fs/btrfs/btrfs.ko
echo "btrfs module inserted into kernel"
mount -t btrfs /dev/sdg /mnt/btrfs_u
echo "device sdg mounted to /mnt/btrfs_u"

