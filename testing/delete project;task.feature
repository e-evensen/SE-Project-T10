Feature: Delete a Project/Task
    Scenario: Deleting a project or task, for any given reason.
    Given the user is a project manager,
    When the user clicks on “Delete Project” or “Delete Task”
    Then the user can delete projects or tasks.

Rule: Only the project manager can delete projects

Example:
    Given there is a project with 3 members, 1 managers and 2 regular members
    And 2 of the members try to delete the project
    Then they can not, since they do not have manager permissions.
        If (member.isManager == true)
            Deletes Project
        Else
            Pop Up that denies deletion

Rule: Project Manager can give permissions to members to delete Tasks.

    Example:
    Given there is a project with 3 members, a project manager and 2 members
    Then one of the members want to delete a task
    And the only can if they have task deletion permissions granted by the manager.
        If (member.taskAssignment == true)
            Deletes Task