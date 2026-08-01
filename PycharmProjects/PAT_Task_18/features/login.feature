Feature: Login functionality with Excel data

  Scenario: Login with credentials from Excel
    When I open the Guvi Homepage
    And I read login data from Excel
    Then Validate Username and Password input boxes
    And Validate Submit button working or not
    And I perform login tests for each row