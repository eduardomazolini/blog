import os
import re
import subprocess
import sys

# Dictionary of technical terms, proper nouns, and common abbreviations to ignore
IGNORED_WORDS = {
    # Tech terms
    'docker', 'nginx', 'proxmox', 'mikrotik', 'nautilus', 'kvm', 'debian', 'ubuntu', 'centos', 'fedora',
    'zabbix', 'zabbly', 'incus', 'jekyll', 'chirpy', 'markdown', 'github', 'git', 'api', 'saas', 'vps',
    'ssh', 'ssl', 'tls', 'https', 'http', 'ip', 'dns', 'dhcp', 'vlan', 'zenity', 'ffmpeg', 'bash', 'bashrc',
    'nmap', 'portainer', 'ollama', 'warp', 'cloudflare', 'cloud-init', 'systemd', 'systemctl', 'sudo',
    'apt', 'curl', 'wget', 'unzip', 'tar', 'gzip', 'zstd', 'lz4', 'xamp', 'blogger', 'liquid', 'yml',
    'yaml', 'json', 'html', 'css', 'js', 'php', 'sql', 'mysql', 'postgres', 'redis', 'mongodb', 'sqlite',
    'fop', 'voip', 'sip', 'asterisk', 'elastix', 'freepbx', 'vivo', 'vzdump', 'uefi', 'bios', 'grub',
    'luks', 'zswap', 'nfc', 'pix', 'cups', 'gpon', 'ont', 'olt', 'nat', 'cgnat', 'wan', 'lan', 'wi-fi',
    'wifi', 'wpa', 'wep', 'ubnt', 'ubiquiti', 'm5', 'uisp', 'ac', 'ap', 'sta', 'poe', 'pppoe', 'pptp',
    'vpn', 'ipsec', 'openvpn', 'wireguard', 'webfig', 'winbox', 'routeros', 'routerboard', 'rb', 'map',
    'hex', 'ccr', 'crs', 'capsman', 'l2tp', 'sstp', 'ospf', 'bgp', 'rip', 'snmp', 'syslog', 'raid',
    'broadcom', 'lsi', 'megacli', 'megaraid', 'storcli', 'sas', 'sata', 'ssd', 'hdd', 'nvme', 'pcie',
    'gpu', 'cpu', 'ram', 'rom', 'eeprom', 'lvm', 'cryptsetup', 'dm-crypt', 'fstab', 'initramfs',
    'nvidia', 'intel', 'amd', 'radeon', 'geforce', 'cuda', 'nouveau', 'mesa', 'vaapi', 'vdpau',
    'qemu', 'libvirt', 'virsh', 'virt-manager', 'spice', 'vnc', 'rdp', 'nfs', 'samba', 'smb', 'cifs',
    'webmin', 'cockpit', 'ajenti', 'webtools', 'zfs', 'btrfs', 'ext4', 'ext3', 'ext2', 'xfs', 'ntfs',
    'fat32', 'exfat', 'dd', 'rsync', 'cp', 'mv', 'rm', 'mkdir', 'rmdir', 'ls', 'cd', 'pwd', 'chmod',
    'chown', 'df', 'du', 'free', 'top', 'htop', 'btop', 'iotop', 'iftop', 'nethogs', 'ping', 'traceroute',
    'mtr', 'ip', 'ifconfig', 'route', 'netstat', 'ss', 'dig', 'nslookup', 'host', 'whois', 'screen',
    'tmux', 'nohup', 'disown', 'jobs', 'bg', 'fg', 'kill', 'pkill', 'killall', 'journalctl', 'dmesg',
    'uptime', 'uname', 'hostname', 'env', 'export', 'alias', 'unalias', 'history', 'clear', 'exit',
    'logout', 'reboot', 'poweroff', 'shutdown', 'init', 'runlevel', 'chkconfig', 'crontab', 'cron',
    'anacron', 'at', 'batch', 'sleep', 'usleep', 'watch', 'date', 'cal', 'bc', 'expr', 'eval', 'exec',
    'source', 'sh', 'zsh', 'ksh', 'csh', 'tcsh', 'fish', 'dash', 'ash', 'busybox', 'chsh', 'passwd',
    'useradd', 'userdel', 'usermod', 'groupadd', 'groupdel', 'groupmod', 'gpasswd', 'id', 'who', 'w',
    'last', 'lastlog', 'finger', 'write', 'wall', 'mesg', 'talk', 'mail', 'mutt', 'pine', 'alpine',
    'sendmail', 'postfix', 'exim', 'qmail', 'dovecot', 'courier', 'cyrus', 'imap', 'pop3', 'smtp',
    'httpd', 'apache', 'apache2', 'lighttpd', 'caddy', 'traefik', 'envoy', 'haproxy', 'squid',
    'privoxy', 'polipo', 'tor', 'i2p', 'freenet', 'gnunet', 'tox', 'ring', 'jami', 'linphone',
    'twinkle', 'ekiga', 'empathy', 'pidgin', 'kopete', 'psi', 'gajim', 'conversations', 'dino',
    'profanity', 'mcabber', 'centerim', 'weechat', 'irssi', 'bitchx', 'hexchat', 'xchat', 'mirc',
    'purple', 'telepathy', 'matrix', 'element', 'synapse', 'skype', 'twitter', 'discord', 'telegram',
    'whatsapp', 'facebook', 'instagram', 'signal', 'email', 'lrf', 'h264', 'hevc', 'hvec', 'dji',
    'djmd', 'dbgi', 'tmcd', 'multicam', 'gyroflow', 'nautilus', 'zenity', 'playstore', 'vlc',
    'gsettings', 'dconf', 'systemback', 'gparted', 'timeshift', 'flatpak', 'snap', 'appimage',
    'plank', 'conky', 'neofetch', 'fastfetch', 'glances', 'gdu', 'ncdu', 'fd', 'ripgrep', 'rg',
    'bat', 'fzf', 'zoxide', 'exa', 'lsd', 'starship', 'fish-shell', 'oh-my-zsh', 'powerlevel10k',
    'gnome', 'kde', 'xfce', 'mate', 'cinnamon', 'lxde', 'lxqt', 'i3', 'sway', 'wayland', 'x11',
    'xorg', 'pulseaudio', 'pipewire', 'alsa', 'jack', 'gstreamer', 'v4l2', 'obs-studio', 'kdenlive',
    'shotcut', 'audacity', 'gimp', 'inkscape', 'blender', 'darktable', 'rawtherapee', 'krita',
    'libreoffice', 'onlyoffice', 'wps-office', 'calibre', 'transmission', 'deluge', 'qbittorrent',
    'filezilla', 'remmina', 'anydesk', 'teamviewer', 'rustdesk', 'synergy', 'barrier', 'virtualbox',
    'vmware', 'hyper-v', 'xen', 'xcp-ng', 'proxmox-ve', 'pve', 'pbs', 'proxmox-backup-server',
    'truenas', 'freenas', 'openmediavault', 'synology', 'qnap', 'unraid', 'casaos', 'yunohost',
    'nextcloud', 'owncloud', 'seafile', 'pcloud', 'syncthing', 'resilio', 'rclone', 'duplicati',
    'restic', 'borgbackup', 'timeshift', 'backintime', 'luckybackup', 'rsnapshot', 'rdiff-backup',
    'duplicity', 'backuppc', 'amanda', 'bareos', 'urbackup', 'kopia', 'velero',
    # Proper nouns / brand names / names / acronyms
    'mazolini', 'emazolini', 'ludicando', 'google', 'microsoft', 'apple', 'amazon', 'netflix',
    'spotify', 'youtube', 'github', 'gitlab', 'bitbucket', 'gitea', 'forgejo', 'dockerhub',
    'pocket', 'osmo', 'dji', 'fop', 'elastix', 'freepbx', 'asterisk', 'vivo', 'claro', 'tim',
    'oi', 'gvt', 'copel', 'algar', 'sercomtel', 'brisanet', 'desktop', 'desktop-environment',
    'unifi', 'edgerouter', 'edgeswitch', 'toughswitch', 'airmax', 'airfiber', 'nanostation',
    'rocket', 'powerbeam', 'litebeam', 'bullet', 'omni', 'sector', 'grid', 'dish', 'loco',
    'ns5', 'nanostation5', 'locom5', 'm2', 'm3', 'm365', 'm900', 'bulletm5', 'rocketm5',
    'unifi-ap', 'uap', 'uap-ac-lite', 'uap-ac-lr', 'uap-ac-pro', 'uap-ac-m', 'uap-flexhd',
    'uap-nanohd', 'uap-iw-hd', 'uap-xg', 'uap-shd', 'usg', 'udm', 'udm-pro', 'uxg-pro',
    'usw', 'usw-flex', 'usw-lite', 'usw-pro', 'usw-enterprise', 'unifi-controller', 'network-application',
    'protect', 'talk', 'access', 'uid', 'connect', 'led', 'smartpower', 'unifi-lte', 'unifi-building-bridge',
    # Portuguese contractions or informal spellings commonly used
    'pra', 'pro', 'pras', 'pros', 'ta', 'to', 'do', 'tas', 'tos', 'tava', 'tavam', 'vc', 'vcs', 'tb', 'tbm',
    'pq', 'pqp', 'kd', 'blz', 'vlw', 'flw', 'gostaria', 'recomendo', 'pessoal', 'deste', 'desta',
    'comigo', 'consigo', 'com', 'sem', 'sob', 'sobre', 'sobrefirewall', 'sub', 'super', 'hyper',
    'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'yotta', 'milli', 'micro', 'nano', 'pico',
    'femto', 'atto', 'zepto', 'yocto', 'kilo', 'hecto', 'deca', 'deci', 'centi', 'mili',
    # Others
    'blogger', 'blogger-style', 'blogger2jekyll', 'jekyll-import', 'disqus', 'giscus', 'utterances',
    'google-analytics', 'ga4', 'clarity', 'hotjar', 'mixpanel', 'amplitude', 'matomo', 'piwik',
    'fathom', 'plausible', 'umami', 'goatcounter', 'simple-analytics', 'shynet', 'ackee', 'counter',
    'clicky', 'statcounter', 'histats', 'awstats', 'webalizer', 'goaccess', 'analog', 'logstalgia',
    'gource', 'gitstats', 'cloc', 'scc', 'tokei', 'sloccount', 'sloc', 'loc', 'lines-of-code'
}

# Portuguese letters regex
WORD_RE = re.compile(r'\b[a-zA-ZáéíóúçãõâêôàíüÁÉÍÓÚÇÃÕÂÊÔÀÍÜªº-]+\b')

def clean_markdown(content):
    # 1. Remove YAML front matter
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 3:
        body = parts[2]
    else:
        body = content

    # 2. Remove code blocks (``` ... ```)
    body = re.sub(r'```.*?```', '', body, flags=re.DOTALL)

    # 3. Remove inline code (`...`)
    body = re.sub(r'`[^`\n]+`', '', body)

    # 4. Remove Markdown links like [text](url) but keep "text"
    body = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', body)

    # 5. Remove automatic links <http...>
    body = re.sub(r'<https?://[^>]+>', '', body)

    # 6. Remove Jekyll directive / block formatting like {: .prompt-tip }
    body = re.sub(r'\{:\s*\.[^\}]+\s*\}', '', body)

    # 7. Remove HTML tags like <br>, <img>
    body = re.sub(r'<[^>]+>', '', body)

    return body

def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    cleaned_body = clean_markdown(content)
    lines = cleaned_body.splitlines()
    
    errors = []
    
    for idx, line in enumerate(lines, start=1):
        # Find all words in the line
        words = WORD_RE.findall(line)
        for word in words:
            # Skip words with numbers (e.g., v3, x86_64 handled by boundary check but good to be safe)
            if any(char.isdigit() for char in word):
                continue
            
            # Skip short words, acronyms, or ignored words
            word_lower = word.lower()
            if len(word) <= 2 or word_lower in IGNORED_WORDS:
                continue
            
            # Use aspell to check if it's correct in Portuguese
            p = subprocess.Popen(['aspell', 'list', '-l', 'pt_BR'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out, err = p.communicate(input=word)
            
            # If the output is not empty, aspell reported this word as misspelled
            if out.strip():
                # Double-check: does it contain hyphen? If yes, check parts individually
                if '-' in word:
                    parts = word.split('-')
                    parts_ok = True
                    for part in parts:
                        if len(part) <= 2 or part.lower() in IGNORED_WORDS:
                            continue
                        p2 = subprocess.Popen(['aspell', 'list', '-l', 'pt_BR'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        out2, _ = p2.communicate(input=part)
                        if out2.strip():
                            parts_ok = False
                            break
                    if parts_ok:
                        continue
                
                errors.append((idx, word, line.strip()))
                
    return errors

def main():
    posts_dir = '/home/emazolini/Documentos/projetos/github/blog/_posts'
    if not os.path.isdir(posts_dir):
        print(f"Directory {posts_dir} not found.")
        sys.exit(1)
        
    all_files = [os.path.join(posts_dir, f) for f in os.listdir(posts_dir) if f.endswith('.md')]
    all_files.sort(reverse=True) # Check newest files first
    
    total_errors = 0
    print(f"Scanning {len(all_files)} files in {posts_dir}...")
    
    for fpath in all_files:
        errors = check_file(fpath)
        if errors:
            print(f"\nFile: {fpath}")
            for line_no, word, line_text in errors:
                print(f"  Line {line_no}: '{word}' -> Context: \"{line_text}\"")
                total_errors += 1
                
    print(f"\nScan complete. Total potential spelling errors: {total_errors}")

if __name__ == "__main__":
    main()
