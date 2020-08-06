#include <time.h> 
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <SDL2/SDL.h>
#include <sys/stat.h>
#include <sys/types.h>

void err(const char * msg){
	fprintf(stderr, "[-] Error: %s\n", msg);
	exit(-1);
}

#define max(a,b) \
({ __typeof__ (a) _a = (a); \
   __typeof__ (b) _b = (b); \
 _a > _b ? _a : _b; })

typedef unsigned short WORD;
typedef unsigned int DWORD;
typedef unsigned int LONG;
typedef struct __attribute__((__packed__)) tagBITMAPFILEHEADER {
	WORD  bfType;
	DWORD bfSize;
	WORD  bfReserved1;
	WORD  bfReserved2;
	DWORD bfOffBits;
} BITMAPFILEHEADER, *LPBITMAPFILEHEADER, *PBITMAPFILEHEADER;

typedef struct tagBITMAPINFOHEADER {
	DWORD biSize;
	LONG  biWidth;
	LONG  biHeight;
	WORD  biPlanes;
	WORD  biBitCount;
	DWORD biCompression;
	DWORD biSizeImage;
	LONG  biXPelsPerMeter;
	LONG  biYPelsPerMeter;
	DWORD biClrUsed;
	DWORD biClrImportant;
} BITMAPINFOHEADER, *LPBITMAPINFOHEADER, *PBITMAPINFOHEADER;


const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;
//The window we'll be rendering to
SDL_Window* window = NULL;
//The surface contained by the window
SDL_Surface* screenSurface = NULL;
int main(int argc, char * argv[]){
	if( argc < 2 ){
		err("Proper usage: jifviewer <jif file path>");
	}

	/* create temporary directory and unzip */
	char dir_name[32];
	snprintf(dir_name, 32, "/tmp/jif-%ld", time(0));
	if(!mkdir(dir_name, 0777)){
		char cmd[128];
		snprintf(cmd, 128, "cp %s %s", argv[1], dir_name);
		system(cmd);

		if(chdir(dir_name)){
			err("Permission to open a new directory is denied");
		}

		system("unzip *.jif -x \"*..*\" && rm *.jif");
	}
	else{
		err("Permission to create a new directory is denied");
	}

	/* SDL initialisation taken from https://lazyfoo.net/tutorials/SDL/01_hello_SDL/index2.php */
	//Initialize SDL
	if( SDL_Init( SDL_INIT_VIDEO ) < 0 ){
		printf( "SDL could not initialize! SDL_Error: %s\n", SDL_GetError() );
	}
	else{
		//Create window
		window = SDL_CreateWindow( "JIF Viewer v1.3.3.7", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN );
		if( window == NULL ){
			printf( "Window could not be created! SDL_Error: %s\n", SDL_GetError() );
		}
		else{
			//Get window surface
			screenSurface = SDL_GetWindowSurface( window );
		}
	}

	/* Iterate through frames and display */
	int frame_no = 0;
	int frame_fd = -1;
	char frame_name[64];
	struct {
		unsigned char b;
		unsigned char g;
		unsigned char r;
	} * bitmap_row = 0;
	BITMAPFILEHEADER file_header;
	BITMAPINFOHEADER info_header;
	
	while(1){
		snprintf(frame_name, 64, "%u.bmp", frame_no);
		frame_fd = open(frame_name, O_RDONLY);
		if(frame_fd < 0)
			break;

		read(frame_fd, &file_header, sizeof(file_header));
		read(frame_fd, &info_header, sizeof(info_header));

		if(file_header.bfType != 0x4d42)
			err("Frame is not a BMP image");
		if(info_header.biBitCount != 24)
			err("Only 24-bit BMP images supported");
	
		if(!bitmap_row){
			if(info_header.biWidth > 640)
				err("Frame is too large, please keep frame size within 640x480");
			bitmap_row = alloca(info_header.biWidth*3);
		}

		lseek(frame_fd, file_header.bfOffBits, SEEK_SET);
		for(int y = 0; y < info_header.biHeight; y++){
			read(frame_fd, bitmap_row, info_header.biWidth*3);
			for(int x = 0; x < info_header.biWidth; x++){
				SDL_Rect dstrect;
				dstrect.x = x; dstrect.y = SCREEN_HEIGHT-y; dstrect.w = 1; dstrect.h = 1;
				SDL_FillRect( screenSurface, &dstrect, SDL_MapRGB( screenSurface->format, bitmap_row[x].r, bitmap_row[x].g, bitmap_row[x].b ) );
			}
			SDL_UpdateWindowSurface( window );
		}
		/* use bfReserved1 for delay if necessary */
		SDL_Delay( max(file_header.bfReserved1, 200) );
		frame_no++;
	}

	//Destroy window
	SDL_DestroyWindow( window );
	//Quit SDL subsystems
	SDL_Quit();
}
