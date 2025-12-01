Why do we use default_factory when initializing a list field in a data class?

 - We use default_factory when initializing a list field because it allows the list to be newly generated each time a new class is initialized instead of sharing the class across objects.

What could go wrong if multiple students shared the same default list?

 - if multiple students shared the list, then there would only be one giant list of all of the classes everybody is taking and none of the classes would be specific to the student.

How does putting methods like enroll and total_courses inside the class help with code organization?

 - it allows us to cleanly add a class to a specific students schedule without confusion and also allows us to see how many classes a specific student is taking.