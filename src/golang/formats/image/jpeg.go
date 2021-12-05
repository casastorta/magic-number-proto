package image

import (
	"github.com/casastorta/magic-number-proto/src/golang/types"
)

var JPEGMagicNumbers = types.FormatMagicNumbers{FormatMagicNumbers: []types.MagicNumberSet{
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFF, 0xD8, 0xFF, 0xDB}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFF, 0xD8, 0xFF, 0xEE}},
	}},
	{MagicNumbers: []types.SingleMagicNumber{
		{Offset: 0, Bytes: []byte{0xFF, 0xD8, 0xFF, 0xE1}},
		{Offset: 6, Bytes: []byte{0x45, 0x78, 0x69, 0x66, 0x00, 0x00}},
	}},
}}
