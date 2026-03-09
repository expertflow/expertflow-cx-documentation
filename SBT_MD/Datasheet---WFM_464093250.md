# CX Knowledgebase : Datasheet - WFM

The **Workforce Management (WFM)** provides a comprehensive set of features aimed at streamlining workforce operations and enhancing employee management efficiency. 

Below is a summary of its key functionalities.

**Features**| **Description**  
---|---  
**Contracts Management**|  Define and manage working hours per agent while ensuring full compliance with labor laws and company policies. The system supports flexible contract types, including full-time and part-time arrangements, with customizable working day rules, minimum/maximum weekly hours, and daily limits. Administrators can configure rest periods, tolerance rules, and boundary conditions to maintain compliance.  
**Organizational Structure**|  Model a multi-level hierarchy by **Organization → Location → Team** , with role-based access controls. This structure provides a consistent framework for scheduling, calendar views, adherence monitoring, and request management across different teams and geographies.  
**Activities**| **Activity Management** Maintain a centralized library of activities (work, breaks, training, coaching, meetings, off-phone tasks). Each activity is characterized by attributes such as inclusion in paid work time, contractual compliance, skill requirements, seat allocation, and cost classification.**Activity Drill-Down** Detailed timeline of agent-level activities. Shows distribution of work, breaks, training, and off-phone tasks for micro-level analysis and optimization.  
**Leave Management**|  Define multiple leave types (Annual, Sick, Study, Unpaid, Maternity, etc.) with customizable rules for pay, contract time inclusion, entitlement tracking (in days or hours), and confidentiality settings. Integrated workflows support self-service agent requests, supervisor approvals, quota validation, and automatic integration into rosters.  
**Shift Swap & Trade Policies**| Configure peer-to-peer swap and open trade rules, including eligibility windows for trading window, skill matching between participants, minimum rest requirements, and tolerance checks for contractual hours. Policies ensure swaps do not create coverage gaps or violate compliance.   
**Forecaster**| **Skills & Service Targets**Define staffing requirements based on skills, queues, or services. Parameters include Service Level (SL), Occupancy, and Shrinkage. Skill tagging ensures only qualified agents are assigned, while service targets drive accurate headcount requirements for forecasting and scheduling.**Workload Preparation (Historical Data)** Import and validate historical data (offered contacts, average handle time, after-call work). Charts and tables highlight anomalies (outliers, missing intervals), allowing planners to adjust before using the data for forecasting. Supports queue-level data, including overflow and routing splits.**Forecasting & Staffing Requirements**The system automatically generates call volume forecasts, calculates talk/ACW times, and derives required headcount before and after shrinkage. Supervisors only provide shrinkage percentages, while the system manages workload modeling, interval breakdowns, and side-by-side overlays of forecasted demand versus staffing capacity.**Data Modes & Validation**Supervisors can compare multiple datasets to ensure forecast accuracy:

  * **Original Data** – raw imported data from historical queues.
  * **Validated Data** – adjusted by supervisors to correct anomalies before forecasting.
  * **Day-of-Week Averages** – smoothed profiles for identifying recurring patterns.

Each dataset serves a distinct purpose. Original ensures transparency, Validated supports corrections, and Day-of-Week averages highlight trends. Supervisors can review them side by side and refine validated data before finalizing forecasts.  
**Shift**| **Shift Categories** Classify shifts (Morning, Evening, Night, etc.) with visual codes and color tags for faster planning, searching, and reporting. Categories support automated allocation, targeted reporting by shift type, and trend analysis for workforce distribution.**Shift Library** Maintain a reusable catalog of shifts with categories, start/end times, and embedded activities. Standardizes schedules across teams and reduces manual effort in roster creation. Supports parameterized templates for global reuse.**Shift Designer** Design shifts with base and additional activities (work tasks, breaks, meetings, training) using configurable early/late start and end windows and segment sizes (e.g., 15/30 minutes). The system applies defined rules to generate and validate all possible shift variations automatically, ensuring activity placement complies with labor policies, contract constraints, and organizational scheduling standards before finalization.  
**Scheduler**| **Schedule Workspace** An interactive workspace to open schedules by team, location, or time range. Provides visual coverage charts, variance analysis, and drill-downs. Supervisors can test “what-if” scenarios, make last-minute adjustments, and save/publish schedules with confidence.**Coverage Analysis** Visual overlays compare forecasted workload against scheduled staffing. Variance lines and threshold indicators highlight shortages or surpluses. Hover-over tooltips reveal exact values per interval, enabling supervisors to spot gaps quickly and adjust coverage.**Forecast vs. Schedule Grid** Tabular view of each interval showing forecasted hours, scheduled hours, variance, and assigned agents. Conditional formatting highlights where demand and staffing are misaligned, supporting faster corrections.**Schedule Period Controls** Define eligibility for scheduling within a set date range, weekly start day, templates, and planning horizon. Prevents allocation of shifts outside valid contract periods or beyond termination dates.  
**Requests Center**|  Centralized dashboard of all pending/approved/rejected requests (leave, swaps, trades). Provides visibility across teams with filtering and status tracking.  
**Workforce**| **User Management**  
Import users in bulk via Excel or manage individually through a tabbed editor (General, Person Period, Schedule Period, Leaves). Roles and teams directly control scheduling eligibility and reporting visibility.**General** Store core details including ID, Name, Email, Username, Roles, Timezone, and Notes. Roles define user permissions across the WFM system.**Person Period** Link each user to their assigned Team, Skills, and Contract, ensuring scheduling and adherence rules are applied correctly.**Schedule Period** Define when and how the user is scheduled. Parameters include Week Start, Shift pattern, Schedule Start/End Dates, and Leaving Date. These dates act as hard boundaries for automated scheduling.**Leave Management** Configure multiple leave types (Annual, Sick, Study, Unpaid, Maternity, etc.) with entitlement tracking by hours or days. Approved leaves are automatically blocked in schedules to avoid conflicts. Confidentiality settings restrict visibility as required.  
**Agent Calendar**| **Leave Requests (In-App)** Agents can request full-day or partial-day leave directly from their personal calendar. Requests are validated against quotas and balances before being approved by the supervisor. Approved leave blocks future scheduling conflicts automatically.**My View** Personalized view of schedules in **Day, Week, or Month** formats. Automatically reflects time zone differences and uses consistent color-coding for activities.**Team Schedule View** Grid-based view of all team members’ schedules with filtering and scrolling. Supervisors can manage multiple teams, compare headcount, and identify coverage issues in one screen.**Inline Shift Swap** Agents initiate swaps directly from the team schedule. Automated validations check skills, contracts, eligibility windows, and workload impact before allowing confirmation.**Open Swap Board** A shared marketplace where agents can post available shifts. Eligible peers can pick up shifts subject to skill and policy validations. Promotes flexibility while ensuring service-level coverage.  
**Adherence**| **Adherence Configuration** Define mappings between real-time ACD states (Ready, Not Ready, ACW, Break, etc.) and planned activities. Configurable rules determine what counts as “in adherence” vs. “out of adherence.”**Adherence Detail Reports** Detailed agent-level adherence reports with metrics on schedule deviations, adherence %, break compliance, and before/after-shift activity. Enables both daily tracking and long-term adherence trend analysis.**Real-Time Adherence Monitoring** Live dashboard showing adherence by team, location, and agent. Displays planned vs. actual states, current rule results, time in state, and adherence percentage. Enables supervisors to act on deviations in real time.  
**Reporting & Exports**| Generate operational and compliance reports such as Queue Statistics, Agent Statistics, Shrinkage, and Schedule Efficiency. Reports can be filtered by date, team, or activity. Export options include PDF, CSV, or HTML for distribution or external analysis.  
  
## Deployment and Scalability

### Microservices

  * **Kubernetes** : All services (auth, core, connector, reporting) are deployed as microservices on Kubernetes, ensuring scalability and resilience.

  * **Helm Charts** : Helm charts are used to manage Kubernetes deployments, providing a templated approach to deploy and manage the microservices.




## Security Considerations

  * **OAuth2 & JWT**: Secure user authentication using OAuth2 and JWT, with token validation in every request.

  * **Database Security** : Encryption of sensitive data in PostgreSQL, with strict access controls.

  * **Kubernetes Security** : Implementation of network policies and secrets management for secure service communication.




## Performance and Scalability

### Microservices Architecture

  * **Service Communication** : RESTful APIs for communication between services.

  * **Load Balancing** : Kubernetes-managed load balancing across service instances.

  * **Horizontal Scaling** : Services scale horizontally in Kubernetes using the Horizontal Pod Autoscaler (HPA).




## Kubernetes Deployment

### Containerization

  * **Docker** : Services are containerized using Docker, with Dockerfiles for each service.

  * **Helm Charts** : Helm charts are used for managing Kubernetes deployments, ensuring consistent and repeatable deployments across environments.



