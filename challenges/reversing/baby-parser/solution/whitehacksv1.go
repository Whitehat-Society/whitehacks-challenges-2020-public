package main

import (
	"bytes"
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"runtime"
)

const FLAGNAME = "flag.png"
const PORT = ":8080"

type Whitehacksv1 struct {
	Magic []byte
	Files []*Whitehacksv1_Tlv
}

func (this *Whitehacksv1) Read(ioX *bytes.Buffer) error {
	magic := make([]byte, 16)
	if _, err := ioX.Read(magic); err != nil {
		log.Fatal(err)
	}
	magicCheck := []byte{87, 72, 73, 84, 69, 72, 65, 67, 75, 83, 86, 49, 0, 0, 0, 0}
	if !bytes.Equal(magicCheck, magic) {
		return errors.New("Magic does not match: " + string(magicCheck))
	}
	this.Magic = magic

	for true {
		if _, err := ioX.ReadByte(); err == io.EOF {
			return nil
		}
		ioX.UnreadByte()

		tlv := Whitehacksv1_Tlv{}
		if err := tlv.Read(ioX); err != io.EOF {
			this.Files = append(this.Files, &tlv)
		}
	}

	return nil
}

type Whitehacksv1_Tlv struct {
	FileName string
	FileSize uint32
	FileData []byte
}

func (this *Whitehacksv1_Tlv) Read(ioX *bytes.Buffer) error {
	filename, err := ioX.ReadBytes(byte(0))
	if err != nil {
		return err
	}
	this.FileName = string(filename[:len(filename)-1])

	fileSize := make([]byte, 4)
	if _, err := ioX.Read(fileSize); err != nil {
		return err
	}
	this.FileSize = binary.LittleEndian.Uint32(fileSize)

	fileData := make([]byte, this.FileSize)
	if _, err := ioX.Read(fileData); err != nil {
		return err
	}
	if this.FileName != FLAGNAME {
		this.FileData = fileData
		log.Printf("File %s of size %d bytes loaded", this.FileName, this.FileSize)
	} else {
		log.Printf("File %s is skipped.", this.FileName)
	}

	return nil
}

func main() {
	f, err := os.Open("baby-parser1.wh")
	if err != nil {
		log.Fatal(err)
	}

	data := &bytes.Buffer{}
	if _, err := data.ReadFrom(f); err != nil {
		log.Fatal(err)
	}

	obj := Whitehacksv1{}
	if err := obj.Read(data); err != nil {
		log.Fatal(err)
	}

	f.Close()
	runtime.GC()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		requestURI := r.RequestURI[1:]
		if requestURI == "" {
			requestURI = "index.html"
		} else if requestURI == FLAGNAME {
			http.Redirect(w, r, "/", http.StatusTemporaryRedirect)
			return
		}

		for _, file := range obj.Files {
			if file.FileName == FLAGNAME {
				continue
			}

			if requestURI == file.FileName {
				if _, err := io.Copy(w, bytes.NewBuffer(file.FileData)); err != nil {
					log.Fatal(err)
				}
				return
			}
		}

		fileList := &bytes.Buffer{}
		for _, file := range obj.Files {
			if file.FileName == FLAGNAME {
				continue
			}

			if _, err := fmt.Fprintf(fileList, "<li><a href=\"/%s\">%s</a></li>", file.FileName, file.FileName); err != nil {
				log.Fatal(err)
			}
		}
		fmt.Fprintf(w, "<html><body><h1>Files:</h1><ul>%s</ul></body></html>", fileList)
	})
	log.Printf("Serving at port %s", PORT)
	http.ListenAndServe(PORT, nil)
}
