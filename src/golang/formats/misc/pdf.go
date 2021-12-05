package misc

import "github.com/casastorta/magic-number-proto/src/golang/types"

var PDFMagicNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x25, 0x50, 0x44, 0x46, 0x2D}},
	}},
}}
