__title__ = 'bwh'
__version__ = '0.0.1'
__author__ = 'ansheng'
__email__ = 'ianshengme@gmail.com'

from urllib.parse import urljoin

import requests


class BwhSdk:
    """
    bandwagonhost panel api sdk
    """

    def __init__(self, veid: int, api_key: str, url: str = None):
        self.veid = veid
        self.api_key = api_key
        if url is None:
            self.url = 'https://api.64clouds.com/v1/'

    def _request(self, call, **kwargs):
        """
        Send request
        """
        kwargs["veid"] = self.veid
        kwargs["api_key"] = self.api_key
        return requests.post(urljoin(self.url, call), data=kwargs).json()

    def start(self):
        """
        Starts the VPS
        """
        return self._request("start")

    def stop(self):
        """
        Stops the VPS
        """
        return self._request("stop")

    def restart(self):
        """
        Reboots the VPS
        """
        return self._request("restart")

    def kill(self):
        """
        Allows to forcibly stop a VPS that is stuck and cannot be stopped by normal means.
        Please use this feature with great care as any unsaved data will be lost.
        """
        return self._request("kill")

    def get_service_info(self):
        """
        get vps info
        """
        return self._request("getServiceInfo")

    def get_live_service_info(self):
        """
        This function returns all data provided by getServiceInfo. In addition, it provides detailed status of the VPS.
        Please note that this call may take up to 15 seconds to complete.
        """
        return self._request("getLiveServiceInfo")

    def get_available_os(self):
        """
        Get a list of OSs that can be installed
        """
        return self._request('getAvailableOS')

    def reinstall_os(self, os: str):
        """
        Reinstall the Operating System. OS must be specified via "os" variable.
        Use getAvailableOS call to get list of available systems.
        """
        return self._request('reinstallOS', os=os)

    def reset_root_password(self):
        """
        Generates and sets a new root password.
        """
        return self._request("resetRootPassword")

    def get_usage_graphs(self):
        """
        Obsolete, use getRawUsageStats instead
        """
        return self._request("getUsageGraphs")

    def get_raw_usage_stats(self):
        """
        Returns a two-dimensional array with the detailed usage statistics shown under Detailed Statistics in KiwiVM.
        """
        return self._request("getRawUsageStats")

    def get_audit_log(self):
        """
        Returns an array with the detailed audit log shown under Audit Log in KiwiVM.
        """
        return self._request("getAuditLog")

    def set_hostname(self, new_hostname: str):
        """
        Sets new hostname.
        """
        return self._request("setHostname", newHostname=new_hostname)

    def set_ptr(self, ip: str, ptr: str):
        """
        Sets new PTR (rDNS) record for IP.
        """
        return self._request("setPTR", ip=ip, ptr=ptr)

    def iso_mount(self, iso: str):
        """
        Sets ISO image to boot from. VM must be completely shut down and restarted after this API call.
        """
        return self._request("iso/mount", iso=iso)

    def iso_unmount(self):
        """
        Removes ISO image and configures VM to boot from primary storage. VM must be completely shut down and restarted
        after this API call.
        """
        return self._request("iso/unmount")

    def basic_shell_cd(self, current_dir: str, new_dir: str):
        """
        Simulate change of directory inside of the VPS. Can be used to build a shell like Basic shell.
        """
        return self._request("basicShell/cd", currentDir=current_dir, newDir=new_dir)

    def basic_shell_exec(self, command: str):
        """
        Execute a shell command on the VPS (synchronously).
        """
        return self._request("basicShell/exec", command=command)

    def shell_script_exec(self, script: str):
        """
        Execute a shell script on the VPS (asynchronously).
        """
        return self._request("shellScript/exec", script=script)

    def snapshot_create(self, description: str = None):
        """
        Create snapshot
        """
        return self._request("snapshot/create", description=description)

    def snapshot_list(self):
        """
        Get list of snapshots.
        """
        return self._request("snapshot/list")

    def snapshot_delete(self, snapshot: str):
        """
        Delete snapshot by fileName (can be retrieved with snapshot/list call).
        """
        return self._request("snapshot/delete", snapshot=snapshot)

    def snapshot_restore(self, snapshot: str):
        """
        Restores snapshot by fileName (can be retrieved with snapshot/list call). This will overwrite all data on the VPS.
        """
        return self._request("snapshot/restore", snapshot=snapshot)

    def snapshot_toggle_sticky(self, snapshot: str, sticky: int):
        """
        Set or remove sticky attribute ("sticky" snapshots are never purged). Name of snapshot can be retrieved with
        snapshot/list call – look for fileName variable.
            Set sticky = 1 to set sticky attribute
            Set sticky = 0 to remove sticky attribute
        """
        return self._request("snapshot/toggleSticky", snapshot=snapshot, sticky=sticky)

    def snapshot_export(self, snapshot: str):
        """
        Generates a token with which the snapshot can be transferred to another instance.
        """
        return self._request('snapshot/export', snapshot=snapshot)

    def snapshot_import(self, veid: int, token: str):
        """
        Imports a snapshot from another instance identified by VEID and Token. Both VEID and Token must be obtained
        from another instance beforehand with a snapshot/export call.
        """
        return self._request("snapshot/import", sourceVeid=veid, sourceToken=token)

    def backup_list(self):
        """
        Get list of automatic backups.
        """
        return self._request("backup/list")

    def backup_copy_to_snapshot(self, backup_token: str):
        """
        Copies a backup identified by backup_token (returned by backup/list) into a restorable Snapshot.
        """
        return self._request("backup/copyToSnapshot", backup_token=backup_token)

    def migrate_get_locations(self):
        """
        Return all possible migration locations.
        """
        return self._request("migrate/getLocations")

    def migrate_start(self, location: str):
        """
        Start VPS migration to new location. Takes new location ID as input. Note that this will result in all IPv4
        addresses to be replaced with new ones, and all IPv6 addresses will be released.
        """
        return self._request("migrate/start", location=location)

    def get_suspension_details(self):
        """
        Retrieve information related to service suspensions.
        """
        return self._request("getSuspensionDetails")

    def unsuspend(self, record_id: str):
        """
        Clear abuse issue identified by record_id and unsuspend the VPS. Refer to getSuspensionDetails call for details.
        """
        return self._request("unsuspend", record_id=record_id)

    def get_rate_limit_status(self):
        """
        When you perform too many API calls in a short amount of time, KiwiVM API may start dropping your requests for
        a few minutes. This call allows monitoring this matter.
        """
        return self._request("getRateLimitStatus")

    def private_ip_get_available_ips(self):
        """
        Returns all available (free) IPv4 addresses which you can activate on VM
        """
        return self._request("privateIp/getAvailableIps")

    def private_ip_assign(self, ip: str = None):
        """
        Assign private IP address. If IP address not specified, a random address will be assigned.
        """
        return self._request("privateIp/assign", ip=ip)

    def private_ip_delete(self, ip: str):
        """
        Delete private IP address.
        """
        return self._request("privateIp/delete", ip=ip)
