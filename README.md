# 0x00. AirBnB clone - The console

# Description

The console is a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
It will enable us to:

-   create your data model
-   manage (create, update, destroy, etc) objects via a console / command interpreter
-   store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240305%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240305T181747Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5e420a9dcf75bef42b5a5b33450acfba5a684b953e1dc875e02636fa0cc864ea)

# How to start the console

1. Clone this repository.
2. Once the repository is cloned, change in to the repository and locate the `console.py`.
3. Run the file to open a shell in interactive mode:

```bash
~/AirBnB$ ./console.py
```

4. After running the file, a prompt should appear:

```bash
(hbnb)
```

5. Alternatively, you can also run the shell in non-interactive mode:

```bash
~/AirBnB$ echo "help" | ./console.py
```

# How to use the console

# Examples
