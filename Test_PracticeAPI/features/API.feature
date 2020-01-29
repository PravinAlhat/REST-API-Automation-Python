Feature: To verify various Rest API method
  Scenario: To verify Get method of Rest API
    Given API url is provided for get
    When User executes get method
    Then User checks the response code for get

  Scenario: To verify Put method of Rest API
    Given API url is provided for put
    When User executes Put method
    Then User checks the response code for put

  Scenario: To verify Post method of Rest API
    Given API url is provided for post
    When User executes Post method
    Then User checks the response code for post

  Scenario: To verify Delete method of Rest API
    Given API url is provided for delete
    When User executes Delete method
    Then User checks the response code for delete
