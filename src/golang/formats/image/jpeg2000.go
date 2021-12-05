package image

import "github.com/casastorta/magic-number-proto/src/golang/types"

var JPEG2KMagigNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x00, 0x00, 0x00, 0x0C, 0x6A, 0x50, 0x20, 0x20, 0x0D, 0x0A, 0x87, 0x0A}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFF, 0x4F, 0xFF, 0x51}},
	}},
}}
