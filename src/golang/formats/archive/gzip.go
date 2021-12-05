package archive

import "github.com/casastorta/magic-number-proto/src/golang/types"

var GZIPMagicNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x1F, 0x8B}},
	}},
}}
