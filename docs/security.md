## Overview

This section explains how Curate manages Role-Based Access Control (RBAC) and how it integrates with SSO providers. Specifically, it addresses the requirements for managing access to sensitive documents, such as those intended exclusively for specific teams.

## Understanding Role-Based Access in Curate

Curate implements a robust RBAC system that determines which users can access specific workspaces, folders, and files. The system uses several key concepts:

### Key Concepts

1. **Roles**: Container for a set of permissions that define what actions a user can perform in the system
2. **Access Control Lists (ACLs)**: Sets of permissions attached to roles that grant access to specific areas
3. **Groups**: Hierarchical organisation of users that can inherit roles
4. **Security Policies**: Dynamic rules that can grant or restrict access based on context (time, location, etc.)

### How Roles Work in Curate

- Each user in Curate can be assigned one or more roles
- Roles determine what folders and files a user can see and what actions they can perform
- Permissions can be applied at the workspace level (by Penwern) or at specific folder/file levels (which can be managed within your organisation)
- When multiple permissions apply, they follow specific merging rules:
  - Deny by Default: If no access is explicitly granted, access is denied
  - Explicit Denial Wins: If a "Deny" permission exists at any level, it overrides any "Allow" permissions

### Role Management Process

### Current Setup

In your Curate implementation, role management is handled by Penwern (as the system administrators). End users and local administrators do not have direct access to role creation in the system.

### Role Creation Process

When you need to create specialised roles:

1. **Request a Role**: Contact Penwern support to request creation of a new role
2. **Define Access Permissions**: Specify which workspaces or folders this role should have apply to
3. **Specify Security Policies**: If needed, define any specific conditions for access (time restrictions, IP limitations, etc.)

Penwern will create the role in the Curate system according to these specifications.

## Integration with SSO Providers

To manage which users are assigned to specific roles, you'll use a combination of group management in your SSO provider and role mapping in Curate.

### Setting Up Access for Specific Documents

#### Step 1: Create a Security Group in Your SSO Provider

1. In your SSO providers admin centre, create a security group (e.g., "Executive Team")
2. Add the appropriate users to this security group
3. Make note of the Group ID or name for reference

##### Step 2: Create Your Folder Structure

1. Your team should create any folders that require specific role based access controls or security policies
2. You have complete freedom to organise your folder structure as needed
3. The permissions will be automatically applied based on the role assignments
4. If you request a role that restricts access to a certain folder, only users who are members of the mapped security group will have access to it

#### Step 3: Request Role-Group Mapping

1. Contact Penwern support with:

   - The name of the security group you created
   - The specific access requirements (which workspaces, folders or files that should be accessible)
   - Any special conditions (e.g., "only accessible during business hours")

2. Penwern will:
   - Create a corresponding role in Curate
   - Map the security group to this Curate role
   - Apply appropriate ACLs and security policies to the requested resources

## Managing Changes

### Adding Users to the Executive Team

1. Simply add the user to the appropriate security group in your SSO provider
2. The SSO integration will automatically grant the user the corresponding role and access permissions in Curate

### Removing Users

1. Remove the user from the security group in your SSO provider
2. The user will no longer have access to the restricted content in Curate

### Modifying Access Permissions

If you need to change what the role can access:

1. Contact Penwern support with your requested changes
2. Specify which resources need modified permissions
3. Penwern will update the role permissions accordingly
4. Your team can then create, modify, or reorganise folders as needed

## Access Control Features

Curate offers several powerful access control features that can be implemented:

### Basic Permissions

- **Read**: Allows viewing files and folders
- **Write**: Allows modifying, uploading, and deleting files
- **Deny**: Explicitly prevents access regardless of other permissions

### Advanced Security Policies

Security policies can add dynamic conditions to access rights:

**Time-Based Access**

- Example: Allow access only during business hours

**Location-Based Access**

- Example: Restrict access to specific IP ranges

**File-Type Restrictions**

- Example: Prevent specific file types from being downloaded

**Granular Action Control**

- Deny Delete: Users can modify but not delete files
- Deny Download: Users can see files exist but cannot view contents
- Deny Upload: Users can read but not modify content

## Practical Examples

### Example 1: Executive Board Papers

- Create an "Executive Board" security group containing all executive members
- Create and organise any folder structure needed for executive resources
- Request a corresponding role in Curate with access to the appropriate resources
- Only members of the Executive Board group will see these folders

### Example 2: Department-Sensitive Documents

- Create department-specific security groups (e.g., "Finance Leadership")
- Your departments can create their own folder structures within their accessible workspaces
- Request a map to corresponding roles in Curate with your security requirements
- Each department will only see the folders in the workspaces their role has access to

## Best Practices

**Group Management**

- Keep Entra groups updated with current team members

**Folder Organization**

- Use consistent naming conventions for roles and folders
- Maintain a clear folder hierarchy that reflects your organisational structure

**Regular Reviews**

- Periodically review membership of sensitive groups
- Conduct access audits to ensure permissions remain appropriate

## Summary

- Create security groups in your SSO provider to organise users with similar access needs
- Penwern will create corresponding roles in Curate and map them to your groups
- Users will automatically receive appropriate access based on their group membership
- Special conditions can be applied to further restrict access when needed

## Support

For any assistance with role creation, mapping, or other access control concerns, please contact Penwern support.

## Frequently Asked Questions

### Q: How quickly are permission changes reflected in the system?

**A:** When you add or remove a user from a security group in your SSO provider, the changes typically take effect during their next login to Curate. For urgent changes, contact Penwern support.

### Q: What happens if a user belongs to multiple groups with conflicting permissions?

**A:** If the user belongs to one group that grants access and another that denies it, the deny permission always takes precedence.

### Q: How can we audit who has accessed sensitive files?

**A:** Curate maintains detailed audit logs of all file access. Contact Penwern support to request access reports for specific files or folders.

### Q: Can we create custom roles for our specific needs?

**A:** Yes, Penwern can create custom roles with precise permission sets tailored to your organizational requirements.
