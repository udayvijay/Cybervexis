import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const levels = {
  1: {
    name: "Cyber Threats",
    topics: [
      "Weak Password Attack",
      "Phishing Attack",
      "Malware Infection",
      "Unsafe Public WiFi",
      "Data Leak"
    ]
  },
  2: {
    name: "Firewall Security",
    topics: [
      "Packet Filtering Firewall",
      "Stateful Inspection Firewall",
      "Proxy Firewall",
      "Cloud Firewall",
      "Software Firewall"
    ]
  },
  3: {
    name: "SOC (Security Operations Center)",
    topics: [
      "In-House SOC",
      "Managed SOC",
      "Hybrid SOC",
      "Co-Managed SOC",
      "Virtual SOC (vSOC)"
    ]
  },
  4: {
    name: "Zero Trust Architecture",
    topics: [
      "Identity-Based Architecture",
      "Device-Based Architecture",
      "Network-Based Architecture",
      "Data-Centric Architecture",
      "Infrastructure-Based Architecture"
    ]
  },
  5: {
    name: "Cyber Resilience",
    topics: [
      "Preventive Resilience",
      "Detective Resilience",
      "Responsive Resilience",
      "Recovery Resilience",
      "Adaptive/Evolving Resilience"
    ]
  }
};

const templates = {
  // Level 1
  "Weak Password Attack": [
    { q: "An attacker uses a list of common phrases and words to guess a user's password. What is this technique?", a: "Dictionary Attack", o: ["Brute Force Attack", "Rainbow Table Attack", "Phishing Attack"] },
    { q: "What security mechanism directly mitigates the risk of weak password cracking?", a: "Multi-Factor Authentication (MFA)", o: ["Data Encryption", "Single Sign-On (SSO)", "Virtual Private Network (VPN)"] },
    { q: "Which password hashing algorithm is designed specifically to prevent brute-force speed attacks?", a: "bcrypt", o: ["MD5", "SHA-1", "DES"] },
    { q: "If an attacker tests all possible character combinations systematically, they are performing which type of attack?", a: "Brute Force Attack", o: ["Dictionary Attack", "SQL Injection", "Man-in-the-Middle Attack"] },
    { q: "What is a major risk associated with using the same password across multiple corporate accounts?", a: "Credential Stuffing", o: ["Social Engineering", "IP Spoofing", "DNS Poisoning"] }
  ],
  "Phishing Attack": [
    { q: "A highly targeted phishing campaign directed at a high-level executive is called what?", a: "Whaling", o: ["Smishing", "Vishing", "Spear Phishing"] },
    { q: "What type of phishing attack relies on sending malicious SMS or text messages?", a: "Smishing", o: ["Vishing", "Spear Phishing", "Clone Phishing"] },
    { q: "An attacker compromises a domain name system to redirect users to a malicious site even when they type the correct URL. This is:", a: "Pharming", o: ["Spear Phishing", "Whaling", "Watering Hole Attack"] },
    { q: "What is the primary indicator of a phishing email when inspecting the header?", a: "Mismatched Sender Address and SPF/DKIM failures", o: ["Presence of attachments", "HTML formatting", "High priority flag"] },
    { q: "Which protocol helps email receivers verify if an email actually came from the claimed domain sender?", a: "DMARC", o: ["HTTPS", "SFTP", "DHCP"] }
  ],
  "Malware Infection": [
    { q: "What type of malware encrypts files and demands payment in exchange for a decryption key?", a: "Ransomware", o: ["Spyware", "Adware", "Trojan Horse"] },
    { q: "Which type of malware can self-replicate and spread across a network without any human interaction?", a: "Worm", o: ["Virus", "Trojan Horse", "Rootkit"] },
    { q: "What malware component hides deep inside the operating system to maintain administrator access?", a: "Rootkit", o: ["Ransomware", "Keylogger", "Adware"] },
    { q: "A piece of malware that disguises itself as legitimate software is known as what?", a: "Trojan Horse", o: ["Worm", "Spyware", "Logic Bomb"] },
    { q: "What is the best way to detect zero-day malware that has no known signature?", a: "Heuristic and Behavioral Analysis", o: ["Signature-based scanning", "Defragmentation", "Ping sweep"] }
  ],
  "Unsafe Public WiFi": [
    { q: "What type of attack involves an attacker setting up a rogue access point with the same name as a legitimate public network?", a: "Evil Twin Attack", o: ["Man-in-the-Middle", "ARP Spoofing", "MAC Flooding"] },
    { q: "Which security tool encrypts all data sent from a laptop over an open public network?", a: "Virtual Private Network (VPN)", o: ["Local Firewall", "Antivirus Scanner", "Proxy Server"] },
    { q: "What attack occurs when a hacker intercepts communication between a client and server on a public network?", a: "Man-in-the-Middle (MitM) Attack", o: ["Denial of Service", "SQL Injection", "Buffer Overflow"] },
    { q: "Why is accessing HTTP sites on public WiFi extremely risky?", a: "Data is transmitted in plain text and can be sniffed easily", o: ["It causes IP address conflicts", "It slows down the network speed", "It automatically downloads viruses"] },
    { q: "Which protocol provides mutual authentication and cryptographic keys on modern secure WiFi?", a: "WPA3", o: ["WEP", "WPA1", "TKIP"] }
  ],
  "Data Leak": [
    { q: "What is the term for the unauthorized transmission of sensitive data from inside an organization to an external recipient?", a: "Data Exfiltration", o: ["Data Encryption", "Data Ingestion", "Data Partitioning"] },
    { q: "Which technology is specifically designed to scan outgoing traffic and block sensitive records (like credit cards) from leaving?", a: "DLP (Data Loss Prevention)", o: ["IPS (Intrusion Prevention System)", "WAF (Web Application Firewall)", "SIEM"] },
    { q: "What is a common cause of accidental cloud data leaks?", a: "Misconfigured S3 bucket permissions", o: ["DDoS attack on the data center", "Expired SSL certificates", "SQL injection on frontend"] },
    { q: "When sensitive files are leaked online because of an insider threat, this is classified as a:", a: "Data Leakage", o: ["Phishing Scam", "Cross-Site Scripting", "Privilege Escalation"] },
    { q: "Which compliance standard regulates the protection of personal data of EU citizens?", a: "GDPR", o: ["PCI-DSS", "HIPAA", "SOX"] }
  ],

  // Level 2
  "Packet Filtering Firewall": [
    { q: "At which layer of the OSI model does a traditional packet filtering firewall primarily operate?", a: "Network/Transport Layer (Layers 3 & 4)", o: ["Application Layer (Layer 7)", "Data Link Layer (Layer 2)", "Physical Layer (Layer 1)"] },
    { q: "What criteria does a packet filtering firewall use to evaluate traffic?", a: "Source/Destination IP addresses and Ports", o: ["HTTP payload content", "User login credentials", "Stateful TCP handshake tracking"] },
    { q: "Which of the following is a limitation of packet filtering firewalls?", a: "They are vulnerable to IP spoofing and cannot inspect payload content", o: ["They are extremely slow", "They require high memory resources", "They only block incoming traffic"] },
    { q: "What is the default action of a securely configured firewall's ACL?", a: "Implicit Deny All", o: ["Permit All", "Log and Forward", "Redirect to Sandbox"] },
    { q: "What table does a packet filtering firewall check to match rules?", a: "Access Control List (ACL)", o: ["NAT Translation Table", "ARP Table", "Routing Table"] }
  ],
  "Stateful Inspection Firewall": [
    { q: "What key characteristic distinguishes stateful firewalls from simple packet filters?", a: "Tracking the state of active network connections in a state table", o: ["Inspecting the full application-layer payload", "Checking user identity credentials", "Filtering by file extension"] },
    { q: "Which network packet is analyzed by a stateful firewall to create a new session entry?", a: "TCP SYN", o: ["TCP ACK", "TCP FIN", "ICMP Echo Request"] },
    { q: "What happens to packets that match an established session in a stateful firewall's state table?", a: "They are automatically allowed without re-checking full ACL rules", o: ["They are sent to the proxy server", "They are dropped immediately", "They undergo deep packet inspection"] },
    { q: "Which TCP handshake flag indicates the completion of session setup in state tables?", a: "ACK", o: ["SYN", "RST", "URG"] },
    { q: "What memory-resident structure does a stateful firewall use to store connection states?", a: "State Table", o: ["Active Directory Directory", "ARP Cache", "Routing Log"] }
  ],
  "Proxy Firewall": [
    { q: "A proxy firewall (application-level gateway) operates at which layer of the OSI model?", a: "Application Layer (Layer 7)", o: ["Network Layer (Layer 3)", "Transport Layer (Layer 4)", "Data Link Layer (Layer 2)"] },
    { q: "How does a proxy firewall handle client connections to an external server?", a: "It terminates the client connection and establishes a new one to the server", o: ["It forwards the packets directly at the network layer", "It encrypts the payload using TLS", "It logs the IP address but does not modify the packet"] },
    { q: "What is the primary security benefit of using a proxy firewall?", a: "Complete shielding of internal IP addresses and deep application payload inspection", o: ["Lowest latency network throughput", "Simplest rule configuration", "Compatibility with all protocols automatically"] },
    { q: "Which proxy type inspects outbound web traffic and filters URL categories?", a: "Forward Proxy", o: ["Reverse Proxy", "Transparent Proxy", "Stateful Proxy"] },
    { q: "What is the name of a proxy server that doesn't require any client configuration?", a: "Transparent Proxy", o: ["Reverse Proxy", "Explicit Proxy", "Anonymizing Proxy"] }
  ],
  "Cloud Firewall": [
    { q: "What is another common name for a Cloud Firewall that is provided as a subscription service?", a: "Firewall as a Service (FWaaS)", o: ["Infrastructure as a Service (IaaS)", "Software as a Service (SaaS)", "Network as a Service (NaaS)"] },
    { q: "What is a key benefit of cloud firewalls compared to traditional hardware firewalls?", a: "Dynamic scalability and centralized management across multi-region resources", o: ["No need for access control rules", "Zero latency network traversal", "Bypassing DNS checks"] },
    { q: "In cloud architectures, security groups differ from network ACLs because security groups are:", a: "Stateful and operate at the instance level", o: ["Stateless and operate at the subnet level", "Hardware-based rather than software", "Only applicable to database storage"] },
    { q: "Which cloud security model relies on firewalls integrated directly inside SaaS/PaaS backends?", a: "Shared Responsibility Model", o: ["Zero Trust Network Access (ZTNA)", "Security Service Edge (SSE)", "Distributed Edge Routing"] },
    { q: "Cloud-native firewalls can automatically tag and apply rules based on what resource attributes?", a: "Metadata tags and resource labels", o: ["MAC addresses of physical servers", "Physical rack slot numbers", "Power consumption profiles"] }
  ],
  "Software Firewall": [
    { q: "Where does a software firewall typically run?", a: "On a local host or client computer's operating system", o: ["On a dedicated physical server rack at the network boundary", "Inside the core network router", "Inside the DNS server"] },
    { q: "What is the primary role of a host-based (software) firewall?", a: "Protecting a single host from unauthorized access and rogue local processes", o: ["Filtering internet traffic for an entire enterprise", "Generating SSL certificates", "Caching DNS records"] },
    { q: "Which software firewall is built into modern Windows operating systems by default?", a: "Windows Defender Firewall", o: ["iptables", "pfSense", "ZoneAlarm"] },
    { q: "In Linux systems, what command-line tool is commonly used to configure the built-in netfilter firewall?", a: "iptables / ufw", o: ["systemctl", "ssh-keygen", "netstat"] },
    { q: "What risk does a software firewall run if the host operating system gets fully compromised by root malware?", a: "The malware can disable or bypass the firewall rules entirely", o: ["The firewall will overheat the CPU", "The network adapter will disconnect", "The files will be automatically decrypted"] }
  ],

  // Level 3
  "In-House SOC": [
    { q: "What is a primary advantage of operating a fully In-House Security Operations Center (SOC)?", a: "Deep understanding of the organization's unique network and assets", o: ["Lower cost than outsourcing", "Zero staff turnover rate", "No requirement for specialized security tools"] },
    { q: "What is the biggest operational challenge of an In-House SOC?", a: "High cost of skilled cybersecurity personnel and 24/7 coverage", o: ["Difficulty communicating with executives", "Lack of hardware availability", "Managing cloud firewall configurations"] },
    { q: "What is the core system used by an In-House SOC to aggregate and analyze log events?", a: "SIEM (Security Information and Event Management)", o: ["DNS Resolver", "DHCP Server", "Active Directory Server"] },
    { q: "In an in-house SOC, who is responsible for writing custom detection rules and alerts?", a: "Security Analysts and Engineers", o: ["System Administrators", "Chief Financial Officer", "External Service Provider"] },
    { q: "What tier of SOC analyst is responsible for deep threat hunting and advanced incident investigation?", a: "Tier 3 Analyst", o: ["Tier 1 Analyst", "Tier 2 Analyst", "SOC Manager"] }
  ],
  "Managed SOC": [
    { q: "What is a Managed SOC service also commonly known as?", a: "MSSP (Managed Security Service Provider)", o: ["SaaS (Software as a Service)", "ISP (Internet Service Provider)", "IaaS (Infrastructure as a Service)"] },
    { q: "Why do smaller enterprises often choose a Managed SOC over an In-House SOC?", a: "Lower capital expenditure and immediate 24/7 expert monitoring", o: ["Complete transfer of legal liability for data breaches", "Managed SOC does not need local log collection", "Automatic remediation of all endpoint bugs"] },
    { q: "What is a potential disadvantage of using a fully Managed SOC?", a: "Lack of deep context regarding internal business processes and custom apps", o: ["MSSPs cannot detect malware", "MSSPs require hardware installation", "Higher network latency"] },
    { q: "What document defines the metrics, response times, and uptime expectations between a company and MSSP?", a: "SLA (Service Level Agreement)", o: ["NDA (Non-Disclosure Agreement)", "SOC 2 Report", "MOU (Memorandum of Understanding)"] },
    { q: "How does a Managed SOC usually collect security event data from a client's network?", a: "By deploying local log forwarders or collectors that upload to the MSSP SIEM", o: ["By routing all network traffic through the MSSP offices", "By sending analysts to the client site weekly", "By running monthly ping sweeps"] }
  ],
  "Hybrid SOC": [
    { q: "What describes a Hybrid SOC model?", a: "In-house analysts work alongside an outsourced MSSP partner", o: ["A SOC that manages both physical and virtual machines", "A SOC using both Linux and Windows servers", "A SOC monitoring both IT and OT networks"] },
    { q: "In a Hybrid SOC, which tier of alerts is typically outsourced to the MSSP?", a: "Tier 1 (Initial triage and basic alert filtering)", o: ["Tier 3 (Threat hunting and forensic investigation)", "Executive level incident response", "Custom automation scripts development"] },
    { q: "What is a key benefit of the Hybrid SOC model?", a: "Relieving local staff of alert fatigue while retaining control over critical response", o: ["It is the cheapest option available", "It eliminates the need for a SIEM tool", "It guarantees 100% security"] },
    { q: "How is responsibility shared in a Hybrid SOC during a high-severity incident?", a: "MSSP detects and flags the threat; in-house team executes the final containment action", o: ["MSSP takes full control of the network; in-house team goes offline", "MSSP contacts the police; in-house team shuts down servers", "Only the in-house team does investigation"] },
    { q: "What technology helps Hybrid SOC teams share ticket data and automate collaborative workflows?", a: "SOAR (Security Orchestration, Automation, and Response)", o: ["Active Directory", "Dynamic DNS", "Local Host file"] }
  ],
  "Co-Managed SOC": [
    { q: "What is the defining characteristic of a Co-Managed SOC?", a: "Shared access to a single SIEM platform and toolset by both client and provider", o: ["Two competitive MSSPs monitoring the same network", "A SOC managed by two different departments internally", "A SOC that only works during business hours"] },
    { q: "How does Co-Managed SOC differ from traditional Managed SOC?", a: "The client retains full visibility and ownership of security data and platforms", o: ["Co-managed SOC is twice as expensive", "Co-managed SOC does not use analysts", "Co-managed SOC relies purely on AI"] },
    { q: "Which tool configuration is shared directly in a co-managed SOC setup?", a: "SIEM dashboard, rules, and incident tickets", o: ["Client payroll systems", "Local active directory credentials only", "Firewall hardware cables"] },
    { q: "What is a main benefit of Co-Managed SOC for growing IT teams?", a: "They can scale operations quickly using provider resources while training internal staff", o: ["No need to pay licensing fees for security tools", "Complete automation of firewall rules", "Reduction in internet subscription costs"] },
    { q: "In a co-managed model, what ensures tasks don't overlap between the two teams?", a: "A detailed RACI matrix (Responsible, Accountable, Consulted, Informed)", o: ["Writing rules in different coding languages", "Running servers in different timezones", "Separating local and cloud traffic logs"] }
  ],
  "Virtual SOC (vSOC)": [
    { q: "What defines a Virtual SOC (vSOC)?", a: "A decentralized team of security experts operating remotely without a physical facility", o: ["A SOC that only monitors virtual machines", "An AI-powered automated security bot", "A simulation tool used to train junior analysts"] },
    { q: "What is a primary driver for choosing a Virtual SOC?", a: "Cost savings from not maintaining physical office space and access to global talent", o: ["Inability to run hardware firewalls", "Compliance requirements demanding virtual teams", "Lower latency internet connections"] },
    { q: "How do Virtual SOC members securely access client monitoring dashboards?", a: "Through secure VPNs, MFA, and virtual desktop environments (VDI)", o: ["Via public web servers with basic passwords", "Through physical fiber optic lines connected to each home", "By disabling local firewalls"] },
    { q: "What communication tools are essential for a Virtual SOC's real-time incident coordination?", a: "Secure chat channels, video conferencing, and integrated ticketing systems", o: ["FTP servers and fax machines", "Standard cellular text messaging", "Local radio frequencies"] },
    { q: "Which security standard verifies that a Virtual SOC operates with appropriate data controls?", a: "SOC 2 Type II", o: ["IPv6 Standard", "OWASP Top 10", "IEEE 802.11"] }
  ],

  // Level 4
  "Identity-Based Architecture": [
    { q: "What is the fundamental principle of Identity-Based Zero Trust Architecture?", a: "Identity is the new primary security perimeter; access is granted per user verification", o: ["Ip addresses define trust levels", "Only internal devices can access resources", "Access is open once connected to local LAN"] },
    { q: "Which standard authentication protocol is widely used for identity federation in ZTA?", a: "SAML 2.0 / OIDC", o: ["FTP", "Telnet", "WEP"] },
    { q: "What technology evaluates user identity, context (like location/time), and behavior dynamically?", a: "Risk-Based Adaptive Authentication", o: ["Static Firewalls", "Signature-based Antivirus", "DNSSEC"] },
    { q: "What role does IAM (Identity and Access Management) play in ZTA?", a: "It acts as the single source of truth for user identities, roles, and permissions", o: ["It routes network packets", "It scans servers for open ports", "It backs up database tables"] },
    { q: "What ZTA concept grants users only the minimum access level necessary to perform their job?", a: "Least Privilege Access", o: ["Role Escalation", "Single Sign-On", "Implicit Trust"] }
  ],
  "Device-Based Architecture": [
    { q: "What is the main objective of Device-Based ZTA?", a: "Ensuring only authorized, compliant, and healthy devices can access resources", o: ["Blocking all mobile devices", "Configuring virtual machines with public IPs", "Verifying the user's biometric traits only"] },
    { q: "What agent is installed on endpoints to monitor health, patch status, and compliance for Device ZTA?", a: "EDR (Endpoint Detection and Response) / MDM", o: ["WAF", "Proxy Server", "Log Forwarder"] },
    { q: "If a device lacks the latest security patch, what should a Device-Based ZTA system do?", a: "Quarantine the device or limit its access to remediation networks", o: ["Ignore the status and allow connection", "Shut down the target server", "Delete the user's credentials"] },
    { q: "What process verifies that a device attempting to connect has not been altered or compromised?", a: "Device Attestation", o: ["Device Defragmentation", "Device Provisioning", "Device Encryption"] },
    { q: "What unique cryptographic identifier is embedded in hardware to verify device identity?", a: "TPM (Trusted Platform Module) chip", o: ["MAC Address", "IP Address", "SSID"] }
  ],
  "Network-Based Architecture": [
    { q: "How does Network-Based ZTA prevent lateral movement of attackers within a corporate network?", a: "Micro-segmentation of networks into isolated zones", o: ["Using a single flat network architecture", "Deploying high-speed network switches", "Disabling local WiFi networks"] },
    { q: "What technology replaces legacy client-to-gateway VPNs in a Zero Trust network?", a: "ZTNA (Zero Trust Network Access)", o: ["PPTP VPN", "L2TP VPN", "GRE Tunnels"] },
    { q: "Under ZTA, what is the default assumption for any traffic inside the corporate intranet?", a: "The traffic is untrusted and must be authenticated and encrypted", o: ["The traffic is trusted because it is behind the perimeter", "The traffic is malicious and must be dropped", "The traffic is high priority"] },
    { q: "What security component acts as the Policy Decision Point (PDP) in a Zero Trust network?", a: "Policy Engine / Controller", o: ["Network Gateway", "Active Directory Server", "Intrusion Detection sensor"] },
    { q: "What is the role of the Policy Enforcement Point (PEP) in network ZTA?", a: "It intercepts connection requests and enforces decisions made by the PDP", o: ["It generates encryption keys", "It shuffles question databases", "It audits log files"] }
  ],
  "Data-Centric Architecture": [
    { q: "What is the primary focus of Data-Centric ZTA?", a: "Securing the data itself, regardless of where it resides or travels", o: ["Securing the physical database server cabinet", "Filtering network packet IP headers", "Monitoring user mouse movements"] },
    { q: "Which technique categorizes files based on sensitivity (e.g., Confidential, Public)?", a: "Data Classification", o: ["Data Masking", "Data Partitioning", "Data Normalization"] },
    { q: "What technology enforces access policies directly inside the data object or file?", a: "IRM (Information Rights Management)", o: ["WAF", "DLP", "SSL Certificate"] },
    { q: "Why is ubiquitous data encryption at rest and in transit critical for ZTA?", a: "To ensure data remains unreadable even if the storage or network is compromised", o: ["To speed up file transfer times", "To compress file sizes", "To satisfy ISP protocols"] },
    { q: "What process replaces sensitive data elements with non-sensitive equivalents (tokens) before use?", a: "Tokenization", o: ["Hashing", "Salting", "Serialization"] }
  ],
  "Infrastructure-Based Architecture": [
    { q: "What does Infrastructure ZTA secure?", a: "Cloud resources, container workloads, virtual machines, and development pipelines", o: ["The office building's electricity grid", "Physical desks and mousepads", "Only database records"] },
    { q: "What concept ensures that infrastructure configurations are defined via code and audited?", a: "Infrastructure as Code (IaC) Security", o: ["Manual provisioning", "Virtual Desktop Infrastructure", "Shadow IT"] },
    { q: "How are workloads securely authenticated to each other in microservice infrastructures?", a: "Using mutual TLS (mTLS) and dynamic service identities", o: ["Using static passwords in text files", "By trusting the local docker bridge IP", "Using public API keys"] },
    { q: "What tool manages secrets, certificates, and API keys dynamically in ZTA infrastructure?", a: "Secrets Manager (e.g., HashiCorp Vault)", o: ["GitHub Repository", "Local text file", "Express Server database.json"] },
    { q: "What is the security risk of 'Shadow IT' in infrastructure ZTA?", a: "Unmanaged cloud instances that bypass corporate security policies and audits", o: ["Excessive hosting fees from providers", "Slow website loading times", "Duplicate codebase files"] }
  ],

  // Level 5
  "Preventive Resilience": [
    { q: "What is the main goal of Preventive Resilience?", a: "Reducing the attack surface to block threats before they can cause damage", o: ["Recovering systems from backups", "Detecting unauthorized database reads", "Rewriting system codes after a patch"] },
    { q: "Which activity helps identify security gaps in code and configuration before deployment?", a: "Penetration Testing and Vulnerability Scanning", o: ["Network Traffic Monitoring", "Log Analysis", "Disaster Recovery Drill"] },
    { q: "What process ensures software is regularly updated to eliminate known security flaws?", a: "Patch Management", o: ["System Defragmentation", "Database Indexing", "Backup Rotation"] },
    { q: "How does security awareness training contribute to preventive resilience?", a: "It trains employees to recognize and avoid social engineering and phishing", o: ["It teaches users how to write firewall rules", "It automates account provisioning", "It replaces the need for antivirus"] },
    { q: "What boundary security system blocks unauthorized web traffic based on signatures and behavior?", a: "Web Application Firewall (WAF)", o: ["Intrusion Detection System (IDS)", "SIEM", "Reverse Proxy"] }
  ],
  "Detective Resilience": [
    { q: "What is the primary objective of Detective Resilience?", a: "Identifying security incidents and anomalies as quickly as possible", o: ["Encrypting user file directories", "Resetting user passwords", "Restoring virtual machines"] },
    { q: "What system aggregates logs from endpoints, networks, and clouds to trigger security alerts?", a: "SIEM (Security Information and Event Management)", o: ["DHCP Server", "Active Directory", "FTP Server"] },
    { q: "What detective tool monitors endpoint behavior for indicators of compromise?", a: "EDR (Endpoint Detection and Response)", o: ["WAF", "Vulnerability Scanner", "DLP"] },
    { q: "What is the term for a decoy system designed to lure attackers and detect unauthorized activity?", a: "Honeypot", o: ["Sandbox", "Proxy", "Firewall"] },
    { q: "What is a key metric used to evaluate detective resilience efficiency?", a: "MTTD (Mean Time to Detect)", o: ["MTTR (Mean Time to Repair)", "RTO (Recovery Time Objective)", "SLA Uptime"] }
  ],
  "Responsive Resilience": [
    { q: "What is the first step in the Incident Response Lifecycle after an incident is detected?", a: "Containment, Eradication, and Recovery", o: ["Writing the final incident report", "Paying the ransom", "Resetting all domain servers"] },
    { q: "What plan outlines roles, communication channels, and procedures during a cyber attack?", a: "Incident Response Plan (IRP)", o: ["Disaster Recovery Plan (DRP)", "Service Level Agreement (SLA)", "Employee Handbook"] },
    { q: "What security tool automates response actions like blocking IPs or isolating endpoints?", a: "SOAR (Security Orchestration, Automation, and Response)", o: ["SIEM", "Nmap", "Wireshark"] },
    { q: "What is the main goal of containment during a ransomware outbreak?", a: "Isolating infected systems to prevent malware from spreading laterally", o: ["Decrypting user files immediately", "Calling the software vendor", "Deleting the backup server data"] },
    { q: "What team is responsible for managing the technical aspects of a cyber incident?", a: "CSIRT (Computer Security Incident Response Team)", o: ["DevOps Team", "SOC Tier 1 exclusively", "Helpdesk Team"] }
  ],
  "Recovery Resilience": [
    { q: "What recovery objective defines the maximum tolerable period of data loss?", a: "RPO (Recovery Point Objective)", o: ["RTO (Recovery Time Objective)", "MTTR (Mean Time to Recovery)", "SLA"] },
    { q: "What recovery objective defines the maximum duration allowed to restore systems?", a: "RTO (Recovery Time Objective)", o: ["RPO (Recovery Point Objective)", "MTTD (Mean Time to Detect)", "KPI"] },
    { q: "Why is maintaining offline or immutable backups critical for ransomware recovery?", a: "It prevents the ransomware from encrypting or deleting the backup files", o: ["It reduces local storage space cost", "It speeds up daily incremental backups", "It automatically registers DNS hosts"] },
    { q: "What process verifies that backups can actually be used to restore operations successfully?", a: "Disaster Recovery (DR) Testing / Drills", o: ["Vulnerability Scanning", "Code Review", "Patching"] },
    { q: "What recovery strategy runs identical redundant services in parallel for zero-downtime failover?", a: "Active-Active Hot Standby", o: ["Cold Site Recovery", "Active-Passive Warm Site", "Local File Copying"] }
  ],
  "Adaptive/Evolving Resilience": [
    { q: "What is the main characteristic of Adaptive Resilience?", a: "Learning from past incidents and threat intelligence to strengthen future security", o: ["Restoring servers from static templates", "Blocking all external emails", "Conducting manual audits quarterly"] },
    { q: "What is the purpose of a Post-Incident Review (PIR)?", a: "Analyzing what went wrong and identifying lessons learned to improve plans", o: ["Assigning blame to individual employees", "Reporting the incident to local police", "Updating the payroll system"] },
    { q: "What is the process of proactively searching for hidden threats that bypassed active controls?", a: "Threat Hunting", o: ["Vulnerability Scanning", "Log Aggregation", "Packet Filtering"] },
    { q: "How does cyber threat intelligence (CTI) improve adaptive resilience?", a: "By providing indicators and tactics of active threat groups to update defenses", o: ["By automating password resets", "By bypassing firewall inspections", "By encrypting database backups"] },
    { q: "What exercises simulate real cyber attacks to test organizational readiness and adaptability?", a: "Red Teaming and Tabletop Exercises", o: ["Ping sweep tests", "Employee training slideshows", "Backup verification tasks"] }
  ]
};

// Generate additional questions programmatically to reach 21 questions per topic
const generateAllQuestions = () => {
  const allQuestions = [];
  let idCounter = 1;

  for (const levelStr of Object.keys(levels)) {
    const levelId = parseInt(levelStr);
    const { topics } = levels[levelId];

    for (const topic of topics) {
      const baseQs = templates[topic] || [];
      
      // Add base questions
      baseQs.forEach((base, idx) => {
        // Shuffle options to ensure they are clean
        const options = [base.a, ...base.o];
        
        allQuestions.push({
          id: `q_${idCounter++}`,
          level: levelId,
          topic: topic,
          question: base.q,
          options: options,
          answer: base.a
        });
      });

      // Generate remaining questions to hit 21 total per topic
      const templatesNeeded = 21 - baseQs.length;
      
      // Scenario generators
      const scenarios = [
        "A senior security analyst at a healthcare firm detects [Indicator]. This is a hallmark of an ongoing [Topic]. What should be the immediate response?",
        "During an external audit, an infrastructure team discovers a vulnerability related to [Topic]: '[Indicator]'. What is the best remediation?",
        "A cybersecurity training module presents a case study where an attacker leveraged [Indicator] to execute a [Topic]. How is this classified?",
        "To satisfy industry compliance standards, a security engineer must implement a control against [Topic]. They focus on [Indicator] because:",
        "An enterprise threat model highlights [Topic] as a high-probability risk. The team realizes that [Indicator] increases their exposure. How should they address this?",
        "A finance company is hit by a massive incident. Forensic reports show the root cause was [Topic] exploiting [Indicator]. What could have prevented this?",
        "When designing a secure cloud architecture, how do developers address [Topic] vulnerability associated with [Indicator]?",
        "Which of the following describes the operational impact of a successful [Topic] targeting [Indicator]?",
        "How does a Next-Generation security suite mitigate [Topic] when it detects [Indicator] in real-time traffic?",
        "A software startup wants to prevent [Topic]. Their lead architect suggests auditing [Indicator] periodically. Why?",
        "If a security operations team is assessing their defense-in-depth posture against [Topic], why is verifying [Indicator] crucial?",
        "A network administrator is configuring logs to monitor for [Topic]. They set up a trigger for [Indicator]. What type of event is this?",
        "Which security metric directly measures the effectiveness of controls designed to block [Topic] involving [Indicator]?",
        "In a threat hunt scenario, an analyst searches for signs of [Topic]. What indicator related to [Indicator] are they looking for?",
        "During a tabletop exercise, a team simulates a [Topic] breach via [Indicator]. What is the primary lesson learned?",
        "What is the relationship between [Topic] and [Indicator] in the context of the cyber kill chain?"
      ];

      const indicators = {
        "Weak Password Attack": [
          "multiple rapid login failures from a single IP",
          "default factory credentials left active on management consoles",
          "users utilizing consecutive keyboard combinations like 'qwerty'",
          "compromised hashes appearing in public databases",
          "credential stuffing attempts targeting VPN gateways",
          "lack of complexity requirements in active directory policies"
        ],
        "Phishing Attack": [
          "a suspicious email with mismatched SPF/DKIM authentication headers",
          "an urgent message requesting verification of bank login details",
          "a lookalike domain name mimicking the corporate login portal",
          "an unexpected invoice attachment with a macro-enabled extension",
          "unsolicited SMS messages containing shortened URL redirects",
          "an email claiming to be from the CEO requesting gift card purchases"
        ],
        "Malware Infection": [
          "unauthorized encrypted files with a '.locked' extension on servers",
          "unusual outbound traffic on non-standard ports to known C2 servers",
          "new persistent registry keys running strange binaries from AppData",
          "antivirus logs indicating multiple quarantined Trojan files",
          "unexplained high CPU utilization and disabled security services",
          "unknown processes attempting to inject code into svchost.exe"
        ],
        "Unsafe Public WiFi": [
          "ARP poisoning packets broadcasted across the local subnet",
          "an open hotspot matching the airport SSID but operating with low signal",
          "plain text passwords intercepted in HTTP POST requests",
          "unencrypted DNS queries leaking user browsing histories",
          "Man-in-the-Middle SSL certificate warning popups",
          "unauthorized local device discovery scans on network neighbors"
        ],
        "Data Leak": [
          "thousands of database customer records being sent to an external IP",
          "confidential design schematics uploaded to a public cloud storage folder",
          "sensitive API keys committed to a public Git repository",
          "DLP alerts triggering on outbound emails containing SSN formats",
          "proprietary source code leaked on underground developer forums",
          "an employee downloading large volumes of sales data to a USB drive"
        ],
        "Packet Filtering Firewall": [
          "ACL rules blocking port 22 traffic from unauthorized ranges",
          "stateless packet drops matching blocked destination IPs",
          "spoofed IP source packets masquerading as internal addresses",
          "heavy packet inspection CPU load on Layer 3 routers",
          "legacy rule logs allowing all traffic on port 80",
          "misconfigured rules causing drop of valid ICMP queries"
        ],
        "Stateful Inspection Firewall": [
          "TCP SYN packets initiating new entries in the state table",
          "packets dropped because they do not match an active session",
          "out-of-sequence TCP segments flagged as potential evasion",
          "exhaustion of state table memory due to a SYN flood",
          "connections terminated automatically after long periods of inactivity",
          "established TCP flags evaluated against session criteria"
        ],
        "Proxy Firewall": [
          "clients communicating only with local proxy IP on port 8080",
          "application payload inspections rewriting HTTP headers",
          "URL categorization rules blocking gambling web portals",
          "latency in web page rendering due to full application decode",
          "requests blocked due to unauthorized custom user-agents",
          "decrypted SSL sessions undergoing inspect at the gateway"
        ],
        "Cloud Firewall": [
          "security groups blocking traffic between web and database subnets",
          "dynamic policy updates tied to resource tags",
          "centralized hub-and-spoke virtual network rule enforcement",
          "API call logs indicating modifications to firewall parameters",
          "auto-scaling instances automatically receiving base rules",
          "egress traffic routes directed through cloud native gateways"
        ],
        "Software Firewall": [
          "local loopback connections blocked by local defender utility",
          "outbound application prompts asking for network privileges",
          "local host logs showing blocked port scans from LAN neighbors",
          "registry modifications attempting to disable firewall services",
          "iptables scripts defining local port forwarding rules",
          "application-specific blocks on background update processes"
        ],
        "In-House SOC": [
          "local SIEM dashboards displaying thousands of security events",
          "analysts manually writing custom scripts to parse unique logs",
          "internal training sessions on standard operating procedures",
          "alert queues accumulating due to high employee workload",
          "direct correlation of internal user directories with alert IPs",
          "threat hunting queries run against local historical log databases"
        ],
        "Managed SOC": [
          "an alert notification forwarded by the MSSP with triage notes",
          "weekly security summary reports delivered by email from the provider",
          "logs forwarded to external collector IPs over secure tunnels",
          "triage calls with external MSSP analysts during a breach",
          "SLA logs measuring provider response time for high alerts",
          "MSSP dashboard displaying alert activity for multiple clients"
        ],
        "Hybrid SOC": [
          "coordination between local Tier 2 analysts and MSSP Tier 1",
          "logs routed to both local fast storage and provider archive",
          "escalation tickets transferred from MSSP to internal response team",
          "joint tabletop simulations involving the outsourcing partner",
          "custom rule sync processes between internal SIEM and MSSP",
          "collaborative threat investigation channels in enterprise chat"
        ],
        "Co-Managed SOC": [
          "both teams active on the same SIEM cloud interface console",
          "incident notes updated simultaneously by vendor and client analysts",
          "shared dashboard views customized for different executive levels",
          "licensing fees split between security platform and expert analysts",
          "rules adjusted by client and verified by MSSP team leaders",
          "coordinated shift handovers using a unified ticketing tool"
        ],
        "Virtual SOC (vSOC)": [
          "analysts logging in from multiple countries using MFA tokens",
          "incident response war-rooms hosted on secure video lines",
          "virtual machine logs analyzed on cloud infrastructure consoles",
          "geographically distributed staff ensuring natural follow-the-sun coverage",
          "ticketing alerts generated directly into chat application channels",
          "strict auditing of analyst access IPs to the central console"
        ],
        "Identity-Based Architecture": [
          "MFA prompts triggered by logons from unfamiliar locations",
          "single sign-on configurations mapping groups to cloud resources",
          "real-time revocation of access when user privileges are modified",
          "verification of user attributes against active database directory",
          "adaptive authentication challenges based on user typing cadence",
          "service accounts executing tasks with short-lived tokens"
        ],
        "Device-Based Architecture": [
          "connections blocked because device patch level is out of compliance",
          "device health checks verifying active local antivirus software",
          "TPM verification checks during system boot sequences",
          "MDM profiles pushed automatically to company-owned mobile phones",
          "unregistered personal laptops redirected to guest network interfaces",
          "OS version checks blocking legacy browser execution"
        ],
        "Network-Based Architecture": [
          "ZTNA agents establishing secure point-to-point tunnels to applications",
          "micro-segmentation rules separating finance databases from general LAN",
          "explicit denies on lateral traffic between development and production",
          "logical perimeter gateways inspecting internal API requests",
          "software-defined WAN connections encrypting packet transfers",
          "internal network mappings indicating no broad subnet broadcasts"
        ],
        "Data-Centric Architecture": [
          "confidential watermarks embedded in exported spreadsheets",
          "data classification tags regulating file attachment policies",
          "files remaining encrypted even when copied to external USB drives",
          "DLP filters preventing copy-paste of sensitive database rows",
          "automatic expiration of access rights on shared document links",
          "granular database logs tracking specific table queries by user"
        ],
        "Infrastructure-Based Architecture": [
          "dynamic secrets rotating every hour in container environments",
          "mTLS configuration files verifying service-to-service calls",
          "IaC scan errors indicating open ports in cloud configurations",
          "container registry scans flagging critical vulnerabilities in images",
          "unauthorized modifications to network route tables in cloud consoles",
          "developer commits verified using hardware signing keys"
        ],
        "Preventive Resilience": [
          "vulnerability scans indicating zero critical issues on public servers",
          "web application firewalls blocking SQL injection payload strings",
          "employee completion rates of phishing simulation tests hitting 95%",
          "scheduled configuration audits aligning systems with security baselines",
          "system harden scripts removing unnecessary software programs",
          "strict password policies blocking common keyboard patterns"
        ],
        "Detective Resilience": [
          "SIEM rules triggering within 30 seconds of an attack sequence",
          "EDR alerts indicating suspicious process spawning from command lines",
          "honeypot systems logging unauthorized connection attempts on SSH ports",
          "anomalous activity detection logs flag high-volume folder access",
          "network flow logs indicating massive outbound data transfers",
          "third-party threat alerts listing corporate IPs in target lists"
        ],
        "Responsive Resilience": [
          "automated playbooks isolating compromised endpoints from the network",
          "CSIRT members utilizing pre-configured off-network communication lines",
          "containment logs showing successful network port blocks on firewalls",
          "incident response logs detailing root cause analysis steps",
          "crisis management alerts sent to legal and public relations teams",
          "evidence logs documenting chain of custody for forensics disks"
        ],
        "Recovery Resilience": [
          "bare-metal server restorations completed within the RTO target",
          "backup restorations verifying database integrity on clean environments",
          "immutable backup vaults blocking deletion commands during a breach",
          "failover systems switching traffic to secondary sites automatically",
          "data synchronizations matching the RPO targets for active databases",
          "disaster recovery logs documenting successful tabletop exercises"
        ],
        "Adaptive/Evolving Resilience": [
          "security logs showing rule updates based on post-incident reviews",
          "threat hunting processes identifying previously unknown security gaps",
          "threat intelligence feeds updating active firewall blocklists hourly",
          "tabletop exercise results highlighting communication bottlenecks for fix",
          "security posture score improvements documented in executive reports",
          "re-architect projects moving legacy servers to Zero Trust networks"
        ]
      };

      const correctAnswers = {
        "Weak Password Attack": [
          "Implement Multi-Factor Authentication (MFA) and account lockout policies.",
          "Enforce strong password complexity and length requirements via security policy.",
          "Use adaptive authentication and audit active directory for weak hashes.",
          "Deploy credential monitoring services and implement single sign-on (SSO).",
          "Ensure password hashing uses key stretching algorithms like bcrypt or Argon2.",
          "Conduct periodic audits of user credentials against known compromised lists."
        ],
        "Phishing Attack": [
          "Configure SPF, DKIM, and DMARC records to verify email senders.",
          "Deploy secure email gateways (SEG) with attachment sandboxing.",
          "Implement email banners warning users of external senders.",
          "Conduct regular phishing simulation training for employees.",
          "Implement FIDO2-compliant security keys for MFA to prevent credential theft.",
          "Deploy reporting plugins to allow users to quickly report suspicious emails."
        ],
        "Malware Infection": [
          "Deploy modern Endpoint Detection and Response (EDR) with heuristic scanning.",
          "Maintain offline, immutable backups and implement network segmentation.",
          "Restrict local administrative privileges and disable script execution.",
          "Implement application whitelisting and regular patch schedules.",
          "Analyze the file in an isolated sandbox and update firewall blocklists.",
          "Isolate the affected machine and conduct full system forensics."
        ],
        "Unsafe Public WiFi": [
          "Enforce the mandatory use of Enterprise VPNs for all remote work.",
          "Disable auto-connect configurations on corporate laptop WiFi adapters.",
          "Enforce DNS-over-HTTPS (DoH) and strict HTTPS-only transport policies.",
          "Implement WPA3 Enterprise security policies on remote endpoints.",
          "Deploy host-based firewalls that block all incoming local LAN traffic.",
          "Utilize cellular data hotspots instead of public networks for work."
        ],
        "Data Leak": [
          "Deploy Data Loss Prevention (DLP) agents to monitor outbound communications.",
          "Configure strict identity policies and encrypt data at rest and in transit.",
          "Implement fine-grained access controls and enable audit logging.",
          "Apply access reviews to all public storage buckets and repositories.",
          "Utilize file encryption and database activity monitoring (DAM) systems.",
          "Conduct risk assessments on third-party vendor integrations."
        ],
        "Packet Filtering Firewall": [
          "Add rules to drop inbound packets with spoofed internal source addresses.",
          "Migrate to a stateful inspection firewall to monitor session flows.",
          "Strictly enforce an 'implicit deny all' rule at the end of the ACL.",
          "Apply security controls to block unused ports and verify IP headers.",
          "Restrict ICMP traffic to minimize network scanning exposure.",
          "Configure logging for all denied packets to identify scan patterns."
        ],
        "Stateful Inspection Firewall": [
          "Ensure the state table is sized correctly to handle expected session volumes.",
          "Implement SYN cookies to prevent state table exhaustion attacks.",
          "Audit connection timeouts to clear inactive sessions from memory.",
          "Utilize stateful rules to bind active TCP flows to ACL conditions.",
          "Drop incoming packets that fail to match active connection states.",
          "Analyze log metrics for sudden surges in new state table entries."
        ],
        "Proxy Firewall": [
          "Configure deep application payload inspection for custom protocols.",
          "Enable SSL/TLS decryption to inspect encrypted web traffic.",
          "Enforce URL filtering based on reputational risk categories.",
          "Implement content caching to improve performance while maintaining blocks.",
          "Enforce browser user-agent checks at the proxy gateway.",
          "Route all outbound web traffic through the proxy and block direct egress."
        ],
        "Cloud Firewall": [
          "Implement security groups as dynamic firewalls at the instance layer.",
          "Use Infrastructure as Code (IaC) to audit and update firewall configurations.",
          "Deploy cloud-native firewalls with auto-scaling capabilities.",
          "Enforce micro-segmentation across virtual networks using subnet routes.",
          "Enable centralized cloud logging to track firewall policy modifications.",
          "Utilize metadata tags to dynamically apply security rules."
        ],
        "Software Firewall": [
          "Configure rules to block all inbound traffic by default on workstations.",
          "Integrate the software firewall with Endpoint Detection and Response (EDR).",
          "Restrict network configuration changes to administrative users only.",
          "Deploy centralized policies using Active Directory Group Policy Objects (GPO).",
          "Ensure outbound application traffic requires signed developer binaries.",
          "Log all local network connection attempts for centralized review."
        ],
        "In-House SOC": [
          "Focus on developing internal threat hunting capabilities and playbooks.",
          "Invest in automated triage tools to reduce alert fatigue for analysts.",
          "Define clear SLAs for incident investigation and escalation stages.",
          "Deploy a centralized SIEM to aggregate internal log data streams.",
          "Utilize SOAR playbooks to automate low-severity alert responses.",
          "Provide continuous training and career development paths for analysts."
        ],
        "Managed SOC": [
          "Verify the MSSP has appropriate context on critical asset classifications.",
          "Define clear escalation paths and response SLAs in the service contract.",
          "Install secure log forwarders to securely upload events to the provider.",
          "Audit the MSSP's performance periodically using simulation drills.",
          "Ensure local teams have visibility into the provider's triage notes.",
          "Perform regular meetings to review threat trends and log configurations."
        ],
        "Hybrid SOC": [
          "Leverage the MSSP for 24/7 basic monitoring while keeping response in-house.",
          "Implement collaborative ticketing systems to pass incidents smoothly.",
          "Train local Tier 2 staff to quickly assume containment on MSSP alerts.",
          "Use standard log formats to ensure both teams view the same data.",
          "Define specific criteria for when the MSSP can initiate block actions.",
          "Hold weekly syncs to align custom rule creation between teams."
        ],
        "Co-Managed SOC": [
          "Provide unified training on the shared SIEM platform for all analysts.",
          "Define a clear RACI matrix to allocate responsibilities between teams.",
          "Audit SIEM changes to ensure rule consistency across dashboards.",
          "Utilize unified ticketing systems to track remediation progress.",
          "Coordinate analyst shift handovers to ensure continuous coverage.",
          "Review shared reports regularly to measure overall operational health."
        ],
        "Virtual SOC (vSOC)": [
          "Implement strict MFA and secure VDIs for all remote analysts.",
          "Set up secure, encrypted communication channels for incident response.",
          "Deploy cloud-based SIEM systems to allow remote access from anywhere.",
          "Establish global schedules to ensure 24/7 coverage across timezones.",
          "Audit remote access logs to prevent credential sharing among analysts.",
          "Implement collaborative document systems for playbooks and procedures."
        ],
        "Identity-Based Architecture": [
          "Implement adaptive MFA that prompts on context changes like location.",
          "Enforce least privilege access based on verified user roles.",
          "Set up real-time policy evaluation for access to sensitive workloads.",
          "Ensure identity stores are audited and synchronized across applications.",
          "Disable legacy authentication protocols that bypass modern checks.",
          "Use short-lived session tokens for all user applications."
        ],
        "Device-Based Architecture": [
          "Deploy host compliance checks before allowing resource connections.",
          "Enforce MDM policies that mandate local encryption and antivirus.",
          "Use TPM chips to uniquely identify and attest hardware integrity.",
          "Quarantine endpoints that fail patch compliance assessments.",
          "Configure endpoint inventory tools to track hardware specifications.",
          "Block access for devices running deprecated or unpatched OS versions."
        ],
        "Network-Based Architecture": [
          "Implement network micro-segmentation to isolate critical zones.",
          "Deploy Zero Trust Network Access (ZTNA) solutions instead of VPNs.",
          "Decrypt and inspect all network traffic crossing segment boundaries.",
          "Use policy engines to dynamically control traffic flow permissions.",
          "Establish explicit block policies for all non-approved port requests.",
          "Implement dynamic routing configurations that adapt to threat levels."
        ],
        "Data-Centric Architecture": [
          "Apply file-level classification and digital rights management (DRM).",
          "Encrypt data at rest, in transit, and in use within database layers.",
          "Use DLP tools to inspect data transfers and prevent unauthorized copies.",
          "Implement data masking and tokenization for testing environments.",
          "Log all file access queries for suspicious bulk download behavior.",
          "Verify access rights for individual data files dynamically on open."
        ],
        "Infrastructure-Based Architecture": [
          "Enforce mTLS and cryptographic service identities for workloads.",
          "Deploy secret management systems to inject API keys dynamically.",
          "Conduct automated security scans on IaC templates prior to launch.",
          "Implement container vulnerability scanning in continuous delivery pipelines.",
          "Audit cloud configurations against CIS benchmarks automatically.",
          "Utilize read-only file systems for production container instances."
        ],
        "Preventive Resilience": [
          "Implement regular vulnerability management and configuration audits.",
          "Conduct continuous security awareness training and phishing simulations.",
          "Deploy web application firewalls and endpoint protection agents.",
          "Apply system hardening configurations based on security standards.",
          "Enforce least privilege access policies across all system configurations.",
          "Verify patch compliance rates meet corporate security standards."
        ],
        "Detective Resilience": [
          "Fine-tune SIEM rules to detect early indicators of compromise (IoC).",
          "Deploy EDR agents to monitor active process trees and memory states.",
          "Position honeypots in key subnets to catch lateral scan activity.",
          "Aggregate and analyze log data from all critical endpoints and clouds.",
          "Conduct threat hunting drills to identify undetected active intrusions.",
          "Integrate threat intelligence feeds to automate blocklist additions."
        ],
        "Responsive Resilience": [
          "Develop and test automated playbooks for isolating compromised hosts.",
          "Establish out-of-band communication plans for the incident team.",
          "Execute pre-defined containment steps to stop lateral malware spread.",
          "Conduct forensic investigations to determine attack entry vectors.",
          "Engage external incident response retainers for advanced containment.",
          "Document all response steps to ensure proper legal chain of custody."
        ],
        "Recovery Resilience": [
          "Maintain offline, air-gapped, or immutable backup architectures.",
          "Establish secondary hot-standby sites for critical services failover.",
          "Conduct regular disaster recovery exercises to test system rebuilds.",
          "Audit backup systems regularly to ensure data integrity during restores.",
          "Establish agreements with hardware vendors for quick physical replacement.",
          "Set RTO and RPO metrics that align with business continuity requirements."
        ],
        "Adaptive/Evolving Resilience": [
          "Conduct detailed post-incident reviews (PIR) to capture lessons learned.",
          "Update threat models and detection rules based on active intelligence.",
          "Run red team engagements to test the adaptability of defenses.",
          "Adjust security budgets to address gaps identified during exercises.",
          "Participate in industry information sharing portals (ISACs) for updates.",
          "Refactor legacy network architectures to incorporate Zero Trust models."
        ]
      };

      const distractorAnswers = {
        "Weak Password Attack": [
          ["Rely on users updating passwords manually every 90 days.", "Disable lockout policies to prevent denial of service.", "Utilize legacy SHA-1 hashing without salt additions."],
          ["Encrypt local desktop folders and disable remote desktop connections.", "Require users to store passwords in standard text spreadsheets.", "Implement DNS filters on all outbound HTTP traffic."],
          ["Install legacy antivirus scanners on primary web host servers.", "Perform weekly ping scans of local subnet environments.", "Utilize standard web application firewalls without custom rules."],
          ["Enable file sharing protocols on local developer machines.", "Set up reverse proxy networks to cache database results.", "Enforce frequent disk cleanup schedules on client machines."],
          ["Utilize standard MD5 hashing schemes for active credentials.", "Use basic firewall rules to monitor port access patterns.", "Disable all administrative access accounts temporarily."],
          ["Monitor network interface utilization statistics regularly.", "Set up local host name resolution tables on user laptops.", "Force system reboots daily for all remote developer hosts."]
        ],
        "Phishing Attack": [
          ["Block all external emails that contain hyperlinks or files.", "Disable email access on local mobile phone devices.", "Implement static routing tables for outbound mail flows."],
          ["Perform virus scanning of local operating system cache folders.", "Enforce hard drives partition encryption policies across laptops.", "Configure port forwarding rules on the local office router."],
          ["Install desktop screensavers displaying safety tips for users.", "Change the public DNS server to use alternative providers.", "Implement network address translation (NAT) at the perimeter."],
          ["Instruct users to ignore spelling errors in incoming messages.", "Configure standard content delivery networks for frontend hosts.", "Disable JavaScript execution on public corporate webpages."],
          ["Utilize basic password authentication without token parameters.", "Route all incoming emails through a local virtual proxy host.", "Generate new SSL certificates for internal websites weekly."],
          ["Increase internet subscription speeds for the central facility.", "Deploy local network load balancers to route email queues.", "Disable SMTP server logging to protect user privacy laws."]
        ],
        "Malware Infection": [
          ["Reboot the affected system and execute a standard disk scan.", "Delete the main file index registry to clear the malware trace.", "Increase RAM resources on the virtual host to handle load."],
          ["Configure local port scanning filters on standard switches.", "Disable server ping responses to hide them from the network.", "Reinstall the local network interface card driver utility."],
          ["Set up automated email alerts for low disk space notifications.", "Enable developer options on all corporate mobile phones.", "Restore system registry from a local unencrypted backup file."],
          ["Disable system logging to increase server computing performance.", "Route outbound web traffic through a single routing gate.", "Run manual disk defragmentation programs on server nodes."],
          ["Implement basic ACL rules on edge network router interfaces.", "Reboot the virtual machine and change root login passwords.", "Restore the database records using SQL backup scripts."],
          ["Report the incident to the ISP and wait for network updates.", "Delete the affected user's Active Directory account profile.", "Disable TCP/IP protocols on all local subnet adapters."]
        ],
        "Unsafe Public WiFi": [
          ["Install simple antivirus tools and disable the local firewall.", "Clear the browser cache history after every network use.", "Enforce MAC address changes on the network device weekly."],
          ["Deploy web application firewalls at the corporate data center.", "Enable file sharing services to facilitate team collaborations.", "Utilize static IP addressing schemes on the endpoint client."],
          ["Verify the SSL certificate fingerprint using a lookup portal.", "Configure static ARP table entries on all local laptops.", "Disable network discovery options on public network connections."],
          ["Deploy network switches with port isolation configurations.", "Configure proxy servers to cache web content locally.", "Update the network drivers on the client endpoint device."],
          ["Enforce access tokens on backend API servers directly.", "Implement static routing tables on corporate office routers.", "Run background malware sweeps on the client laptop node."],
          ["Change the browser home page to use secure local domains.", "Verify the DNS server settings are configured to DHCP mode.", "Restart the laptop network interface adapter utility software."]
        ],
        "Data Leak": [
          ["Reboot the active database server and update login keys.", "Disable outbound FTP traffic on standard network switches.", "Notify all corporate clients about the possible security event."],
          ["Re-index database tables to optimize search queries speed.", "Configure local hosts files to override DNS name resolution.", "Implement local firewall configurations on internal systems."],
          ["Restore cloud server state using automated build templates.", "Modify the DNS records to redirect traffic to staging servers.", "Generate new public SSH keys for deployment developers."],
          ["Change security groups to restrict incoming API connections.", "Perform code formatting checks on public Git integrations.", "Increase storage volumes on backup database storage nodes."],
          ["Configure reverse proxy servers to intercept public web requests.", "Implement single sign-on authentication across systems.", "Audit local active directory groups for inactive members."],
          ["Block incoming network requests from foreign IP ranges.", "Disable external web API endpoints during audit processes.", "Restore backup files to an offline verification system."]
        ],
        "Packet Filtering Firewall": [
          ["Route traffic through an application-layer proxy server interface.", "Increase the processing speed of local network interfaces.", "Configure dynamic routing protocols to bypass blocked nodes."],
          ["Perform stateful connection tracking of session handshakes.", "Verify that packet payload contents match approved signatures.", "Disable packet filtering to speed up network throughput rates."],
          ["Block all network communications on ports below 1024.", "Reboot the firewall router to clear connection cache tables.", "Enforce strict authentication for all incoming network packets."],
          ["Log all packets with high header options for future inspection.", "Configure DNS records to point to secondary host firewalls.", "Change network subnet masks to restrict internal IP ranges."],
          ["Update network routing parameters to utilize dynamic gateways.", "Implement software-based firewalls on all client endpoint hosts.", "Establish secure virtual private network connections for clients."],
          ["Perform packet captures of all incoming traffic streams.", "Disable administrative access to network firewall consoles.", "Verify that firewall configurations are stored in secure locations."]
        ],
        "Stateful Inspection Firewall": [
          ["Configure ACL rules to inspect application layer payload strings.", "Disable stateful monitoring to reduce processing overhead.", "Set up packet filtering rules based on source IP address lists."],
          ["Log connection attempts from internal user subnet ranges.", "Perform weekly reviews of firewall rules and access records.", "Configure network interface parameters to utilize full duplex."],
          ["Enable intrusion prevention modules on all network interfaces.", "Change firewall admin passwords and update SSH access keys.", "Perform automated vulnerability scans of target firewall nodes."],
          ["Reboot the firewall device to clear session memory caches.", "Route connection traffic through network load balancing systems.", "Implement proxy servers to handle application layer requests."],
          ["Generate new cryptographic keys for SSH console connections.", "Verify firewall hardware temperatures are within normal ranges.", "Configure static IP routing tables to ensure correct paths."],
          ["Audit active directory groups for unauthorized user additions.", "Deploy host-based security systems on database server nodes.", "Implement network access control policies on local switches."]
        ],
        "Proxy Firewall": [
          ["Disable proxy configurations to resolve network latency issues.", "Set up stateful firewall rules to monitor connection states.", "Implement network load balancers to route traffic to proxies."],
          ["Configure local host routing tables to bypass proxy gateways.", "Update client network driver software on local machines.", "Log proxy console connection events to central SIEM systems."],
          ["Deploy stateful firewalls at the network boundary layers.", "Modify dns parameters to resolve domain names locally.", "Enable network address translation to shield internal IP routes."],
          ["Configure client browsers to bypass proxy controls for HTTP.", "Reboot the proxy host server during peak operational hours.", "Change network subnet masks to increase local IP allocations."],
          ["Update active directory accounts to restrict administrative users.", "Implement software firewalls on client laptops and servers.", "Perform vulnerability scans on external proxy interfaces."],
          ["Utilize static IP addressing schemes on all client endpoints.", "Deploy hardware firewalls at the network aggregation layers.", "Configure DNS security options to block unauthorized queries."]
        ],
        "Cloud Firewall": [
          ["Install physical firewall appliances in cloud data centers.", "Disable cloud security groups to resolve connection bugs.", "Enforce local hardware firewalls on office server racks."],
          ["Perform manual updates of firewall rules weekly via console.", "Route cloud traffic through local office network systems.", "Implement basic packet filtering rules on local routers."],
          ["Configure cloud route tables to direct traffic to DNS hosts.", "Change admin credentials for the central cloud console.", "Generate new SSL certificates for cloud application gateways."],
          ["Reboot cloud instances to clear invalid configuration files.", "Verify that resource tagging matches naming standard guides.", "Deploy local network load balancers inside cloud subnets."],
          ["Enable audit logging for all database storage access queries.", "Implement single sign-on authentication for cloud access.", "Audit cloud administrator accounts for stale access keys."],
          ["Block incoming cloud connections using static IP listings.", "Disable cloud API endpoints to prevent unauthorized changes.", "Restore cloud configurations from local JSON backups."]
        ],
        "Software Firewall": [
          ["Disable local software firewalls to optimize application speed.", "Deploy hardware firewalls on every office client machine.", "Enforce network segment rules on core network switches."],
          ["Configure edge router ACLs to block incoming scan requests.", "Change root access codes on local host operating systems.", "Install local defragmentation software to clear file cache."],
          ["Reboot the computer to reset local firewall system services.", "Verify that local antivirus systems are running latest updates.", "Configure network adapters to use dynamic IP configurations."],
          ["Uninstall the software firewall and deploy cloud service rules.", "Limit user privileges on local workstation accounts.", "Implement virtual private network tunnels for remote systems."],
          ["Perform code review checks on local system utilities.", "Audit local active directory logs for logon event details.", "Disable loopback address configurations on host computers."],
          ["Generate new host certificates for local encrypted storage.", "Configure DNS host names to align with office naming guides.", "Disable network discovery features on the client computer."]
        ],
        "In-House SOC": [
          ["Outsource all security alerts triage to MSSP providers.", "Disable security logging to reduce SIEM licensing costs.", "Implement static routing rules to block unauthorized IPs."],
          ["Reboot SIEM servers during high traffic events to clear log queues.", "Change administrative passwords for local log databases.", "Enforce strict data compression ratios on storage arrays."],
          ["Deploy local network load balancers to route security events.", "Configure firewall rules to drop all unrecognized packets.", "Conduct vulnerability assessments on external facing systems."],
          ["Audit Active Directory groups for stale analyst credentials.", "Deploy host-based protection tools on core domain servers.", "Implement software firewalls on all analyst workstation nodes."],
          ["Update database index files to speed up search query returns.", "Configure DNS records to resolve internal hostnames faster.", "Utilize virtual private networks for analyst remote access."],
          ["Perform packet capture analysis on edge router interfaces.", "Disable security rules that generate excessive false alerts.", "Report security alerts directly to local systems managers."]
        ],
        "Managed SOC": [
          ["Deploy an in-house SIEM platform to duplicate alert analysis.", "Terminate MSSP contracts and deploy automated antivirus tools.", "Implement static firewall rules to block provider access IPs."],
          ["Change client active directory configurations to match MSSP.", "Disable logging on local host machines to protect user data.", "Perform weekly ping sweeps of client network environments."],
          ["Deploy hardware firewalls at the MSSP connection interfaces.", "Configure local hosts files to override MSSP name routing.", "Generate new SSL certificates for all internal client hosts."],
          ["Reboot log collectors to resolve event forward queue bugs.", "Audit Active Directory logs for provider analyst logins.", "Implement virtual private network tunnels for remote operations."],
          ["Perform automated code audits on client applications files.", "Configure DNS servers to utilize provider IP locations.", "Disable logging for low-severity system warning events."],
          ["Update client network drivers to optimize transfer bandwidth.", "Implement micro-segmentation on internal network subnets.", "Report incident alerts directly to executive management."]
        ],
        "Hybrid SOC": [
          ["Outsource all security operations to reduce internal costs.", "Deploy duplicate SIEM tools for both teams to run queries.", "Implement static firewall rules to separate analyst traffic."],
          ["Change analyst workspace configurations to match provider specs.", "Disable security log forwarding to local database storage.", "Perform weekly vulnerability scans of analyst laptops."],
          ["Deploy local network load balancers to distribute log traffic.", "Configure firewall rules to block all traffic from MSSP IPs.", "Audit local Active Directory groups for provider accounts."],
          ["Reboot security servers to clear event ticket queues.", "Implement virtual private network connections for remote teams.", "Perform code review checks on internal automation scripts."],
          ["Configure DNS records to resolve provider hostnames locally.", "Enable auditing for all database table access commands.", "Disable logging for debug messages on corporate systems."],
          ["Update network infrastructure bandwidth to support data logs.", "Implement software firewalls on internal server nodes.", "Report incident updates directly to third-party providers."]
        ],
        "Co-Managed SOC": [
          ["Deploy separate SIEM platforms for each analytical team.", "Terminate co-management agreements and rely on local firewalls.", "Implement static routing to separate analyst network zones."],
          ["Change SIEM administrator passwords without notifying the vendor.", "Disable log retention policies to save local storage space.", "Perform daily vulnerability scans of the SIEM platform."],
          ["Deploy hardware load balancers to split SIEM event queues.", "Configure firewall rules to deny provider console connections.", "Audit Active Directory logs for client analyst logon times."],
          ["Reboot SIEM dashboard servers to resolve event ticket errors.", "Implement virtual private network access for remote employees.", "Perform code formatting checks on shared analytics scripts."],
          ["Configure local DNS records to redirect SIEM traffic paths.", "Enable auditing for all internal database query operations.", "Disable logging for low-level system warning messages."],
          ["Update network drivers on client analyst workstation nodes.", "Implement software firewalls on internal server machines.", "Report SIEM platform issues directly to executive levels."]
        ],
        "Virtual SOC (vSOC)": [
          ["Require all remote analysts to work from a central office.", "Disable virtual private network access to optimize speeds.", "Implement static firewall rules to restrict analyst locations."],
          ["Change remote analyst laptop operating systems to match servers.", "Disable local security logging to protect user data privacy.", "Perform weekly vulnerability scans of remote analyst routers."],
          ["Deploy local network load balancers to route console traffic.", "Configure firewall rules to block all traffic from remote IPs.", "Audit Active Directory logs for remote analyst logins."],
          ["Reboot remote access gateway systems during active incidents.", "Implement virtual private network connections on public networks.", "Perform code formatting checks on remote analyst script commits."],
          ["Configure local DNS records to redirect remote access traffic.", "Enable auditing for all database query logs on local hosts.", "Disable logging for debug events on virtual host servers."],
          ["Update remote network router drivers to increase speeds.", "Implement software firewalls on local analyst workstation hosts.", "Report remote access issues directly to third-party vendors."]
        ],
        "Identity-Based Architecture": [
          ["Rely on static IP address listings for resource access.", "Disable multi-factor authentication to resolve login bugs.", "Implement network segmentation rules on local switches."],
          ["Change active directory database passwords on domain servers.", "Disable security logs on domain host controllers to speed up.", "Perform weekly port scans of domain active directory servers."],
          ["Deploy network load balancers to route authentication traffic.", "Configure firewall rules to drop all traffic from domain IPs.", "Audit Active Directory logs for admin privilege escalations."],
          ["Reboot authentication servers to resolve user login failures.", "Implement virtual private network tunnels for all endpoints.", "Perform code review checks on identity configuration scripts."],
          ["Configure local DNS hosts to override domain name paths.", "Enable auditing for all database record modifications.", "Disable logging for user authentication success events."],
          ["Update network driver software on database host servers.", "Implement software firewalls on user workstation computers.", "Report identity validation failures directly to managers."]
        ],
        "Device-Based Architecture": [
          ["Rely on user password validation to confirm device health.", "Disable endpoint compliance checks to speed up connections.", "Implement network segmentation rules on office switches."],
          ["Change local device administrator codes on client machines.", "Disable security logging on client endpoint operating systems.", "Perform weekly network scans of client host IP addresses."],
          ["Deploy network load balancers to route client device logs.", "Configure firewall rules to block all unregistered MACs.", "Audit Active Directory logs for client device additions."],
          ["Reboot client devices to clear invalid compliance flags.", "Implement virtual private network access for all endpoints.", "Perform code formatting checks on compliance check scripts."],
          ["Configure local DNS records to resolve device host names.", "Enable auditing for all database table access commands.", "Disable logging for device health check warning messages."],
          ["Update network drivers on client endpoint system adapters.", "Implement software firewalls on user workspace computers.", "Report device compliance status directly to local managers."]
        ],
        "Network-Based Architecture": [
          ["Utilize flat network structures with zero segmentation rules.", "Disable firewall rules to resolve network latency issues.", "Enforce password validation checks on all client systems."],
          ["Change local routing tables on endpoint client machines.", "Disable network traffic logging to protect user data files.", "Perform weekly port scans of network switch interfaces."],
          ["Deploy network load balancers to route segmentation logs.", "Configure firewall rules to drop all internal broadcast frames.", "Audit Active Directory logs for network access modifications."],
          ["Reboot network switches to resolve segmentation block issues.", "Implement virtual private network connections for remote users.", "Perform code formatting checks on routing script parameters."],
          ["Configure local DNS hosts to override internal route paths.", "Enable auditing for all database query logs on local hosts.", "Disable logging for network segment traversal events."],
          ["Update network interface drivers on database host systems.", "Implement software firewalls on client workstation computers.", "Report network boundary block events to executive levels."]
        ],
        "Data-Centric Architecture": [
          ["Enforce perimeter firewall rules to secure network boundaries.", "Disable file encryption to optimize database retrieval speeds.", "Implement password requirements for all client applications."],
          ["Change database access keys on file system registry logs.", "Disable file access logging to reduce SIEM storage needs.", "Perform weekly vulnerability scans of database files hosts."],
          ["Deploy network load balancers to distribute database queries.", "Configure firewall rules to block all traffic to database IPs.", "Audit Active Directory logs for database access additions."],
          ["Reboot database servers to resolve file encryption issues.", "Implement virtual private network tunnels for file transfers.", "Perform code formatting checks on classification scripts."],
          ["Configure local DNS records to redirect database query paths.", "Enable auditing for all internal database administration logs.", "Disable logging for file download success events on servers."],
          ["Update network adapter drivers on file storage host servers.", "Implement software firewalls on client workstation computers.", "Report database classification errors to local system managers."]
        ],
        "Infrastructure-Based Architecture": [
          ["Rely on developer passwords to secure cloud resources.", "Disable secret rotation policies to resolve system bugs.", "Implement network segmentation on local office switches."],
          ["Change cloud administrator passwords on corporate computers.", "Disable deployment logging to speed up container launch.", "Perform weekly port scans of container registry systems."],
          ["Deploy network load balancers to distribute workload logs.", "Configure firewall rules to drop container network frames.", "Audit Active Directory logs for developer account updates."],
          ["Reboot cloud instances to resolve container runtime errors.", "Implement virtual private network access for cloud consoles.", "Perform code formatting checks on IaC templates commit."],
          ["Configure local DNS records to redirect container route paths.", "Enable auditing for all cloud API configuration edits.", "Disable logging for service account token creation events."],
          ["Update network adapter drivers on cloud gateway platforms.", "Implement software firewalls on local workstation computers.", "Report cloud configuration errors directly to cloud vendors."]
        ],
        "Preventive Resilience": [
          ["Focus on restoring systems quickly after an incident occur.", "Disable security training to optimize employee work hours.", "Implement database backup procedures on secondary systems."],
          ["Change local host passwords weekly using automated scripts.", "Disable active logging to save disk storage on servers.", "Perform weekly vulnerability checks of backup storage nodes."],
          ["Deploy network load balancers to route security warnings.", "Configure firewall rules to block all external IP ranges.", "Audit Active Directory logs for system configuration edits."],
          ["Reboot core servers to clear active vulnerability states.", "Implement virtual private network tunnels for external users.", "Perform code review checks on vulnerability scan profiles."],
          ["Configure local DNS records to redirect security warnings.", "Enable auditing for all database query operations logs.", "Disable logging for vulnerability scanner run events."],
          ["Update network drivers on system boundary firewall hosts.", "Implement software firewalls on client workspace computers.", "Report scan results directly to local server administrators."]
        ],
        "Detective Resilience": [
          ["Implement preventative firewalls to block all threat entries.", "Disable security alerts to minimize analyst alert queues.", "Perform daily backups of core operating system files."],
          ["Change SIEM database passwords on centralized servers.", "Disable system logging to improve processor response speeds.", "Perform weekly vulnerability scans of SIEM server hosts."],
          ["Deploy network load balancers to route log aggregation streams.", "Configure firewall rules to block alert email communications.", "Audit Active Directory logs for security analyst additions."],
          ["Reboot log collectors to resolve log aggregation latency.", "Implement virtual private network access for monitoring consoles.", "Perform code formatting checks on SIEM detection rules."],
          ["Configure local DNS records to redirect event logs streams.", "Enable auditing for all database tables query records.", "Disable logging for low-level system configuration edits."],
          ["Update network adapter drivers on core log collector hosts.", "Implement software firewalls on local analyst workstation hosts.", "Report critical alerts directly to public relations managers."]
        ],
        "Responsive Resilience": [
          ["Wait for system backups to restore before taking containment action.", "Disable incident logging to speed up manual response efforts.", "Implement static routing to bypass affected network zones."],
          ["Change incident team leader accounts in Active Directory.", "Disable host logging to protect operational security data.", "Perform weekly vulnerability scans of incident team laptops."],
          ["Deploy local network load balancers to distribute alert logs.", "Configure firewall rules to block communication to incident hosts.", "Audit Active Directory logs for responder profile updates."],
          ["Reboot infected servers to clear active memory malware traces.", "Implement virtual private network connections for remote users.", "Perform code review checks on response playbook templates."],
          ["Configure DNS records to resolve responder workstation IPs.", "Enable auditing for all database records backup operations.", "Disable logging for incident containment playbook executions."],
          ["Update network drivers on incident responder workstations.", "Implement software firewalls on client laptops and computers.", "Report incident updates directly to third-party vendor teams."]
        ],
        "Recovery Resilience": [
          ["Enforce strict firewalls to prevent data deletion commands.", "Disable backup integrity checks to optimize system rebuilds.", "Implement password policies for all backup system accounts."],
          ["Change recovery team leader credentials in Active Directory.", "Disable logging during recovery to speed up system restores.", "Perform weekly port scans of backup system server hosts."],
          ["Deploy network load balancers to route database restores.", "Configure firewall rules to deny backup console connections.", "Audit Active Directory logs for backup restoration events."],
          ["Reboot backup servers to resolve data synchronization issues.", "Implement virtual private network access for restore systems.", "Perform code review checks on disaster recovery playbooks."],
          ["Configure local DNS records to redirect backup recovery paths.", "Enable auditing for all restore operations logs on servers.", "Disable logging for backup verification task completions."],
          ["Update network adapter drivers on backup system storage hosts.", "Implement software firewalls on recovery workstation computers.", "Report recovery updates directly to external auditing firms."]
        ],
        "Adaptive/Evolving Resilience": [
          ["Utilize static backup files to restore server operations.", "Disable threat intelligence feeds to reduce network traffic.", "Implement password changes for all corporate database users."],
          ["Change threat hunter credentials in Active Directory logs.", "Disable logging during reviews to protect security discussions.", "Perform weekly port scans of threat intelligence servers."],
          ["Deploy network load balancers to route threat intelligence logs.", "Configure firewall rules to drop incoming threat feeds files.", "Audit Active Directory logs for security updates modifications."],
          ["Reboot security systems to clear incident lesson archives.", "Implement virtual private network connections for external teams.", "Perform code review checks on security configuration scripts."],
          ["Configure local DNS hosts to redirect threat intel streams.", "Enable auditing for all threat hunter dashboard query logs.", "Disable logging for tabletop exercise coordination events."],
          ["Update network drivers on threat hunting workstation nodes.", "Implement software firewalls on local security management hosts.", "Report post-incident lessons directly to media channels."]
        ]
      };

      for (let i = 0; i < templatesNeeded; i++) {
        // Pick templates and indicators cyclically to avoid index error
        const scenarioTpl = scenarios[i % scenarios.length];
        const indicatorList = indicators[topic];
        const indicator = indicatorList[i % indicatorList.length];
        
        // Form the question
        const questionText = scenarioTpl
          .replace("[Topic]", topic)
          .replace("[Indicator]", indicator);

        // Pick answers cyclically
        const correctAnsList = correctAnswers[topic];
        const answer = correctAnsList[i % correctAnsList.length];

        // Pick distractors
        const distractorList = distractorAnswers[topic];
        const distractors = distractorList[i % distractorList.length];

        // Combine and shuffle options
        const options = [answer, ...distractors];

        allQuestions.push({
          id: `q_${idCounter++}`,
          level: levelId,
          topic: topic,
          question: questionText,
          options: options,
          answer: answer
        });
      }
    }
  }

  // Shuffle options in each question (but keep target answer correct)
  allQuestions.forEach(q => {
    // Standard Fisher-Yates shuffle
    const options = [...q.options];
    for (let i = options.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [options[i], options[j]] = [options[j], options[i]];
    }
    q.options = options;
  });

  return allQuestions;
};

const main = () => {
  console.log("Generating 500+ cybersecurity questions...");
  const questions = generateAllQuestions();
  console.log(`Generated ${questions.length} total questions.`);

  const outputDir = path.join(__dirname, 'data');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const outputPath = path.join(outputDir, 'questions.json');
  fs.writeFileSync(outputPath, JSON.stringify(questions, null, 2), 'utf-8');
  console.log(`Successfully wrote questions database to ${outputPath}`);
};

main();
