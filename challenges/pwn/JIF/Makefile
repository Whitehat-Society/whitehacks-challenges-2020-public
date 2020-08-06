#OBJS specifies which files to compile as part of the project
OBJS = main.c

#OBJ_NAME specifies the name of our exectuable
OBJ_NAME = jifviewer

#This is the target that compiles our executable
all : $(OBJS)
	gcc $(OBJS) -lSDL2 -o $(OBJ_NAME) -fno-stack-protector -g
