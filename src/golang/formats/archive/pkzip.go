package archive

import "github.com/casastorta/magic-number-proto/src/golang/types"

var PKZIPMagicNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x50, 0x4B, 0x03, 0x04}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x50, 0x4B, 0x05, 0x06}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0x50, 0x4B, 0x07, 0x08}},
	}},
}}
