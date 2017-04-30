# IN DEVEL: NOTHING is working AT 04/30/17
==========================================

# Installation

___You need to have ```requests``` installed on your system, for your specific version of python.___


```sh
pip install requests
git clone https://github.com/camilleeyries/pasta.cf-python-API.git
```

Now move pastacfapi.py to the root file of your project ( or somewhere in your $PYTHONPATH )

# Usage

### To import: ( pastacfapi.py need to be in the same folder of the root file.)

```py
import pastacfapi
```

### To create a new paste:

```py
pastacfapi.create(paste_title, paste_text, paste_type)
```

# Exemples:

```py
import pastacfapi

paste = pastacfapi.create("PASTA-CF-API", "Wow, this API is really great, thanks to Camille Eyriès, <3", pastacfapi.SELF_BURNING)

print("Paste url is: " + paste.url)
```

# Documentations

## Functions:

- create(title, text, type)
-
Return a [pasta_object](https://github.com/camilleeyries/pasta.cf-python-API#pasta_object)

## Constants:

### Paste type:

- ```SELF_BURNING```
- ```EDITABLE```
- ```STANDARD```

Side note: URL_SHORTENER is not supported yet.

## Classes

### pasta_object

- pasta['token']
-
The token of your pasta e.g: ```papa-sampling-random```

- pasta['view']
-
It's the standard user GUI url to see the pasta you just created.

- pasta['raw']
-
It's the raw GUI of your pasta, without fireworks.

- pasta['password']
-
It's the password of the paste you just created, if it's type is ```EDITABLE```

- pasta['type']
-
It's the type of the paste you just created (again!), if you forgot what is was.


# TODO:
##### Any ortographic help is welcome. I'm french. I speak english like an albinos unicorn.
##### Implement error handling. Please, someone, do that for me, because I don't know how to do it, really :(
##### Add commentaries (?) to the source code, because I'm bit lazy tonight.
##### Format this ugly README.md, I would accept every commit about that

# Contributors:

- Camille Eyriès
- You ?
