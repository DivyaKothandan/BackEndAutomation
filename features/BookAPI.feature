Feature: Verify if Books are added using Library API
  @smoke
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And  status code of response should be 201

#   @library
#    Scenario Outline: Verify AddBook API functionality
#    Given the Book details with <bookId> and <customerName>
#    When we execute the AddBook PostAPI method
#    Then book is successfully added
#      Examples:
#        |bookId  |  customerName |
#        | 1| John   |
#        | 5 | Henry  |
#        | 6 | Smith  |




