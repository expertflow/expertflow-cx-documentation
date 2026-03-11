import os
from pathlib import Path
import re

def patch_links(root_dir):
    root_path = Path(root_dir)
    
    # Precise redirect map for known broken links
    redirect_map = {
        "1687093262.md": "ARCHIVE_NOTICE.md",
        "1070825519.md": "ARCHIVE_NOTICE.md",
        "2525731.md": "ARCHIVE_NOTICE.md",
        "PI-Roadmap_1382678547.html": "ARCHIVE_NOTICE.md",
        "Application-Security_2527480.html": "ARCHIVE_NOTICE.md",
        "Data-Encryption.md": "Solution_Admin/Encryption-at-Rest-Configuration-Guide.md",
        "PII-Data-Masking.md": "ARCHIVE_NOTICE.md",
        "Socket-Events-Schema-Reference.md": "Developer/Socket-Events.md",
        "Designing-Evaluation-Forms.md": "QM/Designing-Evaluation-Forms.md",
        "index.md": "ARCHIVE_NOTICE.md",
        "Campaign-Management.md": "Solution_Admin/Managing-Outbound-Campaigns.md",
        "WFM-Prerequisites.md": "Functional_Areas/Workforce_Schedule_Management/WFM-Prerequisites.md",
        "Media-Server-Deployment-Guide.md": "Partner/CX-SIP-Proxy-Installation-Guide.md",
        "CX-Solution-Helm-Uninstallation.md": "Partner/Helm-Based-Application-Deployment.md",
        "ETCD-Backup-and-Restore.md": "ARCHIVE_NOTICE.md",
        "Failover-Cluster-Replicated-Block-Volume.md": "ARCHIVE_NOTICE.md",
        "Silent-Monitoring-and-Coaching.md": "ARCHIVE_NOTICE.md",
        "Handle-Multi-channel-Conversation_2528824.md": "Agent/Accept-a-Conversation.md",
        "Handle-Multi-channel-Conversation.md": "Agent/Accept-a-Conversation.md",
        "Creating-a-Simple-Flow-in-Studio_512163856.md": "Designer/Conversation-Studio-Fundamentals.md",
        "Studio-Nodes_2530098.md": "ARCHIVE_NOTICE.md",
        "Form-Builder_866812373.md": "Designer/Creating-Survey-Forms-and-Flows.md",
        "Task-Reason-Codes_144212603.md": "Solution_Admin/Configuring-Reason-Codes.md",
        "Cisco-Voice-Channel-Configuration-Guide_2527992.md": "Integrator/Cisco-Voice-Channel-Configuration.md",
        "CX-Voice-Channel-Configuration-Guide.md": "Solution_Admin/Voice-Channel-Configuration-Limitations.md",
        "Database-Backup-Restore-Manual.md": "ARCHIVE_NOTICE.md",
        "Kubernetes-Backup-Velero.md": "ARCHIVE_NOTICE.md",
        "Channel-Related-Objects_276594689.md": "Developer/Conversation-Life-Cycle-Objects.md",
        "UTC-Offset---Reports_2526326.md": "Functional_Areas/Performance_Insights_Data/UTC-Offset-Reports.md",
        "Configure-Vault-for-MongoDB-Dynamic-Credentials.md": "Solution_Admin/Vault-Dynamic-Credentials-MongoDB.md",
        "Configure-Vault-for-Redis-Credentials.md": "Solution_Admin/Vault-Dynamic-Credentials-Redis.md",
        "Configure-Vault-for-PostgreSQL-Dynamic-Credentials.md": "Solution_Admin/Vault-Dynamic-Credentials-MongoDB.md",
        "Configure-Vault-for-ActiveMQ.md": "Solution_Admin/Vault-Dynamic-Credentials-ActiveMQ.md",
        "679117567.md": "Developer/YouTube-Integration-Configuration-Developer.md",
        "Historical-Reports_1321664626.md": "Supervisor/Historical-Reports-Reference.md"
    }
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    total_patched = 0
    
    for md_file in root_path.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def fix_orphans(match):
            text = match.group(1)
            link = match.group(2)
            
            # Skip external
            if link.startswith("http") or link.startswith("#"):
                return match.group(0)
            
            # Clean link for lookup
            link_stem = Path(link.split('#')[0]).name
            
            if link_stem in redirect_map:
                target_path = root_path / redirect_map[link_stem]
                # Calculate relative path
                try:
                    new_rel = os.path.relpath(target_path, md_file.parent)
                    return f"[{text}]({new_rel})"
                except:
                    return match.group(0)
            
            # Handle deep relative path errors (../../Role-Based_Guides/...)
            if "../../Role-Based_Guides/" in link:
                # Flatten the path to search within Phase4
                simplified = link.split('/')[-1]
                # Try to find this file anywhere in Phase4
                for candidate in root_path.rglob(simplified):
                    new_rel = os.path.relpath(candidate, md_file.parent)
                    return f"[{text}]({new_rel})"
            
            return match.group(0)

        new_content = link_pattern.sub(fix_orphans, content)
        
        # Also catch remaining .html strings
        new_content = new_content.replace(".html", ".md")
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            total_patched += 1
            
    print(f"Final patch applied to {total_patched} files.")

if __name__ == "__main__":
    patch_links("Phase4")
