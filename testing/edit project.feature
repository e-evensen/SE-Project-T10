Feature: Edit a Project
    Scenario: 
Given the user is within a project,
When the user selects “edit”,
Then the user is granted the ability to add, delete, and modify tasks.
Example:
    def editProject(a_user):
        If (a_user == manager || a_user == whitelisted):
            continue
        [various onClick() event handlers for adding tasks “+”, deleting tasks “x”, etc]