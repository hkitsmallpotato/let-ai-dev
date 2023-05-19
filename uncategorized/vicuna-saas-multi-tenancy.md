# Vicuna design multi-tenancy feature in SaaS

## SaaS multi-tenancy

**Human**:

A common feature in SaaS platform is multi-tenancy. One way to implement this is as follows:There are many Organisations (Org). Users begin without belonging to Org, but they can create and join Org. Org has admin User with administrative control over Org policy, one of which is the right to invite User to join.

Projects are the unit of workload isolation. Projects are created by, and belongs to Org.

Projects acquire usage charge, which are accounted to Org. Therefore each Org is required to have an associated billing account, which can be owned and created by any User in the Org, but only Org admin has the right to assign said account to Org (subject to billing account User’s approval). Org without billing account will have some actions forbidden.

One way to perform billing is a monthly invoice model.

Given these info, propose a design for a RESTful API for these aspects. Focus on resource modelling (with URL) instead of repetitive CRUD operation. Exceptions are allowed for intricate transactional flows.

**AI**:

Here is a proposed design for a RESTful API for the given information:

Resources:
* User
* Org
* Project
* BillingAccount

Actions:
* create/join Org
* create/join Project
* assign BillingAccount to Org
* get User, Org, Project, and BillingAccount information

URLs:
* `/users/{user_id}` - get user information
* `/orgs/{org_id}` - get org information
* `/orgs/{org_id}/projects` - get a list of projects for a specific org
* `/orgs/{org_id}/projects/{project_id}` - get project information
* `/billing-accounts/{billing_account_id}` - get billing account information
* `/billing-accounts/{billing_account_id}/assign` - assign billing account to org (POST)

Note: It's important to consider security and access control when designing a RESTful API. This proposal does not include specific details on how to handle authentication and authorization.

**Human**:

- How should a user 1) create, 2) join an Org?
- An Org's admin is by default the User who created it, but admin can also make other Users in the Org an admin. How to do this through API?
- Org admin also has the right to transfer project ownership to another Org, how to do this?

**AI**:

To create or join an Org through the API, a user would need to make a POST request to the /orgs resource with a JSON payload that includes the org information. The payload could include the org name, description, and any other relevant information. The API could also require the user to provide their own user ID, as well as the ID of the org they want to join.

To make a user an admin of an Org through the API, the org admin would need to make a PUT request to the `/orgs/{org_id}/admins/{user_id}` resource. This would update the org admin information for the specified user.

To transfer project ownership to another Org through the API, the org admin of the current owner would need to make a DELETE request to the `/orgs/{current_org_id}/projects/{project_id}` resource, and then a PUT request to the same resource with the new org ID in the path. This would remove the project from the current org and add it to the new org. The API could also require the new org to be specified in the request payload.

**Human**:

Make a change: now there is the concept of admin and superadmin's. Superadmin is a more powerful version of admin and there can only be one superadmin in an org at a time. By default the User who created the Org is the superadmin of that Org. The difference between admin and superadmin is that while admin can make other User in an Org an admin, only superadmin can remove admin status from a User in that Org. Only Superadmin him/herself can transfer the superadmin status to another User he/she designate within the Org. Suggest what change to the API should be make and any flow affected or other noteworthy things.

**AI**:

To reflect the new concept of superadmins in the API, the `/orgs` resource could include a new property called `superadmin_id` that indicates the ID of the superadmin for the org. This property could be read-only, and the only way to change it would be through a transactional flow that involves updating the superadmin_id property and removing the admin property for the current superadmin.

To make a user an admin or superadmin of an Org through the API, the org admin would need to make a PUT request to the `/orgs/{org_id}/admins` resource, including the user ID and the admin flag. If the user is already an admin, this would update their admin status. If the user is not an admin and the org has only one superadmin, the request would need to include the superadmin flag, and the API would check if the user is the current superadmin before updating their status. If the org has multiple admins, the request would only need to include the admin flag.

To remove admin status from a User in an Org, only the superadmin of the org would be able to make a DELETE request to the `/orgs/{org_id}/admins/{user_id}` resource. This would remove the admin status for the specified user, and if the user was also a superadmin, the superadmin status would be transferred to another User designated by the superadmin.

Note: It's important to consider security and access control when designing a RESTful API. This proposal does not include specific details on how to handle authentication and authorization.

