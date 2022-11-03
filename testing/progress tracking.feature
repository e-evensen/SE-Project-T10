Feature: Progress tracking
    Scenario: 
        Given the user is part of a project,
        When at least one task is completed,
        Then users can track the percentage of the overall project is complete/remaining.

    Example:
        def progressTracker(tasks_complete, total_tasks):
            progress = tasks_complete/total_tasks
            return progress

        The view of this would be a progress bar, as well as the percentage displayed.