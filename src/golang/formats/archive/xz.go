package archive

import "github.com/casastorta/magic-number-proto/src/golang/types"

var XZMagicNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFD, 0x37, 0x7A, 0x58, 0x5A, 0x00}},
	}},
}}
