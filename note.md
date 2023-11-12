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
- Create class User that inherits from BaseModel
- Fix error in class BaseModel updated_at created_at most be datetime not string
- add documents to class User

## 11/08/2023

- Update FileStorage to manage correctly serialization and deserialization of User. in `method reload`
- Update command interpreter (console.py) to allow show, create, destroy, update and all used with User.
- change in methods command in console `delete for LOOP` no need to check id or name class `method Printerr` do that
- check pycodestyle

## 11/09/2023

- add all classses `State City Amenity Place Review` complete task 8.
- remove the old code which had a comment by #
- Update FileStorage to manage correctly serialization and deserialization of all our new classes:
  Place, State, City, Amenity and Review
- Update your command interpreter (console.py) to allow those actions:
  show, create, destroy, update and all with all classes created previously.
- We currently have console version 1.0, `i like that :D`
- check pycodestyle
- i will start Unittest

## 11/10/2023

- testing Classes ...
- add task 11 `<class name>.all()`
- add task 12 `<class name>.count()`
- adding task 13, 14 `<class name>.show(id)` `<class name>.destroy(id)`
- update default method

## 11/11/2023

- check all task `start fixe code`
- add test models.
- working on pass dictionary at update command.

## 11/12/2023

- try fix error on task 5.
- start testing my console.
- help command

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
    			Usage: `update BaseModel <id> email "aibnb@mail.com"
		- checktype: a function that check type of value.
		- Printerr: a function that check if samething is missing and print error
```

### class User

```py
	Public class attributes:
		email: string - empty string
		password: string - empty string
		first_name: string - empty string
		last_name: string - empty string
```

### class State

```py
	Public class attributes:
		name: string - empty string
```

### class City

```py
	Public class attributes:
		state_id: string - empty string: it will be the State.id
		name: string - empty string
```

### class Amenity

```py
	Public class attributes:
		name: string - empty string
```

### class Place

```py
	Public class attributes:
		city_id: string - empty string: it will be the City.id
		user_id: string - empty string: it will be the User.id
		name: string - empty string
		description: string - empty string
		number_rooms: integer - 0
		number_bathrooms: integer - 0
		max_guest: integer - 0
		price_by_night: integer - 0
		latitude: float - 0.0
		longitude: float - 0.0
		amenity_ids: list of string - empty list: it will be the list of Amenity.id later
```

#### class Review

```py
	Public class attributes:
		place_id: string - empty string: it will be the Place.id
		user_id: string - empty string: it will be the User.id
		text: string - empty string
```
