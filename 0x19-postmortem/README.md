# Postmortem: Web Stack Outage Incident

## Issue Summary
- **Duration:**
  - Start Time: November 12, 2023, 09:15 AM (GMT+1)
  - End Time: November 12, 2023, 11:45 AM (GMT+1)
- **Impact:**
  - 🚫 Web application downtime: 30 minutes
  - 🐢 Users experienced slow response times and intermittent errors
  - 🤔 Approximately 12% of users were affected

## Root Cause
- The outage was caused by a database connection leak that led to a spike in connection pool usage, exhausting available resources.

## Timeline
- **09:15 AM (GMT+1):**
  - **Detection:** An automated monitoring alert flagged an increased number of database connections and latency.
- **09:20 AM (GMT+1):**
  - **Actions Taken:**
    - Initial investigation focused on the database servers.
    - Assumed root cause: Database performance degradation due to increased load.
- **09:40 AM (GMT+1):**
  - **Misleading Paths:**
    - Database servers were optimized for performance, but the issue persisted.
    - Investigated network issues, suspecting latency between web servers and the database.
- **10:00 AM (GMT+1):**
  - **Escalation:**
    - Issue escalated to the database and networking teams.
    - Database team identified the connection leak but believed it was a symptom, not the root cause.
- **10:30 AM (GMT+1):**
  - **Resolution:**
    - Database team implemented a temporary fix by restarting the database server, clearing all existing connections.
    - Web team deployed a hotfix to address the connection leak in the application code.

## Root Cause and Resolution
- **Root Cause:**
  - A code change in a recent deployment inadvertently introduced a database connection leak.
  - Leaked connections accumulated over time, causing the database connection pool to reach its limit.
- **Resolution:**
  - Immediate action taken to restart the database server and clear all existing connections.
  - Code fix deployed to the web application, addressing the connection leak issue.

## Corrective and Preventative Measures
- **Improvements/Fixes:**
  - Implement more comprehensive monitoring for database connections and resource usage.
  - Enhance deployment procedures to include thorough code reviews for potential resource leaks.
- **Tasks:**
  - Patch database connection pooling mechanism to automatically reclaim and release idle connections.
  - Conduct a post-incident review with the development team to reinforce best practices for code changes.
  - Strengthen collaboration between development and operations teams to streamline issue resolution.

## Conclusion
The web stack outage was swiftly addressed through a combination of database server restart and code fix. The incident highlighted the importance of vigilant monitoring and effective communication between teams during troubleshooting. Moving forward, the implementation of preventive measures and continuous improvement in deployment practices will minimize the likelihood of similar incidents. This postmortem serves as a valuable learning experience for the entire team, reinforcing the need for proactive measures to maintain the stability and reliability of our web services.
