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
