package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"strings"

	"github.com/casastorta/magic-number-proto/src/golang/formats/archive"
	"github.com/casastorta/magic-number-proto/src/golang/formats/misc"
	"github.com/casastorta/magic-number-proto/src/golang/types"

	"github.com/casastorta/magic-number-proto/src/golang/formats/image"
)

const MaxChunkSize = 40

func main() {
	testBasePath := "../../tests/resources"
	testCases := []string{
		fmt.Sprintf("%s/empty_file.bin", testBasePath),
		fmt.Sprintf("%s/jfif_jpeg.jpeg", testBasePath),
		fmt.Sprintf("%s/olympus-c960.jpg", testBasePath),
		fmt.Sprintf("%s/PNG_transparency_demonstration_1.png", testBasePath),
		fmt.Sprintf("%s/sample.pdf", testBasePath),
		fmt.Sprintf("%s/small_archive.zip", testBasePath),
		fmt.Sprintf("%s/small_file.txt", testBasePath),
	}

	tests := map[string]types.FormatMagicNumbers{
		"JPEG":   image.JPEGMagicNumbers,
		"PNG":    image.PNGMagicNumbers,
		"JPEG2K": image.JPEG2KMagigNumbers,

		"PKZIP": archive.PKZIPMagicNumbers,
		"GZIP":  archive.GZIPMagicNumbers,
		"XZ":    archive.XZMagicNumbers,

		"PDF": misc.PDFMagicNumbers,
	}

	for _, testCase := range testCases {

		f, err := os.Open(testCase)
		if err != nil {
			panic(err)
		}

		payloadBytes, err := ioutil.ReadAll(io.LimitReader(f, MaxChunkSize))
		if err != nil {
			panic(err)
		}

		for testName, test := range tests {
			testOutcome, err := test.CheckPayload(&payloadBytes)
			fmt.Printf("%s is %s: %t, had error: %t\n", testCase, testName, testOutcome, err != nil)
		}

		fmt.Println(strings.Repeat("-", 40))

		defer f.Close()
	}
}
