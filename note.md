# starting project airbnb.

## 11/06/2023

- start reading resources.
- make repository.
- add souad to calloboration in repo.
- make task 0, check pycode style, and task 3
- add `**kwargs` to `__init__` in class BaseModel
- add condition if else ...
- complete task 4.

## 11/07/2023

- start working on task 5 `make class FileStorage`
- I was working on filestorage `thanks for complete __init__.py `
- create basic console `Task 6`
- complete console `Task 7`

## information about classes

### BaseModel

```py
    in class basemodel we can :

    class BaseModel
        - create new object with:
            id : unique
            created_at: time create that object
            updated_at: time update that object

            - pass dict to make object by **kwargs.

        - __str__: return information about object
            format: [<class name>] (<self.id>) <self.__dict__>
        - to_dict : return dictionary
        - save: update attribute updated_at
```

### FilwStogare

```py
	class Filestorage:

	privet class attribute.
		- file_path = "file.json"
		- object = empty dict {}

	public class methods:
		- all: returns the dictionary __objects
		- new:  sets in __objects the obj with key <obj class name>.id
		- save: serializes __objects to the JSON file (path: __file_path)
		- reload: deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

```

### class HBNBCommand

```py
	class HBNBCommand

	public class attribute
		- prompte (str): "(hbnb) "

	public class methods
		- EOF : exit programe
		- quit : exit program
		- emptyline: shouldn’t execute anything

		- create: to Creates a new instance Usage:  `create BaseModel` it will give you your id.
    	- show: to  Prints the string representation of an instance based on the class name and id.
    			Usage: `show BaseModel <id>`.
    	- destroy: Deletes an instance based on the class name and id
    	    	Usage: ` destroy BaseModel <id>`
    	- all: Prints all string representation of all instances based or not on the class name.
    			Usage: `all BaseModel` or `all`.
    	- update: Updates an instance based on the class name and id by adding or updating attribute
    			Usage: `update BaseModel <id> email "aibnb@mail.com"`
```
