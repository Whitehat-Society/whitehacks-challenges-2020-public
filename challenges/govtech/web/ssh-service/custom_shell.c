#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h> // Used for cmd_date
#include <grp.h> // Used to retrieve group related info
#include <sys/types.h> // Used for gid, uid
#include <limits.h>

#define NUM_GROUPS_MAX 10 // Maximum number of groups to be display for cmd_userinfo()
/*
  Function Declarations for builtin shell commands:
 */
int cmd_help(char **args);
int cmd_list(char **args);
int cmd_print(char **args);
int cmd_exit(char **args);
void cshell_intro();
/*
  List of builtin commands, followed by their corresponding functions.
 */
char *builtin_str[] = {
  "help",
  "list",
  "print",
  "exit",
};


int (*builtin_func[]) (char **) = {
  &cmd_help,
  &cmd_list,
  &cmd_print,
  &cmd_exit,
};

int cmd_num_builtins() {
  return sizeof(builtin_str) / sizeof(char *);
}

/*
  Builtin function implementations.
*/

/**
   @brief - Introduction to CustomShell
   @param - n/a
   @return Alawys returns 1, to continue executing
*/

void cshell_intro()
{
  printf("======= A VERY SIMPLE CUSTOM SHELL =======\n");
  printf("Type 'help' to get a list of allowed commands\n");
  printf("==========================================\n");

}

int cmd_list(char **args)
{
  if (args[1] == NULL)
    system("ls -la");
  else {
        char ls[100];
        for (int i = 0, j; args[1][i] != '\0'; ++i) {
            // enter the loop if the character is not an alphabet
            // not the null character and '.'
            while (!(args[1][i] >= 'a' && args[1][i] <= 'z') && !(args[1][i] >= 'A' && args[1][i] <= 'Z') && !(args[1][i] == '\0') && !(args[1][i] == '.')) {
                for (j = i; args[1][j] != '\0'; ++j) {
                // if jth element of line is not an alphabet,
                // assign the value of (j+1)th element to the jth element
                args[1][j] = args[1][j + 1];
                }
                args[1][j] = '\0';
            }
        }
        sprintf(ls, "ls -la %s",args[1]);
        system(ls);
  }
  return 1;
}

int cmd_print(char **args)
{
  if (args[1] == NULL)
    fprintf(stderr, "Oppss: unexpected argument to \"print\"\n");
  else {

      char cat[100];
      for (int i = 0, j; args[1][i] != '\0'; ++i) {
            // enter the loop if the character is not an alphabet
            // and not the null character
            while (!(args[1][i] >= 'a' && args[1][i] <= 'z') && !(args[1][i] >= 'A' && args[1][i] <= 'Z') && !(args[1][i] == '\0') && !(args[1][i] == '.') && !(args[1][i] == '/')) {
                for (j = i; args[1][j] != '\0'; ++j) {

                // if jth element of line is not an alphabet,
                // assign the value of (j+1)th element to the jth element
                args[1][j] = args[1][j + 1];
                }
                args[1][j] = '\0';
            }
        }
      sprintf(cat, "cat %s",args[1]);
      system(cat);
  }
  return 1;
}

/**
   @brief Builtin command: print help.
   @param args List of args.  Not examined.
   @return Always returns 1, to continue executing.
 */
int cmd_help(char **args)
{
  int i;
  printf("\n======= HELP SECTION =======\n");
  printf("These are the following commands that can be used by this CustomShell\n");

  for (i = 0; i < cmd_num_builtins(); i++) {
    printf("  %s\n", builtin_str[i]);
  }
  printf("======= HELP SECTION =======\n");
  return 1;
}

/**
   @brief Builtin command: exit.
   @param args List of args.  Not examined.
   @return Always returns 0, to terminate execution.
 */
int cmd_exit(char **args)
{
  return 0;
}

/**
   @brief Execute shell built-in or launch program.
   @param args Null terminated list of arguments.
   @return 1 if the shell should continue running, 0 if it should terminate
 */
int cshell_execute(char **args)
{
  int i;

  if (args[0] == NULL) {
    // An empty command was entered.
    return 1;
  }

  for (i = 0; i < cmd_num_builtins(); i++) {
    if (strcmp(args[0], builtin_str[i]) == 0) {
      return (*builtin_func[i])(args);
    }
  }
  fprintf(stderr, "Oppss: invalid command\n");
}

#define CSHELL_RL_BUFSIZE 1024
/**
   @brief Read a line of input from stdin.
   @return The line from stdin.
 */
char *cshell_read_line(void)
{
  int bufsize = CSHELL_RL_BUFSIZE;
  int position = 0;
  char *buffer = malloc(sizeof(char) * bufsize);
  int c;

	// Error check for memory allocation
  if (!buffer) {
    fprintf(stderr, "Oppss: allocation error\n");
    exit(EXIT_FAILURE);
  }

  while (1) {
    // Read a character
    c = getchar();

    // If we hit EOF, replace it with a null character and return.
    if (c == EOF || c == '\n') {
      buffer[position] = '\0';
      return buffer;
    } else {
      buffer[position] = c;
    }
    position++;

    // If we have exceeded the buffer, reallocate.
    if (position >= bufsize) {
      bufsize += CSHELL_RL_BUFSIZE;
      buffer = realloc(buffer, bufsize);
      if (!buffer) {
        fprintf(stderr, "Oppss: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }
  }
}

#define CSHELL_TOK_BUFSIZE 64
#define CSHELL_TOK_DELIM " \t\r\n\a"
/**
   @brief Split a line into tokens (very naively).
   @param line The line.
   @return Null-terminated array of tokens.
 */
char **cshell_split_line(char *line)
{
  int bufsize = CSHELL_TOK_BUFSIZE, position = 0;
  char **tokens = malloc(bufsize * sizeof(char*));
  char *token;

	// Error check for token allocation
  if (!tokens) {
    fprintf(stderr, "Oppss: allocation error\n");
    exit(EXIT_FAILURE);
  }

  token = strtok(line, CSHELL_TOK_DELIM);
  while (token != NULL) {
    tokens[position] = token;
    position++;

    if (position >= bufsize) {
      bufsize += CSHELL_TOK_BUFSIZE;
      tokens = realloc(tokens, bufsize * sizeof(char*));
	    
      if (!tokens) {
        fprintf(stderr, "Oppss: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }

    token = strtok(NULL, CSHELL_TOK_DELIM);
  }
  tokens[position] = NULL;
  return tokens;
}

/**
   @brief Loop getting input and executing it.
 */
void cshell_loop(void)
{
  char *line;
  char **args;
  int status;

  do {
    printf("A very simple custom shell> ");
    line = cshell_read_line();
    args = cshell_split_line(line);
    status = cshell_execute(args);

    free(line);
    free(args);
  } while (status);
}

/**
   @brief Main entry point.
   @param argc Argument count.
   @param argv Argument vector.
   @return status code
 */
int main(int argc, char **argv)
{
  // Run command loop.
  system("clear");
  cshell_intro();
  cshell_loop();

  // Perform any shutdown/cleanup.

  return EXIT_SUCCESS;
}