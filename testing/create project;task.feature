Feature: Create a Project/Task
    Scenario: A project manager creates a new project
        Given I am a project manager who wants to create a new project
        When I click on “create project”
            And I enter the project name
            And I enter the project description
        Then a new project is created