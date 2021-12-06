# Magic Number Detection Prototype

This project contains prototype codebase which can be used to perform 
["magic number" checks](https://en.wikipedia.org/wiki/List_of_file_signatures) against
files of different types.

As a quick prototype implementation, this code has couple of features and limitations:

- It will detect formats based on first _n_ bytes of the content (hardcoeded default values
  is `40`)
- It is able to detect magic numbers in file formats with multiple different offsets
  (see JPEG magic numbers structure implementation, one magic nubmer for JPEG formats needs
  to be verified by both data starting at offset bytes `0` and `6`)

There are couple of known but unsupported use-cases:
- Filetypes with flexible/repeatable offsets (containers formats like Amiga IFF)
- Filetypes with repeating offset (for example MPEG-2)
- Filetypes with negative offset relative to the end of file (for example Apple Disk Image)

## Demos

### Python

[Python implementation](src/python/demo.py) is kind of the main one, implemented in single file 
and well documented through comments in the source code. This is because Python is likely the most 
readable language  for most of the developers, even if they are not Python programmers.

Run the Python demo like this:

```bash
cd src/python && python3 demo.py ; cd -
```

<details><summary>Output of Python demo should be something like:</summary>

```text
Dev/magic-number-proto/tests/resources/empty_file.bin 
 header is: b''
 -> Dev/magic-number-proto/tests/resources/empty_file.bin is some of the image formats: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is JPEG: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is PNG: False

 -> Dev/magic-number-proto/tests/resources/empty_file.bin PDF: False

 -> Dev/magic-number-proto/tests/resources/empty_file.bin is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/empty_file.bin is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg 
 header is: b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00\xd8\x00\xd8\x00\x00\xff\xed\x008Photoshop 3.0\x008B'
 -> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is some of the image formats: True
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is JPEG: True
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is PNG: False

 -> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg PDF: False

 -> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/jfif_jpeg.jpeg is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/olympus-c960.jpg 
 header is: b'\xff\xd8\xff\xe1\x1b\xfdExif\x00\x00II*\x00\x08\x00\x00\x00\x0b\x00\x0e\x01\x02\x00 \x00\x00\x00\x92\x00\x00\x00\x0f\x01\x02\x00\x18\x00'
 -> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is some of the image formats: True
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is JPEG: True
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is PNG: False

 -> Dev/magic-number-proto/tests/resources/olympus-c960.jpg PDF: False

 -> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/olympus-c960.jpg is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png 
 header is: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x03 \x00\x00\x02X\x08\x06\x00\x00\x00\x9av\x82p\x00\x03v<IDA'
 -> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is some of the image formats: True
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is JPEG: False
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is PNG: True

 -> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png PDF: False

 -> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/PNG_transparency_demonstration_1.png is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/sample.pdf 
 header is: b'%PDF-1.3\r\n%\xe2\xe3\xcf\xd3\r\n\r\n1 0 obj\r\n<<\r\n/Type /C'
 -> Dev/magic-number-proto/tests/resources/sample.pdf is some of the image formats: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is JPEG: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is PNG: False

 -> Dev/magic-number-proto/tests/resources/sample.pdf PDF: True

 -> Dev/magic-number-proto/tests/resources/sample.pdf is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/sample.pdf is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/small_archive.zip 
 header is: b'PK\x03\x04\n\x00\x00\x00\x00\x00\x14X\x84S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x1c\x00tests/reso'
 -> Dev/magic-number-proto/tests/resources/small_archive.zip is some of the image formats: False
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is JPEG: False
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is PNG: False

 -> Dev/magic-number-proto/tests/resources/small_archive.zip PDF: False

 -> Dev/magic-number-proto/tests/resources/small_archive.zip is some of the archive formats: True
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is (PK)ZIP: True
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/small_archive.zip is XZ: False
----------------------------------------------------------------------
Dev/magic-number-proto/tests/resources/small_file.txt 
 header is: b'ABC\n'
 -> Dev/magic-number-proto/tests/resources/small_file.txt is some of the image formats: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is JPEG: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is JPEG2k: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is PNG: False

 -> Dev/magic-number-proto/tests/resources/small_file.txt PDF: False

 -> Dev/magic-number-proto/tests/resources/small_file.txt is some of the archive formats: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is (PK)ZIP: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is GZIP: False
 `-> Dev/magic-number-proto/tests/resources/small_file.txt is XZ: False
----------------------------------------------------------------------
```
</details>

### Go (Golang)

Golang implementation is not a simple rewrite of Python implementation, but actually 
utilizes Go features like go-style error handling (no `try`/`catch` there) and uses
`struct` type to define template for the magic numbers definitions and `CheckPayload` method
of it. 

Hence, it has slightly more complex structure, but likely the one which sligtly better reflects 
the structure which you would implement in some other programming languages (like Java).

Run the Golang demo like this:

```bash
cd src/golang && go run main.go ; cd -
```

<details><summary>Output of Golang demo should be something like this:</summary>

```text
../../tests/resources/empty_file.bin is PNG: false, had error: true
../../tests/resources/empty_file.bin is JPEG2K: false, had error: true
../../tests/resources/empty_file.bin is PKZIP: false, had error: true
../../tests/resources/empty_file.bin is GZIP: false, had error: true
../../tests/resources/empty_file.bin is XZ: false, had error: true
../../tests/resources/empty_file.bin is PDF: false, had error: true
../../tests/resources/empty_file.bin is JPEG: false, had error: true
----------------------------------------
../../tests/resources/jfif_jpeg.jpeg is PDF: false, had error: false
../../tests/resources/jfif_jpeg.jpeg is JPEG: true, had error: false
../../tests/resources/jfif_jpeg.jpeg is PNG: false, had error: false
../../tests/resources/jfif_jpeg.jpeg is JPEG2K: false, had error: false
../../tests/resources/jfif_jpeg.jpeg is PKZIP: false, had error: false
../../tests/resources/jfif_jpeg.jpeg is GZIP: false, had error: false
../../tests/resources/jfif_jpeg.jpeg is XZ: false, had error: false
----------------------------------------
../../tests/resources/olympus-c960.jpg is JPEG: true, had error: false
../../tests/resources/olympus-c960.jpg is PNG: false, had error: false
../../tests/resources/olympus-c960.jpg is JPEG2K: false, had error: false
../../tests/resources/olympus-c960.jpg is PKZIP: false, had error: false
../../tests/resources/olympus-c960.jpg is GZIP: false, had error: false
../../tests/resources/olympus-c960.jpg is XZ: false, had error: false
../../tests/resources/olympus-c960.jpg is PDF: false, had error: false
----------------------------------------
../../tests/resources/PNG_transparency_demonstration_1.png is JPEG: false, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is PNG: true, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is JPEG2K: false, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is PKZIP: false, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is GZIP: false, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is XZ: false, had error: false
../../tests/resources/PNG_transparency_demonstration_1.png is PDF: false, had error: false
----------------------------------------
../../tests/resources/sample.pdf is JPEG: false, had error: false
../../tests/resources/sample.pdf is PNG: false, had error: false
../../tests/resources/sample.pdf is JPEG2K: false, had error: false
../../tests/resources/sample.pdf is PKZIP: false, had error: false
../../tests/resources/sample.pdf is GZIP: false, had error: false
../../tests/resources/sample.pdf is XZ: false, had error: false
../../tests/resources/sample.pdf is PDF: true, had error: false
----------------------------------------
../../tests/resources/small_archive.zip is XZ: false, had error: false
../../tests/resources/small_archive.zip is PDF: false, had error: false
../../tests/resources/small_archive.zip is JPEG: false, had error: false
../../tests/resources/small_archive.zip is PNG: false, had error: false
../../tests/resources/small_archive.zip is JPEG2K: false, had error: false
../../tests/resources/small_archive.zip is PKZIP: true, had error: false
../../tests/resources/small_archive.zip is GZIP: false, had error: false
----------------------------------------
../../tests/resources/small_file.txt is PKZIP: false, had error: false
../../tests/resources/small_file.txt is GZIP: false, had error: false
../../tests/resources/small_file.txt is XZ: false, had error: false
../../tests/resources/small_file.txt is PDF: false, had error: false
../../tests/resources/small_file.txt is JPEG: false, had error: false
../../tests/resources/small_file.txt is PNG: false, had error: false
../../tests/resources/small_file.txt is JPEG2K: false, had error: false
----------------------------------------
```
</details>