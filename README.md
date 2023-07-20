# Object Relations Code Challenge - Flatflix

For this challenge, we'll be working with a Movie Review domain, like Netflix.

We have three models: `Viewer`, `Movie`, and `Review`.

A `Movie` has many `Review`s. A `Viewer` has many `Review`s. A `Review` belongs
to a `Viewer` and belongs to a `Movie`.

`Viewer` - `Movie` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge is test-driven. You can run `pytest` at any
time to check your work.
You'll need to create your own sample instances so that you can try out your
code on your own. Make sure your relationships and methods work in the console
before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Movie

- `Movie __init__(self, title)`
  - `Movie` is initialized with a title (string).
  - Title **can be** changed after the `Movie` is initialized.
- `Movie property title()`
  - Returns the `Movie`'s title.
  - Titles must be strings greater than 0 characters.
  - `raise Exception` if validation fails.
- `Movie class attribute all`
  - Stores a list of all movies.

#### Viewer

- `Viewer __init__(self, username)`
  - `Viewer` is initialized with a username (string)
  - Usernames **can be** changed after the Viewer is initialized
- `Viewer property username()`
  - Returns the Viewer's username
  - Usernames must be strings between 6 and 16 characters,
    inclusive
  - `raise Exception` if validation fails
  - _Stretch goal: usernames must be unique_
- `Viewer class attribute all`
  - Stores a list of all viewers.

#### Review

- `Review __init__(self, viewer, movie, rating)`
  - `Review` is initialized with a `Viewer` instance, a `Movie` instance, and a
    rating (number)
  - Instantiating a review should add it to its `viewer`'s `review`s
  - Instantiating a review should add it to its `movie`'s `reviews`
- `Review property rating()`
  - Returns the rating for the `Review` instance
  - Ratings must be integers between 1 and 5, inclusive
  - `raise Exception` if validation fails
- `Review class attribute all`
  - Stores a list of all reviews.

### Object Relationship Attributes and Properties

#### Review

- `Review property viewer()`
  - Returns the viewer who wrote the review.
  - Viewers must be `Viewer` instances.
  - `raise Exception` if validation fails.
- `Review property movie()`
  - Returns the movie that is being reviewed.
  - Movies must be `Movie` instances.
  - `raise Exception` if validation fails.
- _Stretch goal: only the most recent review should persist for each viewer._

#### Viewer

- `Viewer reviews(self)`
  - Returns a list of `Review` instances associated with the `Viewer` instance.
- `Viewer reviewed_movies(self)`
  - Returns a list of `Movie` instances reviewed by the `Viewer` instance.

#### Movie

- `Movie reviews(self)`
  - Returns a list of all the `Review` instances for the `Movie`.
- `Movie reviewers(self)`
  - Returns a list of all of the `Viewer` instances that reviewed the `Movie`.

### Aggregate and Association Methods

#### Viewer

- `Viewer has_reviewed_movie(self, movie)`
  - Returns `True` if the `Viewer` has reviewed this `Movie` (if there is a
    `Review` instance that has this `Viewer` and `Movie`), returns `False`
    otherwise

#### Movie

- `Movie average_rating(self)`
  - Returns the average of all ratings for the `Movie` instance
  - To average ratings, add all ratings together and divide by the total number
    of ratings.
- `Movie classmethod highest_rated(cls)`
  - Returns the `Movie` instance with the highest average rating.
