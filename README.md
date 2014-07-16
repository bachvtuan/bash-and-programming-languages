bash-and-programming-languages
==============================

A simple game to call some programming languages to run that program code by using bash enviroment.

## Game rule:
You can write any programming language to run on bash with follow syntax:

```
program_name Your Full Name
```
### Result


```
Hello: Your Full Name
You're running on bash by using {Programming Language Name} {It 's version}
You're on {OS Name} { Release Version }
```

### Extra rules:
You also can install or remove it.

I wrote 3 files corresponding 3 programing languages consist javascript ( js_program.js), python(python_program.py), php(php_program.php).
### To install any program code

```
./manage install php|python|js
```

**Example**

```
./manage install php
```

### Usage
I assume you installed php before

And now, you can run php program by command

```
 php_program Your Full Name
```

**Below is my result:**
```
bvtuan@bvtuan:~$ php_program Tuan Bach Van
Hello: Tuan Bach Van
You're running on bash by using PHP 5.5.9-1ubuntu4.3
You're on Linux 3.13.0-30-generic
```

### To remove installed program
```
./manage remove php|python|js
```

**Example**

```
./manage remove php
```


### Extension

You can write on other programming language such as Ruby, Java, Go, Perl, C, etc.

