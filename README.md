# kotlin-flask-todo-app
A 'todo' app implemented in Kotlin utilising a Python Flask framework backend API to store data.

# Back-end
Flask app with routes to add, delete and assign completed todo items from database.

Sqlite3 database for to do items.

# Front-end
Composed of 2 Kotlin classes: 

1) MainActivity = the root entry point to the app.

2) Todo = data class - purely holds app data about if a todo item is checked or not.

3) TodoAdapter = holds fundamental logic for app - its constructor holds a mutble list of user-supplied todos from the 'Todo' class aforementioned.

Dependency to the build.gradle file in Kotlin to connect to the Flask database.

Main functions are 'deleteDoneTodos' and 'addTodos'.

Simple testing in jUnit.

# UI/UX
Simple interface in alignment with the Android colour system rule for accesibility.

Clearly highlighted areas of where user should input data and buttons to add inputs to the Flask database.

Checkboxes have to be clicked in order to delete the respective items.

Strikethrough flags implemented a constants when user clicks checkbox.

Utilises 'recycler view' to efficiently show large sets of data (todos) on the screen and if needed, scrollable behaviour.



