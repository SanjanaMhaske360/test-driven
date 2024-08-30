# features/products.feature

Feature: Product Management

  Scenario: Reading a Product
    Given the following products:
      | name        | description         | price | available |
      | Example Product | A product for testing | 19.99 | True     |
    When I request the product with name "Example Product"
    Then the response should be successful
    And the response should contain the product details:
      | name        | description         | price | available |
      | Example Product | A product for testing | 19.99 | True     |
