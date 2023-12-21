# django_5_playground
Django 5 Playground

Exploring Django5 features and testing enhancements to use accross other applications.

# Notes:
20-Dec-23:
 - went through the normal flow of [creating a custom user model](https://testdriven.io/blog/django-custom-user-model/). 
   - No issues.

#### Generated Fields
 - [Testing generated fields](https://www.paulox.net/2023/11/07/database-generated-columns-part-1-django-and-sqlite/) with Decimal Fields
   - No issues
 - Testing generated fields with jsonb fields
   - Suprisingly no issues. Surprised here because aggregating jsonb in postgress is typically quite the hassle as postgress does not support a Sum function on jsonb fields. Th DB used here is sqlite so interested in seeing what happens when testing with pg. Quite the find here.