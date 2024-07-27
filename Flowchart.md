## Flowchart Description

### Overview
The flowchart describes the decision-making process for categorizing and responding to emails.

1. **Email Reception**: An email is received by the system.
2. **Category Classification**: Determine if the email is an inquiry, review, or assistance request.
   - **Inquiry Handling**:
     - Check database for item availability.
     - If available, reply with price.
     - If not available, suggest similar items.
   - **Review Handling**:
     - **Positive**: Thank sender and encourage sharing on social media.
     - **Negative**: Escalate to CRM, reply with gift voucher.
   - **Assistance Request Handling**:
     - Retrieve solution using RAG pipeline.
     - If found, reply with solution.
     - If not, escalate to customer service.
   - **General Handling**: Forward to customer service.
