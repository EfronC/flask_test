# GoGrow - Python (Flask) Code Test

The purpose of this exercise is to give you a chance to demonstrate your
problem solving and coding skills. The exercise is split into two sections:
first you will complete the tasks below at home; if you are successful in the
first part, you will be invited in for an interview where we will discuss your
solution and try to add to it. This is primarily a web development exercise so we
can see how you deal with REST API's and data modeling; bear that in
mind when completing the exercise.

## The tasks

This exercise is intended to be a REST API built using Python and Flask.

The requirements are:

- Create a Flask project from scratch
- Set up a database
- Create a Person model with `fullname`, `gender` and `ethnicity` string attributes
- Create an endpoint to get all persons
  - E.g. `GET /persons`
  - Return the data stored in the database
- Create an endpoint to look for a specific person by `fullname`
  - E.g. `GET /persons/juan`
  - Return the record in the database if exists; consume `https://api.diversitydata.io` otherwise.
    - E.g. `GET https://api.diversitydata.io/?fullname=juan%20jose%20perez`

## What we are looking for

- Good understanding of REST API's
- Good understanding of OOP principles
- Bonus: A detailed git commit log to show the refactoring process you went through