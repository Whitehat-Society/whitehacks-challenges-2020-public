#include <curses.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define REG_L 9
#define REG_C 54

#define STK_L 15
#define STK_C 54

#define DIS_L 24
#define DIS_C 64

#define RES_L 5
#define RES_C 50

/* gcc main.c -lncurses -o bofschool */

int main(){
	alarm(120);

	WINDOW * mainwin, 
		   * regwin,
		   * stkwin,
		   * diswin,
		   * arrwin,
		   * inwin;

	int ch = 0;
	unsigned char buf[300];
	unsigned char buf_in[300];
	int len = 0;
	int len_in = 0;
	memset(buf, '\x00', 300);
	memset(buf_in, '\x00', 300);
	/* init buf */
	memcpy(buf, "\xa0\x05@\x00\x00\x00\x00\x00p\x04@\x00\x00\x00\x00\x00\x00\xd8\xff\xff\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x05@\x00\x00\x00\x00\x000\xd8\xa2\xf7\xff\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xd8\xff\xff\xff\x7f\x00\x00\xa0\xcc\xff\xf7\x01\x00\x00\x00w\x05@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 88);

	/* init */
	if( (mainwin = initscr()) == NULL ){
		fprintf(stderr, "[-] Error initialising ncurses.\n");
		exit(EXIT_FAILURE);
	}
	if(has_colors() == FALSE){
		endwin();
		printf("Your terminal does not support color\n");
		exit(EXIT_FAILURE);
	}
	start_color();
	init_pair(1, COLOR_RED, COLOR_BLACK);
	init_pair(2, COLOR_BLUE, COLOR_BLACK);
	init_pair(3, COLOR_YELLOW, COLOR_BLACK);
	cbreak();	
	noecho();

	/* create sub-windows */
	regwin = subwin(mainwin, REG_L, REG_C, STK_L, 0);
	stkwin = subwin(mainwin, STK_L, STK_C, 0, 0);
	diswin = subwin(mainwin, DIS_L, DIS_C, 0, STK_C);
	inwin  = subwin(mainwin, 3, STK_C+DIS_C, DIS_L, 0);

	/* reg tings */
	char reg_names[5][25]= {
		"rip:  0x000000000040058b",
		"rsp:  0x00007fffffffd770",
		"rbp:  0x00007fffffffd790",
		"rdi:  0x00007fffffffd770",
		"rax:  0x00007fffffffd770"
	};
	for(int i = 0; i < 5; i++)
		mvwaddstr(regwin, 2+i, 2, reg_names[i]);

	/* stk tings */
	char stk[] = "  0x00007fffffffd770|+0x00: 00 00 00 00 00 40 05 a0\n\
  0x00007fffffffd778|+0x08: 00 00 00 00 00 40 04 70\n\
  0x00007fffffffd780|+0x10: 00 00 7f ff ff ff d8 70\n\
  0x00007fffffffd788|+0x18: 00 00 00 00 00 00 00 00\n\
  0x00007fffffffd790|+0x20: 00 00 00 00 00 40 05 a0\n\
  0x00007fffffffd798|+0x28: 00 00 7f ff f7 a2 d8 30\n\
  0x00007fffffffd7a0|+0x30: 00 00 00 00 00 00 00 01\n\
  0x00007fffffffd7a8|+0x38: 00 00 7f ff ff ff d8 78\n\
  0x00007fffffffd7b0|+0x40: 00 00 00 01 f7 ff cc a0\n\
  0x00007fffffffd7b8|+0x48: 00 00 00 00 00 40 05 77\n\
  0x00007fffffffd7c0|+0x50: 00 00 00 00 00 00 00 00";

	mvwaddstr(stkwin, 2, 0, stk);

	/* dis tings */
	char dis[] = "win:\n\
   0x0000000000400566 <+0> :	push   rbp\n\
   0x0000000000400567 <+1> :	mov    rbp,rsp\n\
   0x000000000040056a <+4> :	mov    edi,0x601060 <flag>\n\
   0x000000000040056f <+9> :	call   0x400430 <puts@plt>\n\
   0x0000000000400574 <+14>:	nop\n\
   0x0000000000400575 <+15>:	pop    rbp\n\
   0x0000000000400576 <+16>:	ret    \n\
\n\
  main:\n\
   0x0000000000400577 <+0> :	push   rbp\n\
   0x0000000000400578 <+1> :	mov    rbp,rsp\n\
   0x000000000040057b <+4> :	sub    rsp,0x20\n\
   0x000000000040057f <+8> :	lea    rax,[rbp-0x20]\n\
   0x0000000000400583 <+12>:	mov    rdi,rax\n\
   0x0000000000400586 <+15>:	mov    eax,0x0\n\
   0x000000000040058b <+20>:	call   0x400450 <gets@plt>\n\
   0x0000000000400590 <+25>:	mov    eax,0x0\n\
   0x0000000000400595 <+30>:	leave\n\
   0x0000000000400596 <+31>:	ret    ";
	mvwaddstr(diswin, 2, 2, dis);

	/* no more arrows
	wattron(diswin, COLOR_PAIR(2));
	mvwaddstr(diswin, 18, DIS_C-4, "<=");
	wattroff(diswin, COLOR_PAIR(2));
	*/
	wattron(diswin, COLOR_PAIR(2));
	mvwaddstr(diswin, 18, 3, "0x000000000040058b <+20>:    call   0x400450 <gets@plt>");
	wattroff(diswin, COLOR_PAIR(2));

	/* titles and boxes */
	box(regwin, 0, 0);
	box(stkwin, 0, 0);
	box(diswin, 0, 0);
	box(inwin, 0, 0);
	mvwaddstr(regwin, 0, 1, " Registers ");
	mvwaddstr(stkwin, 0, 1, " Stack ");
	mvwaddstr(diswin, 0, 1, " Disassembly ");
	mvwaddstr(inwin, 0, 1, " Input ");
	refresh();

	/* input loop */
	nodelay(stdscr, TRUE);
	int rc;
	while(ch != 'q'){
		/* handle kp */
		if((ch = getch()) == ERR){
		}
		/* finish routine */
		else if(ch == '\n'){
			unsigned long long int rip, rsp, rbp, rdi, rax;
			char reg[100];
			bool w = false;

			wattron(regwin, COLOR_PAIR(1));
			
			/* no more arrows
			wattron(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 18, DIS_C-4, "  ");
			mvwaddstr(diswin, 19, DIS_C-4, "<=");
			wrefresh(diswin);
			*/
			wattroff(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 18, 3, "0x000000000040058b <+20>:    call   0x400450 <gets@plt>");
			wattron(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 19, 3, "0x0000000000400590 <+25>:    mov    eax,0x0");
			wrefresh(diswin);
			mvwaddstr(regwin, 2, 2, "rip:  0x0000000000400590");	
			mvwaddstr(regwin, 6, 2, "rax:  0x0000000000000000");	
			wrefresh(regwin);
			sleep(1);

			/* no more arrows
			mvwaddstr(diswin, 19, DIS_C-4, "  ");
			mvwaddstr(diswin, 20, DIS_C-4, "<=");
			wrefresh(diswin);
			*/
			wattroff(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 19, 3, "0x0000000000400590 <+25>:    mov    eax,0x0");
			wattron(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 20, 3, "0x0000000000400595 <+30>:    leave");
			wrefresh(diswin);
			mvwaddstr(regwin, 2, 2, "rip:  0x0000000000400595");	
			mvwaddstr(regwin, 3, 2, "rsp:  0x00007fffffffd798");	
			rsp = 0x00007fffffffd798;
			rbp = *((unsigned long long int *)&buf[0x20]);
			sprintf(reg, "rbp:  0x%016llx", rbp);
			mvwaddstr(regwin, 4, 2, reg);
			wrefresh(regwin);
			sleep(1);

			/* no more arrows
			mvwaddstr(diswin, 20, DIS_C-4, "  ");
			mvwaddstr(diswin, 21, DIS_C-4, "<=");
			wrefresh(diswin);
			*/
			wattroff(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 20, 3, "0x0000000000400595 <+30>:    leave");
			wattron(diswin, COLOR_PAIR(2));
			mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
			wrefresh(diswin);
			rip = *((unsigned long long int *)&buf[0x28]);
			sprintf(reg, "rip:  0x%016llx", rip);
			mvwaddstr(regwin, 2, 2, reg);	
			wrefresh(regwin);
			sleep(1);

			/* rip unchanged */
			if(rip == 0x0000007ffff7a2d8){
				wattroff(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
				wrefresh(diswin);
				WINDOW *reswin = subwin(mainwin, RES_L, RES_C, STK_L/2, STK_C/2);
				wattron(reswin, COLOR_PAIR(3));
				wclear(reswin);
				box(reswin, 0, 0);
				mvwaddstr(reswin, 0, 1, " Result ");
				mvwaddstr(reswin, 2, 2, "Program exited safely.");
				mvwaddstr(reswin, 3, 2, "Try to hack me!");
				wrefresh(reswin);
				sleep(10);
				endwin();
				exit(0);
			}

			/* rip within win */
			if(rip == 0x0000000000400566){
				w = true;
				/* no more arrows
				mvwaddstr(diswin, 21, DIS_C-4, "  ");
				mvwaddstr(diswin, 3, DIS_C-4, "<=");
				wrefresh(diswin);
				*/
				wattroff(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
				wattron(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin,  3, 3, "0x0000000000400566 <+0> :	push   rbp");
				wrefresh(diswin);
				rip = 0x0000000000400567;
				sleep(1);
			}
			if(rip == 0x0000000000400567){
				w = true;
				/* no more arrows
				mvwaddstr(diswin, 21, DIS_C-4, "  ");
				mvwaddstr(diswin, 3, DIS_C-4, "  ");
				mvwaddstr(diswin, 4, DIS_C-4, "<=");
				wrefresh(diswin);
				*/
				wattroff(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
				mvwaddstr(diswin,  3, 3, "0x0000000000400566 <+0> :	push   rbp");
				wattron(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin,  4, 3, "0x0000000000400567 <+1> :	mov    rbp,rsp");
				wrefresh(diswin);
				rbp = rsp;
				sprintf(reg, "rbp:  0x%016llx", rbp);
				mvwaddstr(regwin, 4, 2, reg);	
				wrefresh(regwin);
				rip = 0x000000000040056a;
				sleep(1);
			}
			if(rip == 0x000000000040056a){
				w = true;
				/* no more arrows
				mvwaddstr(diswin, 21, DIS_C-4, "  ");
				mvwaddstr(diswin, 4, DIS_C-4, "  ");
				mvwaddstr(diswin, 5, DIS_C-4, "<=");
				wrefresh(diswin);
				*/
				wattroff(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
				mvwaddstr(diswin,  4, 3, "0x0000000000400567 <+1> :	mov    rbp,rsp");
				wattron(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin,  5, 3, "0x000000000040056a <+4> :	mov    edi,0x601060 <flag>");
				wrefresh(diswin);
				rdi = 0x601060;
				sprintf(reg, "rdi:  0x%016llx", rdi);
				mvwaddstr(regwin, 5, 2, reg);	
				wrefresh(regwin);
				rip = 0x000000000040056f;
				sleep(1);
			}
			if(rip == 0x000000000040056f){
				/* no more arrows
				mvwaddstr(diswin, 21, DIS_C-4, "  ");
				mvwaddstr(diswin, 5, DIS_C-4, "  ");
				mvwaddstr(diswin, 6, DIS_C-4, "<=");
				wrefresh(diswin);
				*/
				wattroff(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin, 21, 3, "0x0000000000400596 <+31>:    ret");
				mvwaddstr(diswin,  5, 3, "0x000000000040056a <+4> :	mov    edi,0x601060 <flag>");
				wattron(diswin, COLOR_PAIR(2));
				mvwaddstr(diswin,  6, 3, "0x000000000040056f <+9> :	call   0x400430 <puts@plt>");
				wrefresh(diswin);
				rip = 0x400430;
			}


			if(w){
				WINDOW *reswin = subwin(mainwin, RES_L, RES_C, STK_L/2, STK_C/2);
				wattron(reswin, COLOR_PAIR(3));
				wclear(reswin);
				box(reswin, 0, 0);
				mvwaddstr(reswin, 0, 1, " Result ");
				mvwaddstr(reswin, 2, 2, "Congrats! You got the flag :D");
				mvwaddstr(reswin, 3, 2, "  WH2020{A_for_pwning!}");
				wrefresh(reswin);
				sleep(10);
				endwin();
				exit(0);
			}
			else{
				WINDOW *reswin = subwin(mainwin, RES_L, RES_C, STK_L/2, STK_C/2);
				wattron(reswin, COLOR_PAIR(3));
				wclear(reswin);
				box(reswin, 0, 0);
				mvwaddstr(reswin, 0, 1, " Result ");
				mvwaddstr(reswin, 2, 2, "Segmentation fault (core dumped)");
				sprintf(reg, "rip:  0x%016llx", rip);
				mvwaddstr(reswin, 3, 2, reg);
				wrefresh(reswin);
				sleep(10);
				endwin();
				exit(0);
			}
		}
		/* backspace */
		else if(ch == '\x7f'){
			if(len_in <= 0)
				continue;
			if((len_in >= 3 && buf_in[len_in-3] == '\\') ||
			   (len_in >= 2 && buf_in[len_in-2] == '\\') ){
				/* dont update stack */
			}
			else{
				/* update stack */
				len--;
				char tmp[3];
				sprintf(tmp, "%02X", buf[len]&0xff);
				int row = len/8; int col = len%8;
				mvwaddstr(stkwin, 2+row, STK_C-5-3*col, tmp);
				wrefresh(stkwin);
			}
			/* update input buffer */
			if(len_in >= 4 && buf_in[len_in-4] == '\\'){
				len_in -= 4;
				memset(&buf_in[len_in], '\x00', 4);
			}
			else if(len_in >= 3 && buf_in[len_in-3] == '\\'){
				len_in -= 3;
				memset(&buf_in[len_in], '\x00', 3);
			}
			else if(len_in >= 2 && buf_in[len_in-2] == '\\'){
				len_in -= 2;
				memset(&buf_in[len_in], '\x00', 2);
			}
			else{
				buf_in[--len_in] = '\x00';
			}
			mvwaddstr(inwin, 1, 2, buf_in);
			wclrtoeol(inwin);
			wrefresh(inwin);

			
		}
		else if(ch == '\\'){
			if(buf_in[len_in-2] == '\\')
				continue;
			if(buf_in[len_in-3] == '\\')
				continue;
			buf_in[len_in++] = '\\';
			buf_in[len_in++] = 'x';
			mvwaddstr(inwin, 1, 2, buf_in);
			wrefresh(inwin);
		}
		else{
			if(len < 88){
				/* escape */
				if(len_in >= 2 && ( buf_in[len_in-2] == '\\' || buf_in[len_in-3] == '\\' )){
					if( (ch >= 'a' && ch <= 'f') ||
						(ch >= 'A' && ch <= 'F') ||
						(ch >= '0' && ch <= '9') ){

						if(buf_in[len_in-2] == '\\'){
							buf_in[len_in++] = ch;
							mvwaddstr(inwin, 1, 2, buf_in);
							wrefresh(inwin);
						}
						else{
							buf_in[len_in++] = ch;
							mvwaddstr(inwin, 1, 2, buf_in);
							wrefresh(inwin);
							buf[len] = strtol(&buf_in[len_in-2], NULL, 16)&0xff;
							/* update stack */
							char tmp[3];
							sprintf(tmp, "%02X", buf[len]&0xff);
							int row = len/8; int col = len%8;
							wattron(stkwin, COLOR_PAIR(1));
							mvwaddstr(stkwin, 2+row, STK_C-5-3*col, tmp);
							wattroff(stkwin, COLOR_PAIR(1));
							wrefresh(stkwin);
							len++;
						}
					}
				}
				/* non-escape */
				else{
					/* update stack */
					char tmp[3];
					sprintf(tmp, "%02X", ch);
					int row = len/8; int col = len%8;
					wattron(stkwin, COLOR_PAIR(1));
					mvwaddstr(stkwin, 2+row, STK_C-5-3*col, tmp);
					wattroff(stkwin, COLOR_PAIR(1));
					wrefresh(stkwin);

					/* update input buffer */
					buf[len] = ch; 
					buf_in[len_in] = ch; 
					mvwaddstr(inwin, 1, 2, buf_in);
					wrefresh(inwin);
					len++;
					len_in++;
				}

			}
		}
	}

	/* exit */
	endwin();
	return 0;
}
