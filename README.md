# IN DEVEL: NOTHING is working AT 04/30/17
==========================================

# Installation

```sh
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

### create(title, text, type)

Return a [pasta_object](#pasta_object)

## Constants:

### Paste type:

- ```SELF_BURNING```
- ```EDITABLE```
- ```STANDARD```

Side note: URL_SHORTENER is not supported yet.

## Classes

### pasta_object

##### Any ortographic help is welcome. I'm french. I speak english like an albinos unicorn.