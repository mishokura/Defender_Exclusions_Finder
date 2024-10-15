This is a python script which enumerates dictionaries with variable root directory and depth to MpCmdRun.exe in order to find out if any of them is added to Defender Exclusions, all this without admin privileges.
It uses default windows MpCmdRun.exe to catch command output "skipped", which is only printed if supplied directory name has invalid filename charecter followed by * and is in Defender exceptions.
Initially discovered by: https://blog.fndsec.net/2024/10/04/uncovering-exclusion-paths-in-microsoft-defender-a-security-research-insight/
