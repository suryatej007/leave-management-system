# leave-management-system
Seamless HR Solutions: Building a Leave Approval System with AWS

**OBJECTIVE **

The project aims to develop a Leave Management System to facilitate leave requests within an organization. This system will enable employees to submit leave applications and allow HR personnel to review, approve, or reject these requests. Upon approval or rejection, the system will automatically send email notifications to the respective employees.

**KEY FEATURES**

Effortless Leave Application: Employees can conveniently submit leave requests online, streamlining the entire process.

Instant Confirmation: Upon submitting a leave application, employees receive immediate confirmation, ensuring transparency and peace of mind.

Automated Notification for New Requests: Administrators are promptly notified of new leave requests, enabling swift action and reducing response times.

Reminder Notifications: To prevent delays, automated reminders are sent to approvers, ensuring timely review of pending leave requests.

Real-time Approval/Rejection Notifications: Upon approval or rejection, employees receive instant notifications, providing clarity and eliminating uncertainties.

**LIST OF THE AWS SERVICES USED**

AWS Lambda: Powers backend logic for leave request processing, notifications, and approval/rejection handling, ensuring scalable and serverless execution.
Amazon SES (Simple Email Service): Sends email notifications to employees and approvers for leave requests, approvals, and rejections, ensuring reliable delivery.
Amazon API Gateway: Acts as an interface between the frontend application and backend Lambda functions, enabling secure and efficient communication via RESTful APIs.
Amazon S3 (Simple Storage Service): Hosts frontend assets (HTML, CSS, JavaScript) for the Leave Management System, providing scalable and reliable static web content storage.
Amazon DynamoDB: Stores and manages leave request, employee, approval, and audit trail data, offering a fully managed NoSQL database service with seamless scalability and low latency access.

**HOW DOES THIS PROJECT WORK **

Employee Submits Leave Request:Employee accesses the Leave Management System's frontend interface.They fill out the leave request form with details such as start date and end date.Upon completion, the employee submits the leave request.

Notification to HR:Upon submission, the system notifies the HR department about the new leave request. HR can access the system through their interface or receive email notifications.

HR Reviews Leave Request:HR personnel review the leave request details, including the employee's name and requested dates.Based on organizational policies and workload considerations, HR approves or rejects the leave request.

Notification to Employee:The system sends a notification to the employee regarding the approval or rejection of their leave request.

Employee Accesses Leave Status:The employee can check the status of their leave request through the system's frontend interface.They can view whether their request has been approved, rejected, or is still pending.
