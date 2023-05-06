# Library App #

# Design Decisions: #

**Model Design:** The Book model was designed with fields such as title, author, publisher, publication date, ISBN, and category. The primary key was set to the auto-incrementing id field provided by Django and was named 'book_id'. This model was used to represent book objects in the database.

**View Design:** The views were designed to handle different HTTP requests such as GET, POST, and DELETE. Each view performs a specific task such as adding, updating, deleting, searching, and displaying book records. The views also make use of `request.POST.get()` and client-side validation to ensure that only valid data is entered into the database.

**Template Design:** The templates were designed using Bootstrap CSS framework to make the application look visually appealing. The layout.html file was used to define the base structure of all the other templates. The templates were designed to be reusable by using template inheritance to extend the base.html file. Bootstrap Navbar and buttons were used.

**Delete Page:** To ensure that user is 100% sure that he/she wants to delete a book a separate page was given to ensure that they can check all the details before deleting. The fields in the form are given attribute `readonly` to ensure the user can't change fields.

# Challenges Faced: #

**Pagination**: Implementing pagination was a bit challenging as it required some extra logic to split the results into pages and display them accordingly. Django's built-in pagination feature was used to implement this. As this was a library app the results per page were limited to 10 results per page.

**Search Functionality**: Implementing the search functionality required some extra work as it involved filtering the results based on the user's input. The Q object was used to construct complex queries based on user input.

**Form Validation**: Ensuring that only valid data is entered into the database was challenging. As the inputs were limited to title, author, publisher, publication date, ISBN, and category so only client-side validation was done to ensure correct user input. In the forms these fields were set as required. Title, author, publisher and category were set as text based fields in the form. Publication date was set as date field in the form and lastly isbn was set as a number. This ensured no server-side validation was needed for all fields except *isbn* as the user was restricted to enter only correct form of inputs like text, number and date. As two books can have same title, publisher, publication date and category there was no need of checking for existing records. But as isbn of two books cannot be the same server-side validation was done.

*To run the app make migrations first*
*To test the app please start adding books*

**Overall, the development of the library application was a great learning experience. It helped me to learn more about Django and its built-in features for handling forms, templates, and database operations.**