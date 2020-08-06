GOCMD = go
GOBUILD = $(GOCMD) build -ldflags="-s -w"
GOWINARGS = CGO_ENABLED=0 GOOS=windows GOARCH=amd64
GOLINUXARGS = CGO_ENABLED=0 GOOS=linux GOARCH=amd64
GOWINEXT = .exe
GOLINUXEXT = .elf

all: build-wh-files build-go-windows build-go-linux

make-directory:
	mkdir ./build 2>/dev/null

build-wh-files: make-directory
	for baby_dir in `ls -d baby-parser*`; do \
		python3 $$baby_dir/baby-parser*.py ; \
	done

build-go-windows: make-directory
	$(GOWINARGS) $(GOBUILD) -o ./build/whitehacksv1$(GOWINEXT) ./solution/whitehacksv1.go
	$(GOWINARGS) $(GOBUILD) -o ./build/whitehacksv2$(GOWINEXT) ./solution/whitehacksv2.go
	$(GOWINARGS) $(GOBUILD) -o ./build/whitehacksv3$(GOWINEXT) ./solution/whitehacksv3.go
	# $(GOWINARGS) $(GOBUILD) -o ./build/whitehacksv45$(GOWINEXT) ./solution/whitehacks.go ./solution/whitehacksv4.go ./solution/whitehacksv5.go

build-go-linux: make-directory
	$(GOLINUXARGS) $(GOBUILD) -o ./build/whitehacksv1$(GOLINUXEXT) ./solution/whitehacksv1.go
	$(GOLINUXARGS) $(GOBUILD) -o ./build/whitehacksv2$(GOLINUXEXT) ./solution/whitehacksv2.go
	$(GOLINUXARGS) $(GOBUILD) -o ./build/whitehacksv3$(GOLINUXEXT) ./solution/whitehacksv3.go
	# $(GOLINUXARGS) $(GOBUILD) -o ./build/whitehacksv45$(GOLINUXEXT) ./solution/whitehacks.go ./solution/whitehacksv4.go ./solution/whitehacksv5.go

clean:
	rm -rf ./build