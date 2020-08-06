package main

import (
	"bytes"
	"compress/zlib"
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"runtime"
)

const FLAGNAME = "flag.png"
const PORT = ":8080"

type Whitehacksv2 struct {
	Magic []byte
	Files []*Whitehacksv2_Tlv
}

func (this *Whitehacksv2) Read(ioX *bytes.Buffer) error {
	magic := make([]byte, 16)
	if _, err := ioX.Read(magic); err != nil {
		log.Fatal(err)
	}
	magicCheck := []byte{87, 72, 73, 84, 69, 72, 65, 67, 75, 83, 86, 50, 0, 0, 0, 0}
	if !bytes.Equal(magicCheck, magic) {
		return errors.New("Magic does not match: " + string(magicCheck))
	}
	this.Magic = magic

	for true {
		if _, err := ioX.ReadByte(); err == io.EOF {
			return nil
		}
		ioX.UnreadByte()

		tlv := Whitehacksv2_Tlv{}
		if err := tlv.Read(ioX); err == io.EOF {
			return nil
		}
		this.Files = append(this.Files, &tlv)
	}

	return nil
}

type Whitehacksv2_Tlv struct {
	FileName             string
	FileSizeCompressed   uint32
	FileSizeUncompressed uint32
	FileData             []byte
}

func (this *Whitehacksv2_Tlv) Read(ioX *bytes.Buffer) error {
	filename, err := ioX.ReadBytes(byte(0))
	if err != nil {
		return err
	}
	this.FileName = string(filename[:len(filename)-1])

	fileSizeCompressed := make([]byte, 4)
	if _, err := ioX.Read(fileSizeCompressed); err != nil {
		return err
	}
	this.FileSizeCompressed = binary.LittleEndian.Uint32(fileSizeCompressed)

	fileSizeUncompressed := make([]byte, 4)
	if _, err := ioX.Read(fileSizeUncompressed); err != nil {
		return err
	}
	this.FileSizeUncompressed = binary.LittleEndian.Uint32(fileSizeUncompressed)

	fileData := make([]byte, this.FileSizeCompressed)
	if _, err := ioX.Read(fileData); err != nil {
		return err
	}
	r, err := zlib.NewReader(bytes.NewReader(fileData))
	if err != nil {
		return err
	}
	if this.FileName != FLAGNAME {
		this.FileData, _ = ioutil.ReadAll(r)
		log.Printf("File %s of size %d bytes loaded", this.FileName, this.FileSizeUncompressed)
	} else {
		log.Printf("File %s is skipped.", this.FileName)
	}

	return nil
}

func main() {
	f, err := os.Open("baby-parser2.wh")
	if err != nil {
		log.Fatal(err)
	}

	data := &bytes.Buffer{}
	if _, err := data.ReadFrom(f); err != nil {
		log.Fatal(err)
	}

	obj := Whitehacksv2{}
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
