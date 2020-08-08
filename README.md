# Testing in Django
Automated testing is an extremely useful bug-killing tool for the modern Web developer. You can use a collection of tests – a test suite – to solve, or avoid, a number of problems:

When you’re writing new code, you can use tests to validate your code works as expected.

When you’re refactoring or modifying old code, you can use tests to ensure your changes haven’t affected your application’s behavior unexpectedly.

Required installations

Python 3.6
Django 1.11 ('pip install django<2')
Selenium ('pip install selenium')

=Checking it all works
  (env) $ pyhton
  Python 3.6.X
  >>> import Django
  >>> print( django.get_version() )
  1.11.x
  >>> from selenium import webdriver
  >>> browser = webdriver.Firefox()
  >>> browser.get("http://www.google.com")
  >>> print(browser.title)
  Google
  >>> browser.quit()
