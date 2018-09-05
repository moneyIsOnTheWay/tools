package main

import (
	"log"
	"net/http"
	"os"
)

func main() {

	os.Mkdir("file", 0777)
	http.Handle("/list/", http.StripPrefix("/list/", http.FileServer(http.Dir("file"))))
	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}

}

//build时候注意build参数
//linux:CGO_ENABLED=0;GOOS=linux;GOARCH=amd64
//window:CGO_ENABLED=0;GOOS=windows;GOARCH=amd64
